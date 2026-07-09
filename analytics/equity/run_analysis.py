#!/usr/bin/env python3
"""
ONC equity analytics: pressure-ulcer detection timeliness by Monk skin tone.

Pipeline (mirrors the Open Health Stack fhir-data-pipes flow at demo scale):
    FHIR NDJSON  ->  Parquet (flat analysis views)  ->  stratified metrics
                 ->  metrics.csv + equity_report.md + chart PNG

In production, run OHS fhir-data-pipes (https://github.com/ohs-foundation/fhir-data-pipes)
in batch mode against your FHIR server to land Patient/Observation Parquet,
then point --parquet at its output directory instead of using the demo NDJSON.

Metrics per Monk band (A-J):
  - n patients / n pressure ulcers
  - median days from skin-tone assessment (baseline) to first PU documentation
  - late-detection rate: % of ulcers first documented at stage 3/4,
    unstageable, or deep-tissue injury

Usage:
    python3 run_analysis.py [--data data] [--out output]
"""
import argparse
import json
from pathlib import Path

import pandas as pd

MONK_BANDS = list("ABCDEFGHIJ")
LATE_STAGES = {"stage-3", "stage-4", "unstageable", "deep-tissue"}

# Chart ink & surface (kept consistent with the IG's NHS-blue identity).
SERIES = "#005EB8"      # validated: lightness band, chroma, >=3:1 on light surface
SURFACE = "#fcfcfb"
INK = "#1a1a1a"
INK_MUTED = "#6b7280"
GRID = "#e5e7eb"


def ndjson(path: Path) -> list[dict]:
    with open(path) as f:
        return [json.loads(line) for line in f if line.strip()]


def build_views(data_dir: Path, parquet_dir: Path) -> pd.DataFrame:
    """Flatten FHIR resources into analysis views and persist as Parquet."""
    monk_rows = []
    for o in ndjson(data_dir / "Observation_monk.ndjson"):
        monk_rows.append({
            "monk_obs_id": o["id"],
            "patient": o["subject"]["reference"].split("/")[1],
            "band": o["valueCodeableConcept"]["coding"][0]["code"],
            "assessed": pd.Timestamp(o["effectiveDateTime"]),
        })
    monk = pd.DataFrame(monk_rows)

    ulcer_rows = []
    for o in ndjson(data_dir / "Observation_ulcer.ndjson"):
        ulcer_rows.append({
            "patient": o["subject"]["reference"].split("/")[1],
            "stage": o["valueCodeableConcept"]["coding"][0]["code"],
            "detected": pd.Timestamp(o["effectiveDateTime"]),
        })
    ulcer = pd.DataFrame(ulcer_rows)

    parquet_dir.mkdir(parents=True, exist_ok=True)
    monk.to_parquet(parquet_dir / "monk_skintone.parquet", index=False)
    ulcer.to_parquet(parquet_dir / "pressure_ulcer.parquet", index=False)

    joined = ulcer.merge(monk, on="patient", how="inner")
    joined["days_to_detection"] = (joined["detected"] - joined["assessed"]).dt.total_seconds() / 86400.0
    joined["late"] = joined["stage"].isin(LATE_STAGES)
    return joined


def compute_metrics(joined: pd.DataFrame, monk_total: pd.Series) -> pd.DataFrame:
    g = joined.groupby("band")
    m = pd.DataFrame({
        "patients_assessed": monk_total,
        "pressure_ulcers": g.size(),
        "median_days_to_detection": g["days_to_detection"].median().round(1),
        "late_detection_rate_pct": (100 * g["late"].mean()).round(1),
    }).reindex(MONK_BANDS)
    m.index.name = "monk_band"
    return m


