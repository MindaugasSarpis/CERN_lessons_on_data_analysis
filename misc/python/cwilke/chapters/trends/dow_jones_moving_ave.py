"""Dow Jones 2009 with 20/50/100-day moving averages — centred
(Wilke fig 14.2, panel b)."""

from __future__ import annotations

import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import numpy as np

from cwilke import data as D
from cwilke.theme import apply_base, grid, save


def _moving_ave(y, window, center=True):
    out = np.full_like(y, np.nan, dtype=float)
    half = window // 2
    n = len(y)
    for i in range(n):
        if center:
            lo, hi = i - half, i + half + 1
        else:
            lo, hi = i - window + 1, i + 1
        if lo < 0 or hi > n:
            continue
        out[i] = y[lo:hi].mean()
    return out


def render() -> None:
    apply_base()
    df = D.dow_jones_2009()
    y = df["close"].values
    x = df["date"].values

    fig, ax = plt.subplots(figsize=(7.6, 4.0))
    ax.plot(x, y, color="#333333", linewidth=0.7, label="daily")
    for window, col, label in [
        (20,  "#009E73", "20-day average"),
        (50,  "#D55E00", "50-day average"),
        (100, "#0072B2", "100-day average"),
    ]:
        ax.plot(x, _moving_ave(y, window), color=col, linewidth=1.8,
                label=label)
    ax.set_ylabel("Dow Jones Industrial Average")
    ax.legend(loc="lower right", frameon=False)
    ax.xaxis.set_major_locator(mdates.MonthLocator(bymonth=[1, 4, 7, 10]))
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %Y"))
    grid(ax)
    fig.autofmt_xdate()
    save(fig, "trends", "dow_jones_moving_ave")


if __name__ == "__main__":
    render()
