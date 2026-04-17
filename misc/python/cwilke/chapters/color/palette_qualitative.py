"""Okabe-Ito qualitative palette swatch — edge-to-edge bars, no title chrome."""

from __future__ import annotations

import matplotlib.patches as patches
import matplotlib.pyplot as plt

from cwilke.theme import OKABE_ITO, apply_base, save


NAMES = [
    "black", "orange", "sky blue", "bluish green",
    "yellow", "blue", "vermillion", "reddish purple",
]


def render() -> None:
    apply_base()

    n = len(OKABE_ITO)
    fig, ax = plt.subplots(figsize=(12, 1.4))
    for i, (colour, name) in enumerate(zip(OKABE_ITO, NAMES)):
        rect = patches.Rectangle(
            (i, 0), 1, 1, facecolor=colour, edgecolor="none",
        )
        ax.add_patch(rect)
        text_color = "#2c3e50" if name in ("yellow",) else "white"
        ax.text(i + 0.5, 0.5, name,
                ha="center", va="center",
                fontsize=11, color=text_color, fontweight="bold")

    ax.set_xlim(0, n)
    ax.set_ylim(0, 1)
    ax.set_xticks([])
    ax.set_yticks([])
    for spine in ax.spines.values():
        spine.set_visible(False)
    fig.subplots_adjust(left=0, right=1, top=1, bottom=0)
    save(fig, "color", "palette_qualitative")


if __name__ == "__main__":
    render()
