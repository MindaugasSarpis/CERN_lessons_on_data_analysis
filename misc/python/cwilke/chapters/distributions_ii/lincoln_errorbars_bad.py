"""Mean ± 2σ error bars per month (Wilke fig 9.1, "bad").

Error bars conflate two different ideas — uncertainty of the mean
vs. spread of the population — and hide any skew or bimodality.
Compare against the boxplot / violin / sina renditions in this chapter.
"""

from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np

from cwilke import data as D
from cwilke.theme import apply_base, hgrid, save, stamp_bad


_MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
           "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]


def render() -> None:
    apply_base()
    df = D.lincoln_temps()

    means = [df.loc[df["month"] == m, "mean_temp_F"].mean() for m in _MONTHS]
    sds   = [df.loc[df["month"] == m, "mean_temp_F"].std()  for m in _MONTHS]

    fig, ax = plt.subplots(figsize=(8.2, 4.2))
    xs = np.arange(len(_MONTHS))
    ax.errorbar(xs, means,
                yerr=[2 * s for s in sds],
                fmt="o", color="#2c3e50", ecolor="#2c3e50",
                capsize=4, markersize=6, linewidth=1.2)
    ax.set_xticks(xs)
    ax.set_xticklabels(_MONTHS)
    ax.set_xlabel("month")
    ax.set_ylabel("mean temperature (°F)")
    hgrid(ax)
    stamp_bad(fig)
    fig.tight_layout()
    save(fig, "distributions_ii", "lincoln_errorbars_bad")


if __name__ == "__main__":
    render()
