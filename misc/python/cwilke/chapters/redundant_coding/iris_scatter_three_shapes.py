"""Iris scatter with distinct colours AND shapes (Wilke fig 20.3)."""

from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np

from cwilke import data as D
from cwilke.theme import apply_base, grid, save


# Swap setosa & versicolor colours vs. the "bad" version, add shape map.
SPECIES_STYLE = {
    "setosa":     ("#56B4E9", "o"),   # sky blue circle
    "virginica":  ("#E69F00", "s"),   # orange square
    "versicolor": ("#009E73", "D"),   # green diamond
}


def render() -> None:
    apply_base()

    df = D.iris()
    rng = np.random.default_rng(3942)
    jitter_x = rng.uniform(-0.04, 0.04, len(df))
    jitter_y = rng.uniform(-0.03, 0.03, len(df))

    fig, ax = plt.subplots(figsize=(6.4, 4.4))
    for sp, (col, marker) in SPECIES_STYLE.items():
        sub = df[df["species"] == sp]
        ii = sub.index
        ax.scatter(sub["sepal_length"] + jitter_x[ii],
                   sub["sepal_width"] + jitter_y[ii],
                   s=46, marker=marker,
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
    save(fig, "redundant_coding", "iris_scatter_three_shapes")


if __name__ == "__main__":
    render()
