"""Sample, SD, SE, and 80/95/99% CI for Canadian cocoa ratings (Wilke 16.5)."""

from __future__ import annotations

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import t as student_t

from cwilke.data import cacao_ratings
from cwilke.theme import apply_base, save, vgrid


def render() -> None:
    apply_base()
    rng = np.random.default_rng(7843)
    df = cacao_ratings()
    canada = df[df["location"] == "Canada"]["rating"].values

    mean = canada.mean()
    sd = canada.std(ddof=1)
    n = len(canada)
    se = sd / np.sqrt(n)

    levels = {
        "80% confidence interval": 0.80,
        "95% confidence interval": 0.95,
        "99% confidence interval": 0.99,
    }

    rows = [
        ("99% confidence interval", mean, mean + student_t.ppf(0.005, n - 1) * se,
                                       mean + student_t.ppf(0.995, n - 1) * se),
        ("95% confidence interval", mean, mean + student_t.ppf(0.025, n - 1) * se,
                                       mean + student_t.ppf(0.975, n - 1) * se),
        ("80% confidence interval", mean, mean + student_t.ppf(0.10, n - 1) * se,
                                       mean + student_t.ppf(0.90, n - 1) * se),
        ("+/- standard error",      mean, mean - se, mean + se),
        ("+/- standard deviation",  mean, mean - sd, mean + sd),
    ]
    labels = [r[0] for r in rows][::-1] + ["sample"]
    ys = np.arange(len(labels))
    # sample at top
    fig, ax = plt.subplots(figsize=(8.6, 4.2))
    # Sample points jittered
    jitter = rng.uniform(-0.25, 0.25, n)
    ax.scatter(canada, np.full(n, ys[-1]) + jitter,
               color="#116a4a", s=6, alpha=0.7)

    # error bars
    for i, row in enumerate(rows[::-1]):
        lab, m, lo, hi = row
        y = ys[i]
        ax.errorbar([m], [y], xerr=[[m - lo], [hi - m]],
                    fmt="o", color="#D55E00", ecolor="#2c3e50",
                    elinewidth=1.2, capsize=3, markersize=6)
        ax.text(hi + 0.04, y, lab, va="center", fontsize=10)

    ax.text(max(canada) + 0.06, ys[-1], "sample", va="center", fontsize=10)
    ax.text(mean, ys[-1] + 0.35, "mean", color="#D55E00",
            ha="center", va="bottom", fontsize=10)
    ax.plot(mean, ys[-1], "o", color="#D55E00", markersize=6)

    ax.set_xlim(1.95, 4.4)
    ax.set_yticks([])
    ax.set_xlabel("chocolate flavor rating")
    vgrid(ax)
    fig.tight_layout()
    save(fig, "uncertainty", "cocoa_data_vs_ci")


if __name__ == "__main__":
    render()
