"""Health status vs age — stacked density plot (Wilke fig 10.9).

The continuous analogue of a time-series stacked bar chart. Great for
showing how relative proportions vary along a continuous covariate
(here, age). Note: hides the overall density of the population.
"""

from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import gaussian_kde

from cwilke import data as D
from cwilke.theme import apply_base, save


HEALTH_LEVELS = ["poor", "fair", "good", "very good", "excellent"]
COLORS = ["#f1eef6", "#bdc9e1", "#74a9cf", "#2b8cbe", "#045a8d"]


def render() -> None:
    apply_base()
    df = D.happy_health_age()

    ages = np.linspace(18, 90, 300)

    # Per-category density weighted by subgroup frequency.
    per_category_counts = np.zeros((len(HEALTH_LEVELS), ages.size))
    for i, level in enumerate(HEALTH_LEVELS):
        sub = df.loc[df["health"] == level, "age"].values
        if sub.size < 2:
            continue
        kde = gaussian_kde(sub, bw_method=0.3)
        per_category_counts[i] = kde(ages) * sub.size

    total = per_category_counts.sum(axis=0)
    total[total == 0] = 1  # avoid /0
    fractions = per_category_counts / total

    # stackplot with cumulative fractions
    fig, ax = plt.subplots(figsize=(7.4, 4.0))
    ax.stackplot(ages, fractions, labels=HEALTH_LEVELS,
                  colors=COLORS, edgecolor="white", linewidth=0.5)
    ax.set_xlim(18, 90)
    ax.set_ylim(0, 1)
    ax.set_xlabel("age (years)")
    ax.set_ylabel("relative proportion")
    ax.set_yticks([0, 0.25, 0.5, 0.75, 1.0])
    ax.set_yticklabels(["0%", "25%", "50%", "75%", "100%"])
    leg = ax.legend(loc="center left", bbox_to_anchor=(1.0, 0.5),
                     frameon=False, title="health")
    leg.get_title().set_fontweight("bold")
    for sp in ("top", "right"):
        ax.spines[sp].set_visible(False)
    fig.tight_layout()
    save(fig, "proportions", "health_vs_age_stacked_density")


if __name__ == "__main__":
    render()
