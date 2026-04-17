"""Dow Jones 2009 — LOESS-style smoother vs 100-day moving average
(Wilke fig 14.3)."""

from __future__ import annotations

import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import numpy as np

from cwilke import data as D
from cwilke.theme import apply_base, grid, save


def _moving_ave(y, window):
    out = np.full_like(y, np.nan, dtype=float)
    half = window // 2
    n = len(y)
    for i in range(n):
        lo, hi = i - half, i + half + 1
        if lo < 0 or hi > n:
            continue
        out[i] = y[lo:hi].mean()
    return out


def _loess(x, y, span=0.3):
    """Simple local-linear LOESS using a tricube kernel."""
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)
    n = len(x)
    k = max(int(span * n), 5)
    out = np.empty(n)
    for i in range(n):
        d = np.abs(x - x[i])
        idx = np.argsort(d)[:k]
        h = d[idx].max() or 1.0
        w = (1 - (d[idx] / h) ** 3) ** 3
        # weighted least squares for line
        xi = x[idx]
        yi = y[idx]
        W = w
        sw = W.sum()
        xm = (W * xi).sum() / sw
        ym = (W * yi).sum() / sw
        b = (W * (xi - xm) * (yi - ym)).sum() / ((W * (xi - xm) ** 2).sum() or 1)
        a = ym - b * xm
        out[i] = a + b * x[i]
    return out


def render() -> None:
    apply_base()
    df = D.dow_jones_2009()
    y = df["close"].values
    x = df["date"].values
    t = np.arange(len(y), dtype=float)

    fig, ax = plt.subplots(figsize=(7.6, 3.8))
    ax.plot(x, y, color="#333333", linewidth=0.7, label="daily")
    ax.plot(x, _moving_ave(y, 100), color="#D55E00", linewidth=1.8,
            label="100-day average")
    ax.plot(x, _loess(t, y, span=0.35),
            color="#0072B2", linewidth=1.8, label="LOESS smoother")
    ax.set_ylabel("Dow Jones Industrial Average")
    ax.legend(loc="lower right", frameon=False)
    ax.xaxis.set_major_locator(mdates.MonthLocator(bymonth=[1, 4, 7, 10]))
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %Y"))
    grid(ax)
    fig.autofmt_xdate()
    save(fig, "trends", "dow_jones_loess")


if __name__ == "__main__":
    render()
