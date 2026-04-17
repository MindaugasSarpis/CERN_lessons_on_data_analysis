"""Boxplots drawn as empty outlines (Wilke fig 22.8)."""

from __future__ import annotations

import matplotlib.pyplot as plt

from cwilke import data as D
from cwilke.theme import apply_base, open_axes, save


MONTH_ORDER = ["Dec", "Nov", "Oct", "Sep", "Aug", "Jul",
               "Jun", "May", "Apr", "Mar", "Feb", "Jan"]


def render() -> None:
    apply_base()
    df = D.lincoln_weather_2016()
    data = [df[df["month"] == m]["mean_temp_F"].values for m in MONTH_ORDER]

    fig, ax = plt.subplots(figsize=(7.2, 4.6))
    bp = ax.boxplot(data, vert=True, labels=MONTH_ORDER,
                    patch_artist=False, showfliers=True,
                    boxprops=dict(color="#2c3e50", linewidth=1.0),
                    medianprops=dict(color="#2c3e50", linewidth=1.2),
                    whiskerprops=dict(color="#2c3e50", linewidth=1.0),
                    capprops=dict(color="#2c3e50", linewidth=1.0),
                    flierprops=dict(marker="o", markersize=3,
                                    markerfacecolor="none",
                                    markeredgecolor="#2c3e50"))
    ax.set_xlabel("month")
    ax.set_ylabel("mean temperature (°F)")
    open_axes(ax)

    fig.tight_layout()
    save(fig, "avoid_line_drawings", "lincoln_box_empty")


if __name__ == "__main__":
    render()
