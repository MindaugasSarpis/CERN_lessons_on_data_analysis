"""Titanic age histograms at four different bin widths (Wilke fig 7.2)."""

from __future__ import annotations

import numpy as np
import matplotlib.pyplot as plt

from cwilke import data as D
from cwilke.theme import PRIMARY_BLUE, apply_base, hgrid, save


def render() -> None:
    apply_base()
    df = D.titanic()
    age = df["age"].dropna().values

    widths = [1, 3, 5, 15]
    fig, axes = plt.subplots(2, 2, figsize=(9.0, 6.0), sharex=True)
    for ax, w in zip(axes.ravel(), widths):
        bins = np.arange(0, age.max() + w, w)
        ax.hist(age, bins=bins, color=PRIMARY_BLUE,
                alpha=0.9, edgecolor="white", linewidth=0.6)
        ax.set_title(f"bin width = {w}")
        ax.set_xlabel("age (years)")
        ax.set_ylabel("count")
        hgrid(ax)

    fig.tight_layout()
    save(fig, "distributions_i", "titanic_hist_binwidth")


if __name__ == "__main__":
    render()
