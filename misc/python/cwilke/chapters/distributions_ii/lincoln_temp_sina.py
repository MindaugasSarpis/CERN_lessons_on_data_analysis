"""Sina plot of monthly temperatures (Wilke fig 9.9).

A sina plot is a hybrid between a violin and a jittered strip: each
point is placed at the real data's y value but jittered in x in
proportion to the local density. Visible individuals AND visible shape.
"""

from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import gaussian_kde

from cwilke import data as D
from cwilke.theme import PRIMARY_BLUE, apply_base, hgrid, save


_MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
           "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]


def _sina_jitter(values: np.ndarray, max_width: float,
                 rng: np.random.Generator) -> np.ndarray:
    """Jitter x positions proportional to local KDE density."""
    kde = gaussian_kde(values, bw_method=0.35)
    d = kde(values)
    d = d / d.max()
    return rng.uniform(-1, 1, values.size) * d * max_width


def render() -> None:
    apply_base()
    df = D.lincoln_temps()
    rng = np.random.default_rng(42)

    fig, ax = plt.subplots(figsize=(8.2, 4.6))

    # First: faint violins as background.
    groups = [df.loc[df["month"] == m, "mean_temp_F"].values for m in _MONTHS]
    parts = ax.violinplot(groups, positions=range(len(_MONTHS)),
                           widths=0.85, showmeans=False,
                           showmedians=False, showextrema=False)
    for body in parts["bodies"]:
        body.set_facecolor("#cfd8dc")
        body.set_edgecolor("none")
        body.set_alpha(0.9)

    # Overlay sina points.
    for i, vals in enumerate(groups):
        x_j = _sina_jitter(vals, 0.35, rng)
        ax.scatter(i + x_j, vals, s=10, color=PRIMARY_BLUE,
                   alpha=0.7, edgecolor="none")

    ax.set_xticks(range(len(_MONTHS)))
    ax.set_xticklabels(_MONTHS)
    ax.set_xlabel("month")
    ax.set_ylabel("mean temperature (°F)")
    hgrid(ax)
    fig.tight_layout()
    save(fig, "distributions_ii", "lincoln_temp_sina")


if __name__ == "__main__":
    render()
