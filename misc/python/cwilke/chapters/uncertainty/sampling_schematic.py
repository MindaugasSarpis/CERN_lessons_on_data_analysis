"""Schematic of population / sample / sampling distribution (Wilke 16.4)."""

from __future__ import annotations

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

from cwilke.theme import apply_base, save


def render() -> None:
    apply_base()
    fill_color = "#cfe7f6"
    fig, (ax1, ax2, ax3) = plt.subplots(
        3, 1, figsize=(7.2, 7.4),
        gridspec_kw={"height_ratios": [1, 0.45, 1]})

    x = np.linspace(-4, 4, 300)

    # --- Population distribution --------------------------------------
    y = norm.pdf(x)
    ax1.fill_between(x, y, color=fill_color)
    ax1.plot([0, 0], [0, norm.pdf(0)], color="#2c3e50",
             linestyle="--", linewidth=0.8)
    ax1.annotate("", xy=(1, norm.pdf(1)), xytext=(0, norm.pdf(1)),
                  arrowprops=dict(arrowstyle="<->", color="#2c3e50", lw=0.9))
    ax1.text(0.1, norm.pdf(0) * 0.4, "mean", fontsize=10, va="top")
    ax1.text(1.05, norm.pdf(1) * 1.02, "standard deviation", fontsize=10)
    ax1.set_title("population distribution", loc="left", fontsize=12)
    ax1.set_xlabel("variable of interest")
    ax1.set_yticks([])
    ax1.set_xlim(-4, 4)
    for s in ("top", "right", "left"):
        ax1.spines[s].set_visible(False)

    # --- Sample --------------------------------------------------------
    rng = np.random.default_rng(452061)
    n = 15
    sample = rng.normal(0, 1, n)
    ax2.scatter(sample, rng.normal(0, 0.01, n),
                s=60, facecolor=fill_color,
                edgecolor="#2c3e50", linewidth=0.6)
    m = sample.mean()
    sd = sample.std(ddof=1)
    ax2.plot([m, m], [-0.2, 0.2], color="#D55E00", linewidth=2.0)
    ax2.annotate("", xy=(m + sd, 0.13), xytext=(m, 0.13),
                  arrowprops=dict(arrowstyle="<->", color="#2c3e50", lw=0.9))
    ax2.text(m + 0.05, -0.18, "sample mean", fontsize=10, color="#D55E00")
    ax2.text(m + sd + 0.05, 0.14, "sample standard dev.", fontsize=10)
    ax2.text(min(sample) - 0.2, 0.12, "observations", fontsize=10, ha="right")
    ax2.set_title("sample", loc="left", fontsize=12)
    ax2.set_xlim(-4, 4)
    ax2.set_ylim(-0.25, 0.25)
    ax2.set_yticks([])
    ax2.set_xticks([])
    for s in ("top", "right", "left", "bottom"):
        ax2.spines[s].set_visible(False)

    # --- Sampling distribution ----------------------------------------
    se = 1 / np.sqrt(n)
    y2 = norm.pdf(x, 0, se)
    ax3.fill_between(x, y2, color=fill_color)
    ax3.plot([0, 0], [0, norm.pdf(0, 0, se)], color="#2c3e50",
             linestyle="--", linewidth=0.8)
    ax3.annotate("", xy=(se, norm.pdf(se, 0, se)),
                  xytext=(0, norm.pdf(se, 0, se)),
                  arrowprops=dict(arrowstyle="<->", color="#2c3e50", lw=0.9))
    ax3.text(0.08, norm.pdf(0, 0, se) * 0.4, "mean of the sample means",
             fontsize=10, va="top")
    ax3.text(se + 0.05, norm.pdf(se, 0, se) * 1.02,
             "standard error", fontsize=10)
    ax3.set_title("sampling distribution of the mean", loc="left", fontsize=12)
    ax3.set_xlabel("sample mean")
    ax3.set_yticks([])
    ax3.set_xlim(-4, 4)
    for s in ("top", "right", "left"):
        ax3.spines[s].set_visible(False)

    fig.tight_layout()
    save(fig, "uncertainty", "sampling_schematic")


if __name__ == "__main__":
    render()
