"""Titanic age: KDE overlaid on a density-normalised histogram (Wilke fig 7.4)."""

from __future__ import annotations

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde

from cwilke import data as D
from cwilke.theme import BAD, PRIMARY_BLUE, apply_base, hgrid, save


def render() -> None:
    apply_base()
    df = D.titanic()
    age = df["age"].dropna().values

    bins = np.arange(0, age.max() + 2, 2)
    xs = np.linspace(0, age.max(), 400)
    kde = gaussian_kde(age)

    fig, ax = plt.subplots(figsize=(7.2, 4.4))
    ax.hist(age, bins=bins, density=True, color=PRIMARY_BLUE,
            alpha=0.75, edgecolor="white", linewidth=0.6,
            label="histogram")
    ax.plot(xs, kde(xs), color=BAD, linewidth=2.2, label="KDE")
    ax.set_xlabel("age (years)")
    ax.set_ylabel("density")
    hgrid(ax)
    ax.legend(loc="upper right", frameon=False)
    save(fig, "distributions_i", "titanic_density")


if __name__ == "__main__":
    render()
