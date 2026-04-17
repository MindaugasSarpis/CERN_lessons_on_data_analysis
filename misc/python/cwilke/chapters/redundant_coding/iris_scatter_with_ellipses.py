"""Direct-labelled iris scatter with 95% confidence ellipses (Wilke fig 20.9)."""

from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Ellipse

from cwilke import data as D
from cwilke.theme import apply_base, open_axes, save


SPECIES_STYLE = {
    "setosa":     ("#56B4E9", "o", (5.0, 4.25), 0, 0),
    "virginica":  ("#E69F00", "s", (7.0, 3.76), 0.5, 0.5),
    "versicolor": ("#009E73", "D", (5.1, 2.08), 0, 1),
}


def _confidence_ellipse(x, y, ax, edgecolor, n_std=2.0, **kwargs):
    cov = np.cov(x, y)
    vals, vecs = np.linalg.eigh(cov)
    order = np.argsort(vals)[::-1]
    vals, vecs = vals[order], vecs[:, order]
    angle = np.degrees(np.arctan2(*vecs[:, 0][::-1]))
    width, height = 2 * n_std * np.sqrt(vals)
    ell = Ellipse((np.mean(x), np.mean(y)),
                  width=width, height=height, angle=angle,
                  facecolor="none", edgecolor=edgecolor,
                  linewidth=1.2, **kwargs)
    ax.add_patch(ell)


def render() -> None:
    apply_base()

    df = D.iris()
    rng = np.random.default_rng(3942)
    jitter_x = rng.uniform(-0.04, 0.04, len(df))
    jitter_y = rng.uniform(-0.03, 0.03, len(df))

    fig, ax = plt.subplots(figsize=(6.4, 5.0))
    for sp, (col, marker, label_pos, hjust, vjust) in SPECIES_STYLE.items():
        sub = df[df["species"] == sp]
        ii = sub.index
        xs = sub["sepal_length"].values + jitter_x[ii]
        ys = sub["sepal_width"].values + jitter_y[ii]
        ax.scatter(xs, ys, s=44, marker=marker,
                   facecolor=col + "CC",
                   edgecolor="#2c3e50", linewidth=0.5)
        _confidence_ellipse(xs, ys, ax, edgecolor=col)

        ha = ("left", "center", "right")[int(round(hjust * 2))]
        va = ("bottom", "center", "top")[int(round(vjust * 2))]
        ax.text(label_pos[0], label_pos[1], f"Iris {sp}",
                color=col, fontstyle="italic", fontsize=12,
                fontweight="bold",
                ha=ha, va=va)

    ax.set_xlabel("sepal length")
    ax.set_ylabel("sepal width")
    ax.set_xlim(3.95, 8.2)
    ax.set_ylim(1.9, 4.6)
    open_axes(ax)

    fig.tight_layout()
    save(fig, "redundant_coding", "iris_scatter_with_ellipses")


if __name__ == "__main__":
    render()
