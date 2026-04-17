"""Confidence intervals widen with smaller n (Wilke fig 16.6).

Graded error bars compare Canada (n=125) to Switzerland (n=38).
"""

from __future__ import annotations

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import t as student_t

from cwilke.data import cacao_ratings
from cwilke.theme import apply_base, save, vgrid


def _levels(mean, se, n):
    out = {}
    for level, p in [("99%", 0.995), ("95%", 0.975), ("80%", 0.90)]:
        crit = student_t.ppf(p, n - 1)
        out[level] = (mean - crit * se, mean + crit * se)
    return out


def render() -> None:
    apply_base()
    rng = np.random.default_rng(7843)
    df = cacao_ratings()

    colors = {"99%": "#9fc1dd", "95%": "#4a87b3", "80%": "#0f4c75"}
    widths = {"99%": 1.5,       "95%": 2.75,      "80%": 4.0}

    countries = ["Switzerland", "Canada"]
    fig, ax = plt.subplots(figsize=(8.6, 4.2))

    y_positions = []
    for i, country in enumerate(countries):
        vals = df[df["location"] == country]["rating"].values
        n = len(vals)
        mean = vals.mean()
        sd = vals.std(ddof=1)
        se = sd / np.sqrt(n)
        # data row
        y_data = 2 * i
        y_ci = 2 * i + 0.9
        y_positions.extend([y_data, y_ci])
        ax.scatter(vals, np.full(n, y_data) + rng.uniform(-0.25, 0.25, n),
                   color="#116a4a", s=6, alpha=0.7)
        # SD bar on data row
        ax.errorbar([mean], [y_data], xerr=[[sd], [sd]],
                    fmt="o", color="#D55E00", ecolor="#2c3e50",
                    elinewidth=1.0, capsize=3, markersize=5)
        # CI row with three graded bars
        lvls = _levels(mean, se, n)
        for lev, (lo, hi) in lvls.items():
            ax.hlines(y_ci, lo, hi, colors=colors[lev],
                      linewidth=widths[lev])
        ax.plot(mean, y_ci, "o", color="#D55E00", markersize=6)
        ax.text(4.15, y_data, f"{country},\nn = {n}",
                va="center", ha="left", fontsize=10)

    # legend
    import matplotlib.lines as mlines
    handles = [mlines.Line2D([], [], color=colors[k], linewidth=widths[k],
                              label=k) for k in ("80%", "95%", "99%")]
    ax.legend(handles=handles, title="confidence level",
              loc="upper left", frameon=False, ncol=3)

    ax.set_xlim(1.95, 4.5)
    ax.set_yticks([])
    ax.set_xlabel("chocolate flavor rating")
    vgrid(ax)
    fig.tight_layout()
    save(fig, "uncertainty", "cocoa_ci_vs_n")


if __name__ == "__main__":
    render()
