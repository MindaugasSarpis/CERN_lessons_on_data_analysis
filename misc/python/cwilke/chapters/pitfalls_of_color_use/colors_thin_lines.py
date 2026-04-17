"""Colours distinguished less at thin/small sizes (Wilke fig 19.10)."""

from __future__ import annotations

import matplotlib.pyplot as plt

from cwilke._cvd import simulate
from cwilke.theme import OKABE_ITO, apply_base, save


# Four Okabe-Ito categorical colours
COLOURS = [OKABE_ITO[1], OKABE_ITO[4], OKABE_ITO[2], OKABE_ITO[3]]

PANELS = [
    ("original",               "original"),
    ("deuteranopia simulation", "deuteranopia"),
    ("protanopia simulation",   "protanopia"),
    ("tritanopia simulation",   "tritanopia"),
]


def _draw_panel(ax, palette) -> None:
    ax.set_xlim(0, 6)
    ax.set_ylim(0, 4)
    ax.set_xticks([])
    ax.set_yticks([])
    for spine in ax.spines.values():
        spine.set_visible(False)

    # Large tiles (top-left 2x2)
    for i, col in enumerate(palette):
        r, c = divmod(i, 2)
        ax.add_patch(plt.Rectangle(
            (0.2 + c * 1.1, 3.0 - r * 1.0), 1.0, 0.9,
            facecolor=col, edgecolor="none",
        ))

    # Thick horizontal lines (top-right 4 lines)
    for i, col in enumerate(palette):
        y = 3.8 - i * 0.22
        ax.plot([3.0, 5.8], [y, y], color=col, linewidth=4.2)

    # Thin horizontal lines (bottom-right)
    for i, col in enumerate(palette):
        y = 1.8 - i * 0.22
        ax.plot([3.0, 5.8], [y, y], color=col, linewidth=1.0)

    # Small dots (bottom-left)
    for i, col in enumerate(palette):
        for j, s in enumerate((60, 30, 12, 4)):
            ax.scatter(0.45 + j * 0.45, 1.8 - i * 0.28,
                       s=s, color=col, edgecolors="none")


def render() -> None:
    apply_base()

    fig, axes = plt.subplots(2, 2, figsize=(11.5, 5.4))
    for ax, (title, kind) in zip(axes.flatten(), PANELS):
        palette = [simulate(c, kind) for c in COLOURS]
        _draw_panel(ax, palette)
        ax.set_title(title, fontsize=11, fontweight="bold",
                     color="#2c3e50", loc="left", pad=4)

    fig.subplots_adjust(left=0.02, right=0.98, top=0.94,
                        bottom=0.02, hspace=0.25, wspace=0.05)
    save(fig, "pitfalls_of_color_use", "colors_thin_lines")


if __name__ == "__main__":
    render()