def render_chart(m: pd.DataFrame, out_png: Path) -> None:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots(figsize=(8.4, 4.6), dpi=150)
    fig.patch.set_facecolor(SURFACE)
    ax.set_facecolor(SURFACE)

    vals = m["late_detection_rate_pct"]
    bars = ax.bar(m.index, vals, width=0.62, color=SERIES, zorder=3)

    # Recessive grid behind thin marks; no top/right chrome.
    ax.grid(axis="y", color=GRID, linewidth=0.8, zorder=0)
    for side in ("top", "right"):
        ax.spines[side].set_visible(False)
    for side in ("left", "bottom"):
        ax.spines[side].set_color(GRID)
    ax.tick_params(colors=INK_MUTED, labelsize=9)

    # Selective direct labels: extremes only; full table lives in metrics.csv.
    finite = vals.dropna()
    if len(finite):
        for band in (finite.idxmin(), finite.idxmax()):
            v = vals[band]
            ax.annotate(f"{v:.0f}%", (band, v), textcoords="offset points",
                        xytext=(0, 4), ha="center", fontsize=9, color=INK)

    ax.set_ylabel("Late-detection rate (%)", color=INK_MUTED, fontsize=9)
    ax.set_xlabel("Monk Skin Tone band (A = lightest, J = darkest)",
                  color=INK_MUTED, fontsize=9)
    ax.set_ylim(0, max(100, float(finite.max()) * 1.15 if len(finite) else 100))
    ax.set_title("Pressure ulcers first documented at stage 3+ / unstageable / deep-tissue,\n"
                 "by Monk skin-tone band", color=INK, fontsize=11, loc="left", pad=12)
    fig.text(0.01, 0.01,
             "SYNTHETIC demonstration data (bias deliberately injected) — not clinical evidence. "
             "Full metrics: metrics.csv",
             fontsize=7.5, color=INK_MUTED)

    fig.tight_layout(rect=(0, 0.04, 1, 1))
    fig.savefig(out_png, facecolor=SURFACE)
    plt.close(fig)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--data", default="data", help="Directory of demo NDJSON input")
    ap.add_argument("--out", default="output")
    args = ap.parse_args()

    here = Path(__file__).parent
    data_dir, out_dir = here / args.data, here / args.out
    out_dir.mkdir(parents=True, exist_ok=True)

    joined = build_views(data_dir, out_dir / "parquet")
    monk_total = pd.read_parquet(out_dir / "parquet" / "monk_skintone.parquet") \
                   .groupby("band").size()
    metrics = compute_metrics(joined, monk_total)

    metrics.to_csv(out_dir / "metrics.csv")
    render_chart(metrics, out_dir / "detection_delay_by_skin_tone.png")

    lightest = metrics.loc["A":"C", "late_detection_rate_pct"].mean()
    darkest = metrics.loc["H":"J", "late_detection_rate_pct"].mean()
    report = f"""# Equity report: pressure-ulcer detection timeliness by skin tone

> **SYNTHETIC demonstration data** — the generator deliberately injects a
> detection-delay bias so this pipeline has an inequity to surface. Do not
> quote these numbers as clinical findings.

| Signal | Value |
|---|---|
| Late-detection rate, bands A–C (lightest) | {lightest:.1f}% |
| Late-detection rate, bands H–J (darkest) | {darkest:.1f}% |
| **Disparity (H–J vs A–C)** | **{darkest - lightest:+.1f} percentage points** |

Per-band metrics: [`metrics.csv`](metrics.csv) · Chart: `detection_delay_by_skin_tone.png`

**Why this matters:** if a service cannot answer "do our pressure-ulcer
detection rates differ across skin tones?", inequity stays invisible. Because
the ONC-IG records skin tone as structured data (Monk Scale) and gates
pressure-area assessment on it, this question becomes a one-join query —
which is exactly what this pipeline demonstrates.
"""
    (out_dir / "equity_report.md").write_text(report)

    print(metrics.to_string())
    print(f"\nDisparity (H–J vs A–C late-detection): {darkest - lightest:+.1f} pp")
    print(f"outputs -> {out_dir}/(metrics.csv, equity_report.md, detection_delay_by_skin_tone.png, parquet/)")


if __name__ == "__main__":
    main()
