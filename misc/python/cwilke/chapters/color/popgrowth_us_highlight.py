"""US population growth with Texas and Louisiana highlighted (Wilke fig 4.4)."""

from __future__ import annotations

import matplotlib.pyplot as plt
from matplotlib.patches import Patch

from cwilke import data as D
from cwilke.theme import apply_base, save, vgrid


# Desaturated / lightened baseline regional colours
BASE_COLORS = {
    "West":      "#F1D49B",
    "South":     "#B7DCF2",
    "Midwest":   "#A7D8C5",
    "Northeast": "#F6F0B8",
}
HIGHLIGHT = "#2A7BB0"  # darkened sky blue
HIGHLIGHT_STATES = ("Texas", "Louisiana")


def render() -> None:
    apply_base()

    df = D.us_popgrowth().sort_values("popgrowth").reset_index(drop=True)

    colours = []
    label_colors = []
    label_weights = []
    for _, row in df.iterrows():
        if row["state"] in HIGHLIGHT_STATES:
            colours.append(HIGHLIGHT)
            label_colors.append(HIGHLIGHT)
            label_weights.append("bold")
        else:
            colours.append(BASE_COLORS[row["region"]])
            label_colors.append("#555555")
            label_weights.append("normal")

    fig, ax = plt.subplots(figsize=(6.2, 9.5))
    ax.barh(range(len(df)), df["popgrowth"].values * 100,
            color=colours, edgecolor="white", linewidth=0.4)
    ax.set_yticks(range(len(df)))
    ax.set_yticklabels(df["state"].values, fontsize=9)
    for tick, colour, weight in zip(ax.get_yticklabels(),
                                    label_colors, label_weights):
        tick.set_color(colour)
        tick.set_fontweight(weight)
    ax.set_xlabel("population growth, 2000 to 2010 (%)")
    ax.set_xlim(-2, 37.5)
    ax.axvline(0, color="#2c3e50", linewidth=0.6)

    handles = [Patch(facecolor=c, label=r) for r, c in BASE_COLORS.items()]
    ax.legend(handles=handles, loc="lower right", fontsize=10,
              frameon=True, framealpha=0.9, edgecolor="none")

    vgrid(ax)
    ax.margins(y=0.008)
    fig.tight_layout()
    save(fig, "color", "popgrowth_us_highlight")


if __name__ == "__main__":
    render()
