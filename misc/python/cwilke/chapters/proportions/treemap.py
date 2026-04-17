"""Treemap of a 2-level hierarchy (Wilke fig 11.4, simplified).

Top-level categories partition the full rectangle by value; each
sub-category then partitions its parent. Treemaps are good at showing
part-of-whole for hierarchies where a pie chart would collapse under
its own complexity.
"""

from __future__ import annotations

import matplotlib.patches as mpatches
import matplotlib.pyplot as plt

from cwilke.theme import OKABE_ITO, apply_base, save


def _partition(rect, values, vertical):
    """Slice a rectangle into len(values) sub-rectangles proportional to values.

    rect: (x, y, w, h). vertical=True stacks top-to-bottom; False side-by-side.
    """
    x, y, w, h = rect
    total = sum(values)
    children = []
    if vertical:
        cy = y + h
        for v in values:
            frac = v / total
            ch = h * frac
            cy -= ch
            children.append((x, cy, w, ch))
    else:
        cx = x
        for v in values:
            frac = v / total
            cw = w * frac
            children.append((cx, y, cw, h))
            cx += cw
    return children


def render() -> None:
    apply_base()

    # Simple 3 top-level categories, each with sub-categories.
    hierarchy = [
        ("Grades", [("A",  22), ("B",  18), ("C",  8)]),
        ("Popular", [("Sports", 16), ("Looks", 14)]),
        ("Sports",  [("Team", 12), ("Individual", 10)]),
    ]

    top_values = [sum(v for _, v in subs) for _, subs in hierarchy]

    fig, ax = plt.subplots(figsize=(7.4, 5.0))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_aspect("equal")
    ax.axis("off")

    top_rects = _partition((0, 0, 1, 1), top_values, vertical=False)

    for i, (rect, (name, subs)) in enumerate(zip(top_rects, hierarchy)):
        top_color = OKABE_ITO[i + 1]
        sub_values = [v for _, v in subs]

        sub_rects = _partition(rect, sub_values, vertical=True)
        for j, (srect, (sname, _sv)) in enumerate(zip(sub_rects, subs)):
            sx, sy, sw, sh = srect
            shade = 0.85 - 0.12 * j  # tint variation per sub-rect
            patch = mpatches.Rectangle((sx, sy), sw, sh,
                                        facecolor=top_color, alpha=shade,
                                        edgecolor="white", linewidth=2)
            ax.add_patch(patch)
            if sw > 0.07 and sh > 0.07:
                ax.text(sx + sw / 2, sy + sh / 2, sname,
                        ha="center", va="center",
                        color="white", fontsize=11, fontweight="bold")

        # Group label at top of each top-level block
        x, y, w, h = rect
        ax.text(x + w / 2, y + h + 0.015, name,
                ha="center", va="bottom",
                color="#2c3e50", fontsize=12, fontweight="bold")

    ax.set_title("Treemap · hierarchical part-of-whole", pad=24)
    fig.tight_layout()
    save(fig, "proportions", "treemap")


if __name__ == "__main__":
    render()
