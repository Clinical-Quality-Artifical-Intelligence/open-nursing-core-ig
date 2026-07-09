# Equity report: pressure-ulcer detection timeliness by skin tone

> **SYNTHETIC demonstration data** — the generator deliberately injects a
> detection-delay bias so this pipeline has an inequity to surface. Do not
> quote these numbers as clinical findings.

| Signal | Value |
|---|---|
| Late-detection rate, bands A–C (lightest) | 16.5% |
| Late-detection rate, bands H–J (darkest) | 54.4% |
| **Disparity (H–J vs A–C)** | **+37.9 percentage points** |

Per-band metrics: [`metrics.csv`](metrics.csv) · Chart: `detection_delay_by_skin_tone.png`

**Why this matters:** if a service cannot answer "do our pressure-ulcer
detection rates differ across skin tones?", inequity stays invisible. Because
the ONC-IG records skin tone as structured data (Monk Scale) and gates
pressure-area assessment on it, this question becomes a one-join query —
which is exactly what this pipeline demonstrates.
