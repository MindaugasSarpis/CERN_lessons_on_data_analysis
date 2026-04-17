"""Seasonal temperature: linear line plot vs polar (Wilke fig 3.9)."""

from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from cwilke import data as D
from cwilke.theme import PRIMARY_BLUE, apply_base, hgrid, save


MONTH_LABELS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
                "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]


def render() -> None:
    apply_base()

    df = D.lincoln_temps()
    # day-of-year -> month (approximate; uses a non-leap calendar)
    start = pd.Timestamp("2016-01-01")
    dates = start + pd.to_timedelta(df["day"] - 1, unit="D")
    df = df.assign(month=dates.dt.month)
    monthly = df.groupby("month")["mean_temp_F"].mean().reindex(range(1, 13))

    months = monthly.index.values
    temps = monthly.values

    fig = plt.figure(figsize=(10.0, 4.4))
    ax1 = fig.add_subplot(1, 2, 1)
    ax2 = fig.add_subplot(1, 2, 2, projection="polar")

    # linear
    ax1.plot(months, temps, color=PRIMARY_BLUE, linewidth=2.2,
             marker="o", markersize=6)
    ax1.set_xticks(range(1, 13))
    ax1.set_xticklabels(MONTH_LABELS, fontsize=9)
    ax1.set_ylabel("mean temp (°F)")
    ax1.set_title("cartesian")
    hgrid(ax1)

    # polar: close the circle
    theta = 2 * np.pi * (months - 1) / 12
    r = temps
    theta_c = np.concatenate([theta, theta[:1]])
    r_c = np.concatenate([r, r[:1]])

    ax2.plot(theta_c, r_c, color=PRIMARY_BLUE, linewidth=2.2,
             marker="o", markersize=5)
    ax2.set_theta_zero_location("N")
    ax2.set_theta_direction(-1)
    ax2.set_xticks(2 * np.pi * np.arange(12) / 12)
    ax2.set_xticklabels(MONTH_LABELS, fontsize=9)
    ax2.tick_params(axis="y", labelsize=8)
    ax2.set_title("polar", pad=14)

    fig.tight_layout()
    save(fig, "coordinates_axes", "polar_vs_cartesian")


if __name__ == "__main__":
    render()
