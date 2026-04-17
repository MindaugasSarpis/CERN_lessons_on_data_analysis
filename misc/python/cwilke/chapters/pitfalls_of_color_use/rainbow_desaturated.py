"""Rainbow scale and its non-monotonic greyscale (Wilke fig 19.4)."""

from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np

from cwilke.theme import apply_base, save


def _rainbow_luma(grad: np.ndarray) -> np.ndarray:
    """Convert hsv RGB gradient to perceived luma (Rec. 709)."""
    rgb = plt.get_cmap("hsv")(grad)[..., :3]
    luma = 0.2126 * rgb[..., 0] + 0.7152 * rgb[..., 1] + 0.0722 * rgb[..., 2]
    return np.stack([luma, luma, luma], axis=-1)


def render() -> None:
    apply_base()

    grad = np.linspace(0, 1, 512)

    fig, axes = plt.subplots(2, 1, figsize=(11, 2.6))

    axes[0].imshow(plt.get_cmap("hsv")(grad)[np.newaxis, ..., :3],
                   aspect="auto", extent=(0, 1, 0, 1))
    axes[0].set_title("rainbow scale", fontsize=12, fontweight="bold",
                      color="#2c3e50", loc="left", pad=4)

    axes[1].imshow(_rainbow_luma(grad)[np.newaxis, ...],
                   aspect="auto", extent=(0, 1, 0, 1))
    axes[1].set_title("rainbow converted to grayscale",
                      fontsize=12, fontweight="bold",
                      color="#2c3e50", loc="left", pad=4)

    for ax in axes:
        ax.set_xticks([])
        ax.set_yticks([])
        for spine in ax.spines.values():
            spine.set_visible(False)

    fig.subplots_adjust(left=0.01, right=0.99, top=0.88,
                        bottom=0.02, hspace=1.1)
    save(fig, "pitfalls_of_color_use", "rainbow_desaturated")


if __name__ == "__main__":
    render()
