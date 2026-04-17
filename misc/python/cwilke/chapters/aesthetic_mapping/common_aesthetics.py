"""The six common aesthetics: position, shape, size, colour, line width,
line type (Wilke fig 2.1).

A 2×3 grid illustrating what "aesthetics" means in a visualization —
each panel labels one aesthetic and shows a minimal demonstration.
"""

from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np

from cwilke.theme import OKABE_ITO, apply_base, save


def render() -> None:
    apply_base()
    fig, axes = plt.subplots(2, 3, figsize=(8.0, 4.2))

    # -- position --
    ax = axes[0, 0]
    ax.annotate("", xy=(1.05, 0.5), xytext=(0, 0.5),
                arrowprops=dict(arrowstyle="->", color="#2c3e50",
                                lw=1.6, mutation_scale=18))
    ax.annotate("", xy=(0.5, 1.05), xytext=(0.5, 0),
                arrowprops=dict(arrowstyle="->", color="#2c3e50",
                                lw=1.6, mutation_scale=18))
    ax.text(0.45, 1.07, "y", fontsize=11, ha="right", va="bottom")
    ax.text(1.07, 0.47, "x", fontsize=11, ha="left", va="top")
    ax.set_xlim(-0.1, 1.15)
    ax.set_ylim(-0.1, 1.15)
    ax.set_title("position", fontsize=11, loc="left",
                 color="#455a64", fontweight="bold")

    # -- shape --
    ax = axes[0, 1]
    shapes = ["o", "s", "D", "^"]
    for i, mk in enumerate(shapes):
        ax.scatter(i + 1, 0, s=180, marker=mk, facecolor="#cfd8dc",
                   edgecolor="#2c3e50", linewidth=1.4)
    ax.set_xlim(0.4, 4.6)
    ax.set_ylim(-0.6, 0.6)
    ax.set_title("shape", fontsize=11, loc="left",
                 color="#455a64", fontweight="bold")

    # -- size --
    ax = axes[0, 2]
    sizes = [40, 120, 240, 400]
    for i, s in enumerate(sizes):
        ax.scatter(i + 1, 0, s=s, marker="o", facecolor="#cfd8dc",
                   edgecolor="#2c3e50", linewidth=1.0)
    ax.set_xlim(0.4, 4.6)
    ax.set_ylim(-0.6, 0.6)
    ax.set_title("size", fontsize=11, loc="left",
                 color="#455a64", fontweight="bold")

    # -- colour --
    ax = axes[1, 0]
    for i, c in enumerate(OKABE_ITO[1:5]):
        ax.add_patch(plt.Rectangle((i + 0.7, 0.2), 0.6, 0.6,
                                   color=c))
    ax.set_xlim(0.4, 4.6)
    ax.set_ylim(0, 1)
    ax.set_title("colour", fontsize=11, loc="left",
                 color="#455a64", fontweight="bold")

    # -- line width --
    ax = axes[1, 1]
    widths = [1, 2, 3, 5]
    for i, lw in enumerate(widths):
        y = 0.2 + i * 0.22
        ax.plot([0.1, 0.9], [y, y], color="#2c3e50", linewidth=lw)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1.1)
    ax.set_title("line width", fontsize=11, loc="left",
                 color="#455a64", fontweight="bold")

    # -- line type --
    ax = axes[1, 2]
    dashes = [(None, None), (3, 2), (1, 2), (5, 2, 1, 2)]
    ls = ["-", "--", ":", "-."]
    for i, style in enumerate(ls):
        y = 0.2 + i * 0.22
        ax.plot([0.1, 0.9], [y, y], color="#2c3e50",
                linewidth=1.8, linestyle=style)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1.1)
    ax.set_title("line type", fontsize=11, loc="left",
                 color="#455a64", fontweight="bold")

    # Strip axes of ticks / spines for everyone
    for ax in axes.ravel():
        ax.set_xticks([])
        ax.set_yticks([])
        for sp in ("top", "right", "bottom", "left"):
            ax.spines[sp].set_visible(False)

    fig.tight_layout()
    save(fig, "aesthetic_mapping", "common_aesthetics")


if __name__ == "__main__":
    render()
