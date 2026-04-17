"""Bayesian credible vs OLS confidence intervals (Wilke fig 16.13).

We use a tiny synthetic Bayesian posterior (normal-normal conjugate
update, very weak prior) to demonstrate the small shrinkage relative to
the pooled-variance OLS estimate.
"""

from __future__ import annotations

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import t as student_t

from cwilke.data import cacao_ratings
from cwilke.theme import apply_base, hgrid, save


def render() -> None:
    apply_base()
    df = cacao_ratings()
    countries = ["Austria", "Belgium", "Canada", "Peru", "Switzerland", "US"]

    grand_mean = df["rating"].mean()
    grand_var = df["rating"].var(ddof=1)

    rows = []
    for c in countries:
        vals = df[df["location"] == c]["rating"].values
        n = len(vals)
        m = vals.mean()
        se = vals.std(ddof=1) / np.sqrt(n)
        # OLS: use t-distribution 95% CI
        ols_crit = student_t.ppf(0.975, n - 1)
        ols_lo, ols_hi = m - ols_crit * se, m + ols_crit * se
        # Bayes: conjugate update with N(grand_mean, tau^2) prior, tau^2 = grand_var
        prior_prec = 1 / grand_var
        data_prec = n / (vals.var(ddof=1) + 1e-9)
        post_mean = (prior_prec * grand_mean + data_prec * m) / (prior_prec + data_prec)
        post_var = 1 / (prior_prec + data_prec)
        post_sd = np.sqrt(post_var)
        bay_lo, bay_hi = post_mean - 1.96 * post_sd, post_mean + 1.96 * post_sd
        rows.append((c, m, ols_lo, ols_hi, post_mean, bay_lo, bay_hi))
    rows.sort(key=lambda r: r[1])

    fig, ax = plt.subplots(figsize=(7.8, 4.4))
    ys = np.arange(len(rows))
    offset = 0.18
    for y, (c, m, lo, hi, pm, blo, bhi) in zip(ys, rows):
        # OLS
        ax.hlines(y + offset, lo, hi, color="gray", linewidth=1.4)
        ax.vlines([lo, hi], y + offset - 0.1, y + offset + 0.1,
                  color="gray", linewidth=1.4)
        ax.plot(m, y + offset, "o", color="gray", markersize=6)
        # Bayes
        ax.hlines(y - offset, blo, bhi, color="#0f4c75", linewidth=1.4)
        ax.vlines([blo, bhi], y - offset - 0.1, y - offset + 0.1,
                  color="#0f4c75", linewidth=1.4)
        ax.plot(pm, y - offset, "o", color="#0f4c75", markersize=6)

    ax.set_yticks(ys)
    ax.set_yticklabels([r[0] for r in rows])
    ax.set_xlabel("mean rating")
    ax.set_xlim(2.6, 3.6)

    import matplotlib.lines as mlines
    handles = [
        mlines.Line2D([], [], color="gray", marker="o",
                      label="95% confidence interval"),
        mlines.Line2D([], [], color="#0f4c75", marker="o",
                      label="95% credible interval"),
    ]
    ax.legend(handles=handles, loc="lower right", frameon=False)
    hgrid(ax)
    fig.tight_layout()
    save(fig, "uncertainty", "bayes_vs_ols")


if __name__ == "__main__":
    render()
