"""3x3 pair plot (correlogram) of mtcars mpg/hp/wt (Wilke fig 21.4 concept).

Small multiples built as a grid where the diagonal shows each
variable's marginal distribution and the off-diagonals show pairwise
scatters. A compact way to scan a handful of continuous variables for
pairwise structure before reaching for a formal correlation test.
"""

from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import gaussian_kde

from cwilke import data as D
from cwilke.theme import PRIMARY_BLUE, apply_base, grid, open_axes, save


def render() -> None:
    apply_base()
    df = D.mtcars()[["mpg", "hp", "wt"]]
    cols = list(df.columns)
    n = len(cols)

    fig, axes = plt.subplots(n, n, figsize=(7.2, 7.2))

    for i, row in enumerate(cols):
        for j, col in enumerate(cols):
            ax = axes[i, j]
            if i == j:
                # KDE on the diagonal
                vals = df[col].values
                kde = gaussian_kde(vals)
                xs = np.linspace(vals.min(), vals.max(), 200)
                ax.fill_between(xs, 0, kde(xs), color=PRIMARY_BLUE,
                                alpha=0.55, linewidth=0)
                ax.plot(xs, kde(xs), color=PRIMARY_BLUE, linewidth=1.2)
                ax.set_yticks([])
                open_axes(ax)
            else:
                ax.scatter(df[col], df[row], s=20,
                           color=PRIMARY_BLUE, alpha=0.85,
                           edgecolor="white", linewidth=0.3)
                grid(ax)

            # Only outer axes get tick labels.
            if i < n - 1:
                ax.set_xticklabels([])
            if j > 0 and i != j:
                ax.set_yticklabels([])
            if i == n - 1:
                ax.set_xlabel(col)
            if j == 0 and i != j:
                ax.set_ylabel(row)

    fig.suptitle("Correlogram · mtcars (mpg, hp, wt)",
                 fontsize=12, y=0.995)
    fig.tight_layout()
    save(fig, "multi_panel", "correlogram")


if __name__ == "__main__":
    render()
