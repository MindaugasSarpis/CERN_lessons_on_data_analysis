"""Iris sepal-length densities as dashed line drawings — porous (Wilke fig 22.3)."""

from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import gaussian_kde

from cwilke import data as D
from cwilke.theme import apply_base, open_axes, save, stamp_ugly


def render() -> None:
    apply_base()
    df = D.iris()
    species_order = ["setosa", "versicolor", "virginica"]
    linestyles = {"setosa": (0, (4, 2, 1, 2)),     # dash-dot-dot
                  "versicolor": (0, (1, 2)),        # dotted
                  "virginica": "-"}

    xs = np.linspace(3.5, 8.5, 300)
    fig, ax = plt.subplots(figsize=(7.0, 4.2))
    for sp in species_order:
        vals = df[df["species"] == sp]["sepal_length"].values
        kde = gaussian_kde(vals)
        ys = kde(xs)
        ax.plot(xs, ys, color="#2c3e50", linewidth=1.2,
                linestyle=linestyles[sp])
        # Label near peak
        peak = xs[np.argmax(ys)]
        ax.text(peak, ys.max() + 0.05, f"Iris {sp}",
                ha="center", fontsize=10, fontstyle="italic",
                color="#2c3e50")

    ax.set_xlim(3.5, 8.5)
    ax.set_ylim(0, 1.6)
    ax.set_xlabel("sepal length")
    ax.set_ylabel("density")
    open_axes(ax)

    stamp_ugly(fig)
    fig.tight_layout()
    save(fig, "avoid_line_drawings", "iris_densities_lines")


if __name__ == "__main__":
    render()
