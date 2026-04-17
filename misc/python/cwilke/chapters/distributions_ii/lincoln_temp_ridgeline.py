"""Ridgeline plot of Lincoln monthly temperatures (Wilke fig 9.10).

Ridgelines = stacked density plots, one per group. For time-keyed
distributions they beat both boxplots and violins: shape is easy to
compare, trends across time are clearly visible.
"""

from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import gaussian_kde

from cwilke import data as D
from cwilke.theme import PRIMARY_BLUE, apply_base, save, open_axes


_MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
           "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]


def render() -> None:
    apply_base()
    df = D.lincoln_temps()

    temps = df["mean_temp_F"].values
    lo, hi = temps.min() - 5, temps.max() + 5
    xs = np.linspace(lo, hi, 400)

    # Compute densities for every month.
    densities = []
    for m in _MONTHS:
        vals = df.loc[df["month"] == m, "mean_temp_F"].values
        kde = gaussian_kde(vals, bw_method=0.35)
        densities.append(kde(xs))

    peak = max(d.max() for d in densities)
    offset_step = peak * 0.55

    fig, ax = plt.subplots(figsize=(7.6, 6.2))
    # Draw from bottom (December last) up to top (January first).
    for i, (month, d) in reversed(list(enumerate(zip(_MONTHS, densities)))):
        base = i * offset_step
        ax.fill_between(xs, base, base + d,
                         color=PRIMARY_BLUE, alpha=0.75, linewidth=0)
        ax.plot(xs, base + d, color="white", linewidth=1.0)

    ax.set_yticks([i * offset_step for i in range(len(_MONTHS))])
    ax.set_yticklabels(_MONTHS)
    ax.set_xlabel("mean temperature (°F)")
    open_axes(ax)
    ax.tick_params(axis="y", length=0)
    fig.tight_layout()
    save(fig, "distributions_ii", "lincoln_temp_ridgeline")


if __name__ == "__main__":
    render()
