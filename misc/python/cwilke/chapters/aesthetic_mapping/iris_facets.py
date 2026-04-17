"""Iris small-multiples: one panel per species (sepal_length vs petal_length)."""

from __future__ import annotations

import matplotlib.pyplot as plt

from cwilke import data as D
from cwilke.theme import OKABE_ITO, apply_base, open_axes, save


def render() -> None:
    apply_base()
    df = D.iris()

    species_order = ["setosa", "versicolor", "virginica"]
    colors = {"setosa": OKABE_ITO[5],
              "versicolor": OKABE_ITO[1],
              "virginica": OKABE_ITO[3]}

    fig, axes = plt.subplots(1, 3, sharey=True, figsize=(9.6, 3.8))
    for ax, sp in zip(axes, species_order):
        sub = df[df["species"] == sp]
        ax.scatter(sub["sepal_length"], sub["petal_length"],
                   color=colors[sp], s=42, alpha=0.85,
                   edgecolor="white", linewidth=0.6)
        ax.set_title(sp)
        ax.set_xlabel("sepal length (cm)")
        open_axes(ax)

    axes[0].set_ylabel("petal length (cm)")
    fig.tight_layout()
    save(fig, "aesthetic_mapping", "iris_facets")


if __name__ == "__main__":
    render()
