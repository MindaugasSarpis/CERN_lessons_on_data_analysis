"""Sequential colormap swatches — edge-to-edge, label on the swatch itself."""

from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np

from cwilke.theme import apply_base, save


CMAPS = ["viridis", "cividis", "plasma"]


def render() -> None:
    apply_base()

    gradient = np.linspace(0, 1, 512).reshape(1, -1)

    fig, axes = plt.subplots(len(CMAPS), 1, figsize=(12, 1.9))
    for ax, cmap_name in zip(axes, CMAPS):
        ax.imshow(gradient, aspect="auto", cmap=cmap_name)
        ax.set_xticks([])
        ax.set_yticks([])
        for spine in ax.spines.values():
            spine.set_visible(False)
        # Inline label inside the swatch (left side), high contrast.
        ax.text(0.01, 0.5, cmap_name,
                transform=ax.transAxes,
                ha="left", va="center",
                fontsize=11, color="white",
                fontweight="bold",
                path_effects=[])

    fig.subplots_adjust(left=0, right=1, top=1, bottom=0, hspace=0.08)
    save(fig, "color", "palette_sequential")


if __name__ == "__main__":
    render()
