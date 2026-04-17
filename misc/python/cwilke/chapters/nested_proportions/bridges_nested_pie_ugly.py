"""Nested pie with disjoint inner/outer rings (Wilke fig 11.5, "ugly").

Inner ring = material, outer ring = era. Visually neat but the two
rings are independent partitions, so the figure double-counts every
bridge. Shown here as a cautionary example.
"""

from __future__ import annotations

import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import numpy as np

from cwilke import data as D
from cwilke.theme import apply_base, save, stamp_ugly


MAT_COLORS = {
    "iron":  "#D55E00",
    "steel": "#0072B2",
    "wood":  "#009E73",
}
ERA_COLORS = {
    "crafts":   "#F0E442",
    "emerging": "#E69F00",
    "mature":   "#CC79A7",
    "modern":   "#56B4E9",
}


def _wedges(ax, counts, colors, r_inner, r_outer):
    total = sum(counts.values())
    start = 90
    for label, n in counts.items():
        if n == 0:
            continue
        sweep = 360 * n / total
        w = mpatches.Wedge((0, 0), r_outer, start - sweep, start,
                            width=r_outer - r_inner,
                            facecolor=colors[label], edgecolor="white",
                            linewidth=1.5)
        ax.add_patch(w)
        mid = np.deg2rad(start - sweep / 2)
        r_mid = (r_inner + r_outer) / 2
        ax.text(r_mid * np.cos(mid), r_mid * np.sin(mid), str(int(n)),
                 ha="center", va="center", color="black", fontsize=10,
                 fontweight="bold")
        # Outside label
        r_label = r_outer + 0.08
        ax.text(r_label * np.cos(mid), r_label * np.sin(mid), label,
                 ha="center", va="center", fontsize=10)
        start -= sweep


def render() -> None:
    apply_base()
    df = D.bridges()

    mat_counts = dict(df["material"].value_counts())
    era_counts = dict(df["erected"].value_counts())

    fig, ax = plt.subplots(figsize=(6.6, 6.0))
    ax.set_xlim(-1.6, 1.6)
    ax.set_ylim(-1.35, 1.35)
    ax.set_aspect("equal")
    ax.axis("off")

    # Outer ring: era
    _wedges(ax, era_counts, ERA_COLORS, 0.72, 1.0)
    # Inner disc: material
    _wedges(ax, mat_counts, MAT_COLORS, 0.0, 0.7)

    stamp_ugly(fig)
    fig.tight_layout()
    save(fig, "nested_proportions", "bridges_nested_pie_ugly")


if __name__ == "__main__":
    render()
