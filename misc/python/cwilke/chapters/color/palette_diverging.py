"""Diverging colormap swatch — edge-to-edge, minimal inline marker at zero."""

from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np

from cwilke.theme import apply_base, save


def render() -> None:
    apply_base()

    gradient = np.linspace(-1, 1, 512).reshape(1, -1)

    fig, ax = plt.subplots(figsize=(12, 1.4))
    ax.imshow(gradient, aspect="auto", cmap="RdBu_r",
              extent=(-1, 1, 0, 1))
    ax.set_xticks([])
    ax.set_yticks([])
    for spine in ax.spines.values():
        spine.set_visible(False)

    # Thin vertical at the midpoint with a tight in-swatch "0" label.
    ax.axvline(0, color="#2c3e50", linewidth=1.4)
    ax.text(0, 0.5, "0", ha="center", va="center",
            fontsize=11, fontweight="bold", color="#2c3e50",
            bbox=dict(facecolor="white", edgecolor="none",
                      pad=1.5, alpha=0.85))
    ax.text(-0.985, 0.5, "−", ha="left", va="center",
            fontsize=14, color="white", fontweight="bold")
    ax.text(0.985, 0.5, "+", ha="right", va="center",
            fontsize=14, color="white", fontweight="bold")

    fig.subplots_adjust(left=0, right=1, top=1, bottom=0)
    save(fig, "color", "palette_diverging")


if __name__ == "__main__":
    render()
