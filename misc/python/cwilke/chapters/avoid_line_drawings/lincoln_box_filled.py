"""Boxplots with a light grey fill — boxes stand out (Wilke fig 22.9)."""

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
                    patch_artist=True, showfliers=True,
                    medianprops=dict(color="#2c3e50", linewidth=1.3),
                    whiskerprops=dict(color="#2c3e50", linewidth=1.0),
                    capprops=dict(color="#2c3e50", linewidth=1.0),
                    flierprops=dict(marker="o", markersize=3,
                                    markerfacecolor="#90a4ae",
                                    markeredgecolor="white",
                                    alpha=0.85))
    for box in bp["boxes"]:
        box.set_facecolor("#e0e0e0")
        box.set_edgecolor("#2c3e50")
        box.set_linewidth(1.0)
    ax.set_xlabel("month")
    ax.set_ylabel("mean temperature (°F)")
    open_axes(ax)

    fig.tight_layout()
    save(fig, "avoid_line_drawings", "lincoln_box_filled")


if __name__ == "__main__":
    render()
