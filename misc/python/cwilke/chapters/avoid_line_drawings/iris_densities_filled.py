"""Iris sepal-length densities as transparent filled regions (Wilke fig 22.5)."""

from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import gaussian_kde

from cwilke import data as D
from cwilke.theme import apply_base, open_axes, save


def render() -> None:
    apply_base()
    df = D.iris()
    species = ["setosa", "versicolor", "virginica"]
    colors = {"setosa": "#009E73",
              "versicolor": "#E69F00",
              "virginica": "#56B4E9"}

    xs = np.linspace(3.5, 8.5, 300)
    fig, ax = plt.subplots(figsize=(7.0, 4.2))
    for sp in species:
        vals = df[df["species"] == sp]["sepal_length"].values
        kde = gaussian_kde(vals)
        ys = kde(xs)
        ax.fill_between(xs, 0, ys, color=colors[sp], alpha=0.35,
                         linewidth=0)
        ax.plot(xs, ys, color=colors[sp], linewidth=1.3)
        peak = xs[np.argmax(ys)]
        ax.text(peak, ys.max() + 0.05, f"Iris {sp}",
                ha="center", fontsize=10, fontstyle="italic",
                color=colors[sp])

    ax.set_xlim(3.5, 8.5)
    ax.set_ylim(0, 1.6)
    ax.set_xlabel("sepal length")
    ax.set_ylabel("density")
    open_axes(ax)

    fig.tight_layout()
    save(fig, "avoid_line_drawings", "iris_densities_filled")


if __name__ == "__main__":
    render()
