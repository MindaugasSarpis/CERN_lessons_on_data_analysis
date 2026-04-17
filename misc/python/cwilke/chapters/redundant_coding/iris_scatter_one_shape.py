"""Iris scatter with colour-only encoding — bad (Wilke fig 20.1)."""

from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np

from cwilke import data as D
from cwilke.theme import apply_base, grid, save, stamp_bad


COLOURS = {
    "setosa":     "#E69F00",   # orange
    "virginica":  "#56B4E9",   # sky blue
    "versicolor": "#009E73",   # bluish green
}


def render() -> None:
    apply_base()

    df = D.iris()
    rng = np.random.default_rng(3942)
    jitter_x = rng.uniform(-0.04, 0.04, len(df))
    jitter_y = rng.uniform(-0.03, 0.03, len(df))

    fig, ax = plt.subplots(figsize=(6.4, 4.4))
    for sp, col in COLOURS.items():
        sub = df[df["species"] == sp]
        ii = sub.index
        ax.scatter(sub["sepal_length"] + jitter_x[ii],
                   sub["sepal_width"] + jitter_y[ii],
                   s=46, marker="o",
                   facecolor=col + "CC",
                   edgecolor="#2c3e50", linewidth=0.5,
                   label=f"Iris {sp}")

    ax.set_xlabel("sepal length")
    ax.set_ylabel("sepal width")
    ax.set_xlim(3.95, 8.2)
    ax.set_ylim(1.9, 4.6)
    ax.legend(loc="upper right", fontsize=10, frameon=False)
    grid(ax)

    fig.tight_layout()
    stamp_bad(fig)
    save(fig, "redundant_coding", "iris_scatter_one_shape")


if __name__ == "__main__":
    render()
