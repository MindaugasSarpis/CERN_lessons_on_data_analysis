"""US state population growth 2000-2010, coloured by region (Wilke fig 4.2)."""

from __future__ import annotations

import matplotlib.pyplot as plt

from cwilke import data as D
from cwilke.theme import apply_base, save, vgrid


REGION_COLORS = {
    "West":      "#E69F00",
    "South":     "#56B4E9",
    "Midwest":   "#009E73",
    "Northeast": "#F0E442",
}


def render() -> None:
    apply_base()

    df = D.us_popgrowth().sort_values("popgrowth")
    y = range(len(df))
    colours = df["region"].map(REGION_COLORS).tolist()

    fig, ax = plt.subplots(figsize=(6.2, 9.5))
    ax.barh(list(y), df["popgrowth"].values * 100,
            color=colours, edgecolor="white", linewidth=0.4)
    ax.set_yticks(list(y))
    ax.set_yticklabels(df["state"].values, fontsize=9)
    ax.set_xlabel("population growth, 2000 to 2010 (%)")
    ax.set_xlim(-2, 37.5)
    ax.axvline(0, color="#2c3e50", linewidth=0.6)

    # Legend
    from matplotlib.patches import Patch
    handles = [Patch(facecolor=c, label=r) for r, c in REGION_COLORS.items()]
    ax.legend(handles=handles, loc="lower right", fontsize=10,
              frameon=True, framealpha=0.9, edgecolor="none")

    vgrid(ax)
    ax.margins(y=0.008)
    fig.tight_layout()
    save(fig, "color", "popgrowth_us_regions")


if __name__ == "__main__":
    render()
