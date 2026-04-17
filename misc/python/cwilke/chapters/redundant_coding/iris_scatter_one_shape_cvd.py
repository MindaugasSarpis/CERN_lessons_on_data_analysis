"""CVD simulation of iris colour-only scatter (Wilke fig 20.2)."""

from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np

from cwilke import data as D
from cwilke._cvd import simulate
from cwilke.theme import apply_base, grid, save


BASE = {
    "setosa":     "#E69F00",
    "virginica":  "#56B4E9",
    "versicolor": "#009E73",
}

PANELS = [
    ("original",                 "original"),
    ("deuteranopia simulation",  "deuteranopia"),
    ("tritanopia simulation",    "tritanopia"),
    ("desaturated",              "desaturated"),
]


def render() -> None:
    apply_base()

    df = D.iris()
    rng = np.random.default_rng(3942)
    jitter_x = rng.uniform(-0.04, 0.04, len(df))
    jitter_y = rng.uniform(-0.03, 0.03, len(df))

    fig, axes = plt.subplots(2, 2, figsize=(10.5, 7.0))
    for ax, (title, kind) in zip(axes.flatten(), PANELS):
        palette = {sp: simulate(h, kind) for sp, h in BASE.items()}
        for sp, col in palette.items():
            sub = df[df["species"] == sp]
            ii = sub.index
            ax.scatter(sub["sepal_length"] + jitter_x[ii],
                       sub["sepal_width"] + jitter_y[ii],
                       s=32, marker="o",
                       facecolor=col, alpha=0.85,
                       edgecolor="#2c3e50", linewidth=0.3,
                       label=f"Iris {sp}")
        ax.set_xlim(3.95, 8.2)
        ax.set_ylim(1.9, 4.6)
        ax.set_xlabel("sepal length")
        ax.set_ylabel("sepal width")
        ax.set_title(title, fontsize=11, fontweight="bold",
                     color="#2c3e50", loc="left", pad=4)
        grid(ax)

    fig.tight_layout()
    save(fig, "redundant_coding", "iris_scatter_one_shape_cvd")


if __name__ == "__main__":
    render()
