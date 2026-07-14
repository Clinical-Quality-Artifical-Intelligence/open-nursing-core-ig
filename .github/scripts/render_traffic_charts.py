"""Renders traffic/clones.csv and traffic/views.csv into PNG line charts.

Run from the repo root with the traffic-data branch checked out (see
.github/workflows/traffic.yml). Reads the CSVs the merge step just wrote and
overwrites traffic/clones.png and traffic/views.png so the images committed
alongside the data always match it.
"""
import csv
import os

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

TRAFFIC_DIR = "traffic"


def load(path):
    if not os.path.exists(path):
        return []
    with open(path) as f:
        return [(r["date"], int(r["count"]), int(r["uniques"])) for r in csv.DictReader(f)]


def render(rows, title, out_path, color):
    dates = [d[5:] for d, _, _ in rows]
    counts = [c for _, c, _ in rows]

    fig, ax = plt.subplots(figsize=(9, 3), dpi=150)
    ax.plot(dates, counts, marker="o", markersize=4, color=color, linewidth=2)
    ax.set_title(title, fontsize=13, fontweight="bold", loc="left", color="#1C2530")
    ax.set_ylim(bottom=0)
    ax.tick_params(axis="x", labelsize=7, rotation=45)
    ax.tick_params(axis="y", labelsize=8)
    ax.grid(axis="y", color="#DCE4ED", linewidth=0.8)
    ax.set_axisbelow(True)
    for spine in ("top", "right", "left"):
        ax.spines[spine].set_visible(False)
    ax.spines["bottom"].set_color("#DCE4ED")
    fig.tight_layout()
    fig.savefig(out_path, facecolor="white")
    plt.close(fig)


def main():
    clones = load(f"{TRAFFIC_DIR}/clones.csv")
    if clones:
        render(clones, "Daily repository clones", f"{TRAFFIC_DIR}/clones.png", "#005EB8")

    views = load(f"{TRAFFIC_DIR}/views.csv")
    if views:
        render(views, "Daily page views", f"{TRAFFIC_DIR}/views.png", "#F2994A")


if __name__ == "__main__":
    main()
