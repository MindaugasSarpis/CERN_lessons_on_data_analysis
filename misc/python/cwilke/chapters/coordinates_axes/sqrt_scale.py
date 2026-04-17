"""Linear, sqrt-transformed, and sqrt-scale comparison (Wilke fig 3.7).

Three strips showing the same eight points (0, 1, 4, 9, 16, 25, 36, 49)
on: (1) a linear scale, (2) a linear scale after sqrt-transforming, (3)
a square-root scale with the original data labelled.
"""

from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np

from cwilke.theme import PRIMARY_BLUE, apply_base, save


def _strip(ax, xs, *, title, xlabel, xticks, xlim,
           tick_labels=None, transform=None):
    if transform is not None:
        xs = transform(xs)
    ax.scatter(xs, np.ones_like(xs), color=PRIMARY_BLUE, s=55,
               edgecolor="white", linewidth=0.8, zorder=5)
    ax.set_xticks(xticks)
    if tick_labels is not None:
        ax.set_xticklabels([str(t) for t in tick_labels])
    ax.set_xlim(*xlim)
    ax.set_ylim(0.8, 1.2)
    ax.set_yticks([])
    ax.set_xlabel(xlabel)
    ax.set_title(title, fontsize=11, pad=4, fontweight="normal")
    for sp in ("top", "right", "left"):
        ax.spines[sp].set_visible(False)
    ax.grid(True, axis="x", color="#b0bec5", linewidth=0.6, alpha=0.7)


def render() -> None:
    apply_base()
    xs = np.array([0, 1, 4, 9, 16, 25, 36, 49])

    fig, axes = plt.subplots(3, 1, figsize=(7.5, 4.0))

    _strip(axes[0], xs,
           title="original data, linear scale",
           xlabel="x",
           xticks=[0, 10, 20, 30, 40, 50],
           xlim=(-2, 52))

    _strip(axes[1], xs, transform=np.sqrt,
           title="square-root-transformed data, linear scale",
           xlabel=r"$\sqrt{x}$",
           xticks=[0, 1, 2, 3, 4, 5, 6, 7],
           xlim=(-0.2, 7.2))

    # For the sqrt-scale strip: positions are sqrt(x), tick labels are x
    breaks_data = [0, 1, 5, 10, 20, 30, 40, 50]
    breaks_pos = [np.sqrt(b) for b in breaks_data]
    _strip(axes[2], xs, transform=np.sqrt,
           title="original data, square-root scale",
           xlabel="x",
           xticks=breaks_pos, tick_labels=breaks_data,
           xlim=(-0.2, 7.2))

    fig.tight_layout()
    save(fig, "coordinates_axes", "sqrt_scale")


if __name__ == "__main__":
    render()
