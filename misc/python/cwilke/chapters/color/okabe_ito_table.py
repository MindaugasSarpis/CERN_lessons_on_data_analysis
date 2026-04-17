"""Okabe-Ito palette with hex codes (Wilke ch. 19, palette-Okabe-Ito)."""

from __future__ import annotations

import matplotlib.patches as patches
import matplotlib.pyplot as plt

from cwilke.theme import apply_base, save


PALETTE = [
    ("#E69F00", "orange"),
    ("#56B4E9", "sky blue"),
    ("#009E73", "bluish green"),
    ("#F0E442", "yellow"),
    ("#0072B2", "blue"),
    ("#D55E00", "vermillion"),
    ("#CC79A7", "reddish purple"),
    ("#000000", "black"),
]


def render() -> None:
    apply_base()

    n = len(PALETTE)
    fig, ax = plt.subplots(figsize=(12, 2.0))
    for i, (hex_code, name) in enumerate(PALETTE):
        ax.add_patch(patches.Rectangle(
            (i, 0.35), 1, 0.65,
            facecolor=hex_code, edgecolor="none",
        ))
        text_colour = "#2c3e50" if name == "yellow" else "white"
        ax.text(i + 0.5, 0.68, name,
                ha="center", va="center", fontsize=10,
                color=text_colour, fontweight="bold")
        ax.text(i + 0.5, 0.17, hex_code,
                ha="center", va="center", fontsize=10,
                color="#2c3e50", family="monospace")

    ax.set_xlim(0, n)
    ax.set_ylim(0, 1)
    ax.set_xticks([])
    ax.set_yticks([])
    for spine in ax.spines.values():
        spine.set_visible(False)
    fig.subplots_adjust(left=0, right=1, top=1, bottom=0)
    save(fig, "color", "okabe_ito_table")


if __name__ == "__main__":
    render()
