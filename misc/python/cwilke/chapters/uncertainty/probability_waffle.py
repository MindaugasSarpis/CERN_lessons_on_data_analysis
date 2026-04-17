"""Waffle grids: 1%, 10%, 40% success as random squares (Wilke fig 16.1)."""

from __future__ import annotations

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

from cwilke.theme import apply_base, save


def _waffle(ax, rng, p, title):
    n = 100
    n_success = int(round(p * n))
    idx = np.arange(n)
    rng.shuffle(idx)
    success_idx = set(idx[:n_success].tolist())
    dark, light = "#1b3a53", "#d5e4f2"
    for i in range(n):
        row = i // 10
        col = i % 10
        color = dark if i in success_idx else light
        rect = Rectangle((col, 9 - row), 0.92, 0.92,
                         facecolor=color, edgecolor="white", linewidth=0.8)
        ax.add_patch(rect)
    ax.set_xlim(-0.1, 10.1)
    ax.set_ylim(-0.1, 10.1)
    ax.set_aspect("equal")
    ax.set_xticks([])
    ax.set_yticks([])
    for s in ("top", "right", "left", "bottom"):
        ax.spines[s].set_visible(False)
    ax.set_title(title, fontsize=12)


def render() -> None:
    apply_base()
    rng = np.random.default_rng(84524)
    fig, axes = plt.subplots(1, 3, figsize=(8.4, 3.2))
    for ax, p, lab in zip(axes, [0.01, 0.10, 0.40],
                           ["1% chance", "10% chance", "40% chance"]):
        _waffle(ax, np.random.default_rng(int(p * 1000) + 1), p, lab)

    # Legend
    dark, light = "#1b3a53", "#d5e4f2"
    handles = [
        Rectangle((0, 0), 1, 1, facecolor=dark, edgecolor="white"),
        Rectangle((0, 0), 1, 1, facecolor=light, edgecolor="white"),
    ]
    fig.legend(handles, ["success", "failure"],
               loc="lower center", ncol=2, frameon=False,
               bbox_to_anchor=(0.5, -0.02))
    fig.tight_layout(rect=(0, 0.05, 1, 1))
    save(fig, "uncertainty", "probability_waffle")


if __name__ == "__main__":
    render()
