"""Fix: colour by region, direct-label a subset of states (Wilke fig 19.2)."""

from __future__ import annotations

import matplotlib.pyplot as plt

from cwilke import data as D
from cwilke.theme import apply_base, grid, save


REGION_COLORS = {
    "West":      "#E69F00",
    "South":     "#56B4E9",
    "Midwest":   "#009E73",
    "Northeast": "#F0E442",
}

LABELED_STATES = {
    "Alaska", "Arizona", "California", "Florida", "Wisconsin",
    "Louisiana", "Nevada", "Michigan", "Montana", "New Mexico",
    "Pennsylvania", "New York", "Oregon", "Rhode Island",
    "Tennessee", "Texas", "Utah", "Vermont",
}


def render() -> None:
    apply_base()

    df = D.us_popgrowth()

    fig, ax = plt.subplots(figsize=(7.8, 5.4))
    for region, colour in REGION_COLORS.items():
        sub = df[df["region"] == region]
        ax.scatter(sub["pop2000"], sub["popgrowth"] * 100,
                   s=60, facecolor=colour,
                   edgecolor="white", linewidth=0.7,
                   label=region, zorder=3)

    for _, row in df.iterrows():
        if row["state"] not in LABELED_STATES:
            continue
        ax.annotate(row["state"],
                    (row["pop2000"], row["popgrowth"] * 100),
                    xytext=(8, 3), textcoords="offset points",
                    fontsize=9, color="#2c3e50")

    ax.set_xscale("log")
    ax.set_xlabel("population size in 2000")
    ax.set_ylabel("population growth, 2000 to 2010 (%)")
    ax.legend(loc="lower left", fontsize=10, title="region",
              frameon=True, framealpha=0.9, edgecolor="none")
    grid(ax)

    fig.tight_layout()
    save(fig, "pitfalls_of_color_use", "popgrowth_vs_popsize_direct_label")


if __name__ == "__main__":
    render()
