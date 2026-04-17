"""Linear vs log scale illustrated with the five anchor points
1, 3.16, 10, 31.6, 100 (Wilke fig 3.4).

Four small strips: (1) linear scale of original numbers, (2) linear
scale of log-transformed numbers, (3) log scale of original numbers,
(4) log scale but with a *wrong* axis label — marked as "wrong".
"""

from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np

from cwilke.theme import PRIMARY_BLUE, apply_base, save, stamp_wrong


def _strip(ax, xs, *, scale, title, xlabel, xticks=None, xlim=None):
    ax.scatter(xs, np.ones_like(xs), color=PRIMARY_BLUE, s=55,
               edgecolor="white", linewidth=0.8, zorder=5)
    ax.set_xscale(scale)
    if xlim is not None:
        ax.set_xlim(*xlim)
    if xticks is not None:
        ax.set_xticks(xticks)
        ax.set_xticklabels([str(v) for v in xticks])
    ax.set_ylim(0.8, 1.2)
    ax.set_yticks([])
    ax.set_xlabel(xlabel)
    ax.set_title(title, fontsize=11, pad=4, fontweight="normal")
    for sp in ("top", "right", "left"):
        ax.spines[sp].set_visible(False)
    ax.grid(True, axis="x", color="#b0bec5", linewidth=0.6, alpha=0.7)


def render() -> None:
    apply_base()
    xs = np.array([1, 3.16, 10, 31.6, 100])

    fig, axes = plt.subplots(4, 1, figsize=(7.5, 5.2))

    _strip(axes[0], xs, scale="linear",
           title="original data, linear scale",
           xlabel="x",
           xticks=[0, 25, 50, 75, 100],
           xlim=(0, 105))
    _strip(axes[1], np.log10(xs), scale="linear",
           title="log-transformed data, linear scale",
           xlabel=r"$\log_{10}(x)$",
           xticks=[0, 0.5, 1, 1.5, 2],
           xlim=(-0.05, 2.1))
    _strip(axes[2], xs, scale="log",
           title="original data, logarithmic scale",
           xlabel="x",
           xticks=[1, 3.16, 10, 31.6, 100],
           xlim=(0.95, 110))
    _strip(axes[3], xs, scale="log",
           title="logarithmic scale with incorrect axis title",
           xlabel=r"$\log_{10}(x)$",
           xticks=[1, 3.16, 10, 31.6, 100],
           xlim=(0.95, 110))

    stamp_wrong(fig)

    fig.tight_layout()
    save(fig, "coordinates_axes", "linear_vs_log_scale")


if __name__ == "__main__":
    render()
