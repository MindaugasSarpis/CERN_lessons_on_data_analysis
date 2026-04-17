"""Frequentist interpretation of a CI (Wilke fig 16.12).

10 independent samples are drawn from a standard normal.  Each sample
produces a 68% CI (mean ± SE).  Most include the true mean (green); a
few don't (orange).  The true population density is plotted to the right.
"""

from __future__ import annotations

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

from cwilke.theme import apply_base, hgrid, save


def render() -> None:
    apply_base()
    rng = np.random.default_rng(85439)

    n_samples = 10
    n = 5
    means = []
    ses = []
    for _ in range(n_samples):
        s = rng.normal(0, 1, n)
        means.append(s.mean())
        ses.append(s.std(ddof=1) / np.sqrt(n))
    means = np.array(means)
    ses = np.array(ses)
    lower = means - ses
    upper = means + ses
    includes = (lower <= 0) & (upper >= 0)

    fig, ax = plt.subplots(figsize=(6.2, 6.2))

    # Population density on the right (rotated)
    y_line = np.linspace(-3, 3, 300)
    dens = norm.pdf(y_line)
    ax.fill_betweenx(y_line, 10.5, 10.5 + dens * 1.8,
                      color="#b1daf4", linewidth=0)
    ax.text(11.7, 2.6, "population", fontsize=11)
    ax.text(11.0, 0.0, "mean", fontsize=10)

    # horizontal zero line
    ax.axhline(0, color="#2c3e50", linestyle="--", linewidth=0.8)

    # samples
    xs = np.arange(1, n_samples + 1)
    for x, m, lo, hi, inc in zip(xs, means, lower, upper, includes):
        color = "#009E73" if inc else "#D55E00"
        ax.vlines(x, lo, hi, color=color, linewidth=1.2)
        ax.hlines([lo, hi], x - 0.12, x + 0.12, color=color, linewidth=1.2)
        ax.plot(x, m, "o", color=color, markersize=6)

    ax.text(2.5, -2.1, "CI excludes true mean", color="#D55E00",
             fontsize=10)
    ax.text(6.5, 1.6, "CI includes true mean", color="#009E73",
             fontsize=10)

    ax.set_xticks(xs)
    ax.set_xticklabels([f"sample {i}" for i in xs], rotation=90, fontsize=9)
    ax.set_xlim(0.5, 13)
    ax.set_ylim(-3, 3)
    ax.set_yticks([-2, 0, 2])
    hgrid(ax)
    fig.tight_layout()
    save(fig, "uncertainty", "ci_frequentist_expl")


if __name__ == "__main__":
    render()
