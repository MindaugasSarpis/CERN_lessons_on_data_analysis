"""Treemap of bridges: material > era (Wilke fig 11.4).

Rectangular recursion: first partition the plane by material, then
within each material by era. Good at using whitespace; less good at
letting you compare counts across groups with different shapes.
"""

from __future__ import annotations

import matplotlib.colors as mcolors
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt

from cwilke import data as D
from cwilke.theme import apply_base, save


MAT_COLORS = {
    "iron":  "#D55E00",
    "steel": "#0072B2",
    "wood":  "#009E73",
}
ERAS = ["crafts", "emerging", "mature", "modern"]


def _tint(hex_color: str, factor: float) -> str:
    """Lighten a hex colour by blending toward white (factor in [0,1])."""
    rgb = mcolors.to_rgb(hex_color)
    white = (1.0, 1.0, 1.0)
    mixed = tuple(rgb[i] * (1 - factor) + white[i] * factor for i in range(3))
    return mcolors.to_hex(mixed)


def _partition(rect, values, vertical):
    x, y, w, h = rect
    total = sum(values)
    if total == 0:
        return []
    out = []
    if vertical:
        cy = y + h
        for v in values:
            frac = v / total
            ch = h * frac
            cy -= ch
            out.append((x, cy, w, ch))
    else:
        cx = x
        for v in values:
            frac = v / total
            cw = w * frac
            out.append((cx, y, cw, h))
            cx += cw
    return out


def render() -> None:
    apply_base()
    df = D.bridges()
    total = len(df)

    # Top-level: materials.
    mat_counts = df["material"].value_counts()
    mat_order = ["steel", "iron", "wood"]  # largest first visually
    top_values = [int(mat_counts.get(m, 0)) for m in mat_order]

    fig, ax = plt.subplots(figsize=(7.6, 5.4))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_aspect("equal")
    ax.axis("off")

    top_rects = _partition((0, 0, 1, 1), top_values, vertical=False)

    for mat, rect in zip(mat_order, top_rects):
        # Sub-partition: eras within this material.
        sub = df[df["material"] == mat]
        era_counts = [int((sub["erected"] == e).sum()) for e in ERAS]
        if sum(era_counts) == 0:
            continue

        era_rects = _partition(rect, era_counts, vertical=True)
        base_color = MAT_COLORS[mat]

        for era, sub_rect, count in zip(ERAS, era_rects, era_counts):
            if count == 0:
                continue
            sx, sy, sw, sh = sub_rect
            # Tint darker for later eras.
            factor = 0.75 - 0.25 * ERAS.index(era)
            color = _tint(base_color, max(factor, 0.0))
            patch = mpatches.Rectangle((sx, sy), sw, sh,
                                         facecolor=color, edgecolor="white",
                                         linewidth=2.0)
            ax.add_patch(patch)
            if sw > 0.06 and sh > 0.05:
                text_color = "white" if factor < 0.25 else "black"
                ax.text(sx + sw / 2, sy + sh / 2, f"{era}\n{count}",
                         ha="center", va="center",
                         color=text_color, fontsize=10, fontweight="bold")
        # Material label at the top of the group.
        x, y, w, h = rect
        ax.text(x + w / 2, y + h + 0.02, mat,
                ha="center", va="bottom",
                color=base_color, fontsize=13, fontweight="bold")

    fig.tight_layout()
    save(fig, "nested_proportions", "bridges_treemap")


if __name__ == "__main__":
    render()
