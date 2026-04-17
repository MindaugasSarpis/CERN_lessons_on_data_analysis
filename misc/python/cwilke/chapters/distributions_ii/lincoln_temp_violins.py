"""Monthly temperature violin plots (Wilke fig 9.6).

Violins show the full shape of each distribution — revealing bimodality
that boxplots hide. Trade-off: they can look rich even when there are
only a few points per group, so only use them when you have plenty of
data per category.
"""

from __future__ import annotations

import matplotlib.pyplot as plt

from cwilke import data as D
from cwilke.theme import PRIMARY_BLUE, apply_base, hgrid, save


_MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
           "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]


def render() -> None:
    apply_base()
    df = D.lincoln_temps()
    groups = [df.loc[df["month"] == m, "mean_temp_F"].values for m in _MONTHS]

    fig, ax = plt.subplots(figsize=(8.2, 4.4))
    parts = ax.violinplot(groups, positions=range(len(_MONTHS)),
                           widths=0.8, showmeans=False,
                           showmedians=True, showextrema=False)
    for body in parts["bodies"]:
        body.set_facecolor(PRIMARY_BLUE)
        body.set_edgecolor("#2c3e50")
        body.set_alpha(0.75)
        body.set_linewidth(0.8)
    parts["cmedians"].set_color("#2c3e50")
    parts["cmedians"].set_linewidth(1.4)

    ax.set_xticks(range(len(_MONTHS)))
    ax.set_xticklabels(_MONTHS)
    ax.set_xlabel("month")
    ax.set_ylabel("mean temperature (°F)")
    hgrid(ax)
    fig.tight_layout()
    save(fig, "distributions_ii", "lincoln_temp_violins")


if __name__ == "__main__":
    render()
