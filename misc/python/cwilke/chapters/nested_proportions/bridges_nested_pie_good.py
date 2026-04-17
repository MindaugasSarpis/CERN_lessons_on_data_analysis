"""Nested-colour pie: material × era combinations (Wilke fig 11.6).

One slice per (material, era) combination — no double counting. Hue
encodes material, darkness encodes era. More legible than two
independent rings but still wastes space compared to the treemap.
"""

from __future__ import annotations

import matplotlib.colors as mcolors
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import numpy as np

from cwilke import data as D
from cwilke.theme import apply_base, save


MAT_COLORS = {
    "iron":  "#D55E00",
    "steel": "#0072B2",
    "wood":  "#009E73",
}
ERAS = ["crafts", "emerging", "mature", "modern"]


def _tint(hex_color: str, factor: float) -> str:
    rgb = mcolors.to_rgb(hex_color)
    white = (1.0, 1.0, 1.0)
    mixed = tuple(rgb[i] * (1 - factor) + white[i] * factor for i in range(3))
    return mcolors.to_hex(mixed)


def render() -> None:
    apply_base()
    df = D.bridges()

    # Build (material, era) counts in a fixed order.
    material_order = ["wood", "iron", "steel"]
    combos = []
    for mat in material_order:
        for era in ERAS:
            n = int(((df["material"] == mat) & (df["erected"] == era)).sum())
            if n > 0:
                combos.append((mat, era, n))

    total = sum(n for _, _, n in combos)
    fig, ax = plt.subplots(figsize=(6.8, 5.8))
    ax.set_xlim(-1.6, 1.6)
    ax.set_ylim(-1.3, 1.3)
    ax.set_aspect("equal")
    ax.axis("off")

    start = 90
    for mat, era, n in combos:
        sweep = 360 * n / total
        factor = 0.75 - 0.25 * ERAS.index(era)
        color = _tint(MAT_COLORS[mat], max(factor, 0.0))
        w = mpatches.Wedge((0, 0), 1.0, start - sweep, start,
                            facecolor=color, edgecolor="white",
                            linewidth=1.5)
        ax.add_patch(w)
        mid = np.deg2rad(start - sweep / 2)
        # Count inside.
        ax.text(0.6 * np.cos(mid), 0.6 * np.sin(mid), str(n),
                 ha="center", va="center",
                 color="white" if factor < 0.25 else "black",
                 fontsize=10, fontweight="bold")
        # Outside label.
        r_label = 1.1
        ax.text(r_label * np.cos(mid), r_label * np.sin(mid),
                 f"{era} ({mat})",
                 ha="center", va="center", fontsize=9)
        start -= sweep

    fig.tight_layout()
    save(fig, "nested_proportions", "bridges_nested_pie_good")


if __name__ == "__main__":
    render()
