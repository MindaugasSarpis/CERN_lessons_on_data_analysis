"""Directly labelled density curves for iris sepal length (Wilke fig 20.10)."""

from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import gaussian_kde

from cwilke import data as D
from cwilke.theme import apply_base, hgrid, save


STYLE = {
    "virginica":  ("#56B4E9", (6.4,  0.55)),
    "versicolor": ("#E69F00", (6.2,  0.78)),
    "setosa":     ("#009E73", (4.65, 1.12)),
}


def render() -> None:
    apply_base()

    df = D.iris()

    fig, ax = plt.subplots(figsize=(7.2, 4.4))
    grid_x = np.linspace(3.8, 8.3, 400)
    for sp, (col, label_pos) in STYLE.items():
        vals = df.loc[df["species"] == sp, "sepal_length"].values
        kde = gaussian_kde(vals, bw_method=0.5)
        dens = kde(grid_x)
        ax.fill_between(grid_x, dens, color=col, alpha=0.28)
        ax.plot(grid_x, dens, color=col, linewidth=1.6)
        ax.text(label_pos[0], label_pos[1], f"Iris {sp}",
                color=col, fontstyle="italic", fontsize=12,
                fontweight="bold")

    ax.set_xlim(3.8, 8.3)
    ax.set_ylim(0, 1.5)
    ax.set_xlabel("sepal length")
    ax.set_ylabel("density")
    hgrid(ax)

    fig.tight_layout()
    save(fig, "redundant_coding", "iris_densities_direct_label")


if __name__ == "__main__":
    render()
