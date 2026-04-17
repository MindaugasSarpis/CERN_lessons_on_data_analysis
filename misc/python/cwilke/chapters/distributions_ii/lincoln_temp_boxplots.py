"""Monthly temperature boxplots for Lincoln, NE (Wilke fig 9.4).

Twelve-month boxplot sequence — a direct upgrade from the error-bar
version. Shows the median, IQR, whiskers, and any outliers at a glance.
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
    ax.boxplot(
        groups,
        positions=range(len(_MONTHS)),
        widths=0.55,
        patch_artist=True,
        medianprops=dict(color="black", linewidth=1.6),
        boxprops=dict(facecolor=PRIMARY_BLUE, edgecolor="#2c3e50",
                      alpha=0.85, linewidth=1.0),
        whiskerprops=dict(color="#2c3e50", linewidth=1.0),
        capprops=dict(color="#2c3e50", linewidth=1.0),
        flierprops=dict(marker="o", markerfacecolor="#2c3e50",
                        markersize=4, markeredgecolor="none", alpha=0.7),
    )
    ax.set_xticks(range(len(_MONTHS)))
    ax.set_xticklabels(_MONTHS)
    ax.set_xlabel("month")
    ax.set_ylabel("mean temperature (°F)")
    hgrid(ax)
    fig.tight_layout()
    save(fig, "distributions_ii", "lincoln_temp_boxplots")


if __name__ == "__main__":
    render()
