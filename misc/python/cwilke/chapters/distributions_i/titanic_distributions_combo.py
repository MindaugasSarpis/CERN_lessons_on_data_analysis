"""Three views of the same distribution: histogram, density, ECDF."""

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

    fig, axes = plt.subplots(1, 3, figsize=(11.4, 3.8))

    # --- histogram ---
    bins = np.arange(0, age.max() + 3, 3)
    axes[0].hist(age, bins=bins, color=PRIMARY_BLUE,
                 alpha=0.9, edgecolor="white", linewidth=0.6)
    axes[0].set_title("histogram")
    axes[0].set_xlabel("age (years)")
    axes[0].set_ylabel("count")
    hgrid(axes[0])

    # --- density ---
    xs = np.linspace(0, age.max(), 400)
    kde = gaussian_kde(age)
    axes[1].fill_between(xs, kde(xs), color=PRIMARY_BLUE, alpha=0.35)
    axes[1].plot(xs, kde(xs), color=BAD, linewidth=2.0)
    axes[1].set_title("density")
    axes[1].set_xlabel("age (years)")
    axes[1].set_ylabel("density")
    hgrid(axes[1])

    # --- ecdf ---
    age_sorted = np.sort(age)
    ecdf = np.arange(1, age_sorted.size + 1) / age_sorted.size
    axes[2].step(age_sorted, ecdf, where="post",
                 color=PRIMARY_BLUE, linewidth=1.8)
    axes[2].set_title("ECDF")
    axes[2].set_xlabel("age (years)")
    axes[2].set_ylabel("cumulative frequency")
    axes[2].set_ylim(0, 1.02)
    hgrid(axes[2])

    fig.tight_layout()
    save(fig, "distributions_i", "titanic_distributions_combo")


if __name__ == "__main__":
    render()
