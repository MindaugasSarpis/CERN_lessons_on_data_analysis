"""Iris scatter: redundant coding of species via colour + shape (Wilke fig 2.1)."""

from __future__ import annotations

import matplotlib.pyplot as plt

from cwilke import data as D
from cwilke.theme import OKABE_ITO, apply_base, open_axes, save


def render() -> None:
    apply_base()
    df = D.iris()

    species_order = ["setosa", "versicolor", "virginica"]
    colors = {"setosa": OKABE_ITO[5],      # blue
              "versicolor": OKABE_ITO[1],  # orange
              "virginica": OKABE_ITO[3]}   # green
    markers = {"setosa": "o", "versicolor": "s", "virginica": "D"}

    fig, ax = plt.subplots(figsize=(6.4, 4.8))
    for sp in species_order:
        sub = df[df["species"] == sp]
        ax.scatter(sub["sepal_length"], sub["sepal_width"],
                   color=colors[sp], marker=markers[sp],
                   s=48, alpha=0.85, edgecolor="white", linewidth=0.6,
                   label=sp)

    ax.set_xlabel("sepal length (cm)")
    ax.set_ylabel("sepal width (cm)")
    open_axes(ax)
    ax.legend(title="species", loc="upper right", frameon=False)
    save(fig, "aesthetic_mapping", "iris_aesthetics")


if __name__ == "__main__":
    render()
