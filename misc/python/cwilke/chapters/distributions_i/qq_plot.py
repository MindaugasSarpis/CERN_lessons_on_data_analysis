"""Q-Q plot: titanic age vs theoretical Normal quantiles (Wilke fig 8.9).

A quantile-quantile plot compares the empirical quantiles of a dataset to
the quantiles of a reference distribution. Points following the line
suggest the reference fits; systematic deviation diagnoses skew, heavy
tails, etc.
"""

from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

from cwilke import data as D
from cwilke.theme import MUTED, PRIMARY_BLUE, apply_base, open_axes, save


def render() -> None:
    apply_base()

    df = D.titanic()
    x = df["age"].dropna().values
    x = np.sort(x)
    n = x.size

    # Theoretical quantiles under standard Normal (mean/sd matched).
    ranks = np.arange(1, n + 1)
    theoretical = stats.norm.ppf((ranks - 0.5) / n,
                                  loc=x.mean(), scale=x.std(ddof=1))

    fig, ax = plt.subplots(figsize=(5.6, 5.2))
    ax.scatter(theoretical, x, s=18, color=PRIMARY_BLUE,
               edgecolor="white", linewidth=0.4, alpha=0.85)

    # Reference y = x line
    lo = min(theoretical.min(), x.min())
    hi = max(theoretical.max(), x.max())
    ax.plot([lo, hi], [lo, hi],
            color=MUTED, linewidth=1.4, linestyle="--", zorder=1)

    ax.set_xlabel("theoretical normal quantile")
    ax.set_ylabel("observed age (years)")
    ax.set_title("Q-Q plot · titanic passenger ages vs. Normal")
    open_axes(ax)
    fig.tight_layout()
    save(fig, "distributions_i", "qq_plot")


if __name__ == "__main__":
    render()
