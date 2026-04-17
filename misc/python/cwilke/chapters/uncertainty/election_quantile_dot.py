"""Quantile dotplot approximation of the election distribution (Wilke 16.3)."""

from __future__ import annotations

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

from cwilke.theme import apply_base, save


def _quantile_dots(ax, n_dots, mu, sd, binwidth, y_scale, title):
    # quantiles of the normal: place a dot at the midpoint of each equally
    # sized probability bin.
    probs = (np.arange(n_dots) + 0.5) / n_dots
    xs = norm.ppf(probs, loc=mu, scale=sd)
    # Bin the dots by x (using binwidth), stacking within each bin.
    bins = np.arange(xs.min() - binwidth / 2,
                      xs.max() + binwidth * 1.5, binwidth)
    digits = np.digitize(xs, bins) - 1
    counts = np.zeros_like(digits)
    for i, d in enumerate(digits):
        counts[i] = np.sum(digits[:i] == d)

    # Normal overlay
    x_line = np.linspace(-3.5, 5.5, 300)
    y_line = y_scale * norm.pdf(x_line, mu, sd)
    ax.plot(x_line, y_line, color="#2c3e50", linewidth=1.0)
    ax.axvline(0, color="gray", linestyle="--", linewidth=0.8)

    # Dots
    r = binwidth / 2 * 0.9
    for xi, ci in zip(xs, counts):
        color = "#f8f1a9" if xi <= 0 else "#b1daf4"
        circ = plt.Circle((xi, ci * binwidth + r), r,
                           facecolor=color, edgecolor="#2c3e50", linewidth=0.6)
        ax.add_patch(circ)

    ax.set_xlim(-3.0, 5.0)
    ax.set_ylim(0, 1.1 * max(counts.max() * binwidth + 2 * r,
                                y_line.max()))
    ax.set_title(title, fontsize=11, loc="left")
    for s in ("top", "right", "left"):
        ax.spines[s].set_visible(False)
    ax.set_yticks([])
    ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda v, _: f"{v:.1f}%"))


def render() -> None:
    apply_base()
    mu, sd = 1.02, 0.9
    fig, axes = plt.subplots(2, 1, figsize=(7.0, 5.8))
    _quantile_dots(axes[0], 50, mu, sd, 0.29, 1.92, "(a) 50 dots (2% each)")
    _quantile_dots(axes[1], 10, mu, sd, 0.65, 1.92, "(b) 10 dots (10% each)")
    axes[1].set_xlabel("percentage point advantage for blue")
    fig.tight_layout()
    save(fig, "uncertainty", "election_quantile_dot")


if __name__ == "__main__":
    render()
