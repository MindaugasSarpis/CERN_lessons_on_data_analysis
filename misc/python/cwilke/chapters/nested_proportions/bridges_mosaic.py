"""Mosaic plot of bridges: era × material (Wilke fig 11.3).

Width of each column = count of bridges in that era; height of each
stacked piece within a column = proportion of that material within the
era. Every bridge is counted exactly once.
"""

from __future__ import annotations

import matplotlib.patches as mpatches
import matplotlib.pyplot as plt

from cwilke import data as D
from cwilke.theme import apply_base, save


ERAS = ["crafts", "emerging", "mature", "modern"]
MATERIALS = ["iron", "steel", "wood"]
MAT_COLORS = {
    "iron":  "#D55E00",
    "steel": "#0072B2",
    "wood":  "#009E73",
}


def render() -> None:
    apply_base()
    df = D.bridges()
    n = len(df)

    # era totals -> column widths.
    era_counts = df["erected"].value_counts().reindex(ERAS, fill_value=0)
    total = era_counts.sum()

    fig, ax = plt.subplots(figsize=(8.0, 4.8))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_aspect("auto")

    x_start = 0
    for era in ERAS:
        era_n = era_counts.loc[era]
        width = era_n / total if era_n > 0 else 0.0
        if width == 0:
            continue

        # Material breakdown in this era.
        sub = df[df["erected"] == era]
        mat_counts = sub["material"].value_counts().reindex(MATERIALS,
                                                             fill_value=0)

        y_start = 0
        for mat in MATERIALS:
            n_m = mat_counts.loc[mat]
            if n_m == 0:
                continue
            h = n_m / era_n
            patch = mpatches.Rectangle(
                (x_start, y_start), width, h,
                facecolor=MAT_COLORS[mat], alpha=0.85,
                edgecolor="white", linewidth=2,
            )
            ax.add_patch(patch)
            if width > 0.08 and h > 0.08:
                ax.text(x_start + width / 2, y_start + h / 2, str(int(n_m)),
                         ha="center", va="center",
                         color="white", fontsize=12, fontweight="bold")
            y_start += h
        ax.text(x_start + width / 2, -0.04, era,
                 ha="center", va="top", fontsize=12)
        x_start += width

    # Y-axis labels on the left (crafts column) and right (modern).
    for sp in ("top", "right", "left", "bottom"):
        ax.spines[sp].set_visible(False)
    ax.set_xticks([])
    ax.set_yticks([])

    # Legend with material colours.
    handles = [mpatches.Patch(color=MAT_COLORS[m], label=m) for m in MATERIALS]
    ax.legend(handles=handles, loc="upper left",
              bbox_to_anchor=(1.02, 1.0), frameon=False,
              title="material")

    fig.tight_layout()
    save(fig, "nested_proportions", "bridges_mosaic")


if __name__ == "__main__":
    render()
