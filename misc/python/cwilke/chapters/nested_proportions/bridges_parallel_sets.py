"""Parallel sets plot of bridges across four categorical variables
(Wilke fig 11.8).

Each vertical axis is a categorical variable; bands connect categories
across axes with width proportional to the number of bridges that share
those category values. Bands are coloured by material.
"""

from __future__ import annotations

from collections import defaultdict

import matplotlib.patches as mpatches
import matplotlib.path as mpath
import matplotlib.pyplot as plt
import numpy as np

from cwilke import data as D
from cwilke.theme import apply_base, save


MAT_COLORS = {
    "iron":  "#D55E00",
    "steel": "#0072B2",
    "wood":  "#009E73",
}

# Column order.
AXES = ["material", "length", "erected", "river"]
CAT_ORDER = {
    "material": ["wood", "iron", "steel"],
    "length":   ["short", "medium", "long"],
    "erected":  ["crafts", "emerging", "mature", "modern"],
    "river":    ["Allegheny", "Monongahela", "Ohio"],
}


def _axis_positions(df, axis_index, axis_name):
    """For a column, return a dict {category: (y_start, y_end)} normalised to [0,1]."""
    cats = CAT_ORDER[axis_name]
    counts = {c: int((df[axis_name] == c).sum()) for c in cats}
    total = sum(counts.values())
    positions = {}
    y = 1.0
    gap = 0.01
    for c in cats:
        n = counts[c]
        if n == 0:
            positions[c] = (y, y)
            continue
        height = (n / total) * (1.0 - gap * (len(cats) - 1))
        positions[c] = (y - height, y)
        y -= height + gap
    return positions


def _ribbon(ax, x0, y0_top, y0_bot, x1, y1_top, y1_bot, color, alpha=0.45):
    """A smooth bezier ribbon from one vertical slot to another."""
    Path = mpath.Path
    mid = (x0 + x1) / 2
    verts = [
        (x0, y0_top),
        (mid, y0_top), (mid, y1_top), (x1, y1_top),
        (x1, y1_bot),
        (mid, y1_bot), (mid, y0_bot), (x0, y0_bot),
        (x0, y0_top),
    ]
    codes = [Path.MOVETO,
             Path.CURVE4, Path.CURVE4, Path.CURVE4,
             Path.LINETO,
             Path.CURVE4, Path.CURVE4, Path.CURVE4,
             Path.CLOSEPOLY]
    patch = mpatches.PathPatch(Path(verts, codes),
                                facecolor=color, edgecolor="none",
                                alpha=alpha)
    ax.add_patch(patch)


def render() -> None:
    apply_base()
    df = D.bridges()

    # Axis positions.
    axis_positions = [(_axis_positions(df, i, name), name)
                       for i, name in enumerate(AXES)]

    fig, ax = plt.subplots(figsize=(9.4, 5.4))
    ax.set_xlim(-0.1, len(AXES) - 0.9)
    ax.set_ylim(-0.05, 1.08)
    ax.axis("off")

    # Draw the ribbons between adjacent axes, grouped by material.
    # We iterate pairs of axes and slot the ribbon proportionally based on
    # running consumption of each (src_cat, dst_cat) intersection.
    for a_i in range(len(AXES) - 1):
        col_src = AXES[a_i]
        col_dst = AXES[a_i + 1]
        x0 = a_i + 0.05
        x1 = a_i + 1 - 0.05

        pos_src, _ = axis_positions[a_i]
        pos_dst, _ = axis_positions[a_i + 1]

        # Track running offsets consumed in each slot.
        used_src = defaultdict(float)
        used_dst = defaultdict(float)

        # Iterate rows, grouped by (src, dst) and by material (for colour).
        # Include 'material' only as an *extra* group key (distinct from cols).
        group_keys = [col_src, col_dst]
        if "material" not in (col_src, col_dst):
            group_keys = [col_src, col_dst, "material"]
        counts = df.groupby(group_keys).size().reset_index(name="n")
        if "material" not in counts.columns:
            # Pick the dominant material from each (src, dst) cell.
            counts["material"] = counts[col_src] if col_src == "material" else counts[col_dst]
        # Sort rows so ribbons stack in a consistent order per slot.
        counts = counts.sort_values(["material", col_src, col_dst])

        total = len(df)
        for _, row in counts.iterrows():
            s_cat = row[col_src]
            d_cat = row[col_dst]
            mat = row["material"]
            n = int(row["n"])
            if n == 0:
                continue
            h = n / total

            s_lo, s_hi = pos_src[s_cat]
            d_lo, d_hi = pos_dst[d_cat]

            # Slot heights = total data mass in that slot.
            s_mass = sum(counts.loc[counts[col_src] == s_cat, "n"]) / total
            d_mass = sum(counts.loc[counts[col_dst] == d_cat, "n"]) / total
            s_slot_h = s_hi - s_lo if s_mass > 0 else 0
            d_slot_h = d_hi - d_lo if d_mass > 0 else 0

            # Proportional offsets.
            s_top = s_hi - used_src[s_cat]
            s_bot = s_top - s_slot_h * (n / (s_mass * total))
            d_top = d_hi - used_dst[d_cat]
            d_bot = d_top - d_slot_h * (n / (d_mass * total))

            used_src[s_cat] += s_slot_h * (n / (s_mass * total))
            used_dst[d_cat] += d_slot_h * (n / (d_mass * total))

            _ribbon(ax, x0, s_top, s_bot, x1, d_top, d_bot,
                     color=MAT_COLORS[mat])

    # Draw the axis "bars" and labels.
    for i, ((positions, _), name) in enumerate(zip(axis_positions, AXES)):
        x = i
        ax.plot([x, x], [0, 1], color="#2c3e50", linewidth=1.0)
        for cat, (lo, hi) in positions.items():
            if hi - lo <= 0.001:
                continue
            rect = mpatches.Rectangle((x - 0.02, lo), 0.04, hi - lo,
                                        facecolor="#b0bec5",
                                        edgecolor="#2c3e50",
                                        linewidth=0.8)
            ax.add_patch(rect)
            ax.text(x, (lo + hi) / 2, cat,
                     ha="center", va="center", fontsize=9,
                     rotation=90)
        ax.text(x, 1.04, name, ha="center", va="bottom",
                 fontweight="bold", fontsize=11)

    fig.tight_layout()
    save(fig, "nested_proportions", "bridges_parallel_sets")


if __name__ == "__main__":
    render()
