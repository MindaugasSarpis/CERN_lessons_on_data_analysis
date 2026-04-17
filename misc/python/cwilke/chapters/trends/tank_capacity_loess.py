"""Fuel-tank capacity vs car price with LOESS smoother (Wilke fig 14.4)."""

from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np

from cwilke import data as D
from cwilke.theme import PRIMARY_BLUE, apply_base, grid, save


def _loess(x, y, span=0.5):
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)
    n = len(x)
    k = max(int(span * n), 5)
    xs = np.linspace(x.min(), x.max(), 200)
    out = np.empty_like(xs)
    for i, xi in enumerate(xs):
        d = np.abs(x - xi)
        idx = np.argsort(d)[:k]
        h = d[idx].max() or 1.0
        w = (1 - (d[idx] / h) ** 3) ** 3
        xj = x[idx]; yj = y[idx]
        sw = w.sum()
        xm = (w * xj).sum() / sw
        ym = (w * yj).sum() / sw
        denom = (w * (xj - xm) ** 2).sum() or 1
        b = (w * (xj - xm) * (yj - ym)).sum() / denom
        a = ym - b * xm
        out[i] = a + b * xi
    return xs, out


def render() -> None:
    apply_base()
    df = D.cars93()

    fig, ax = plt.subplots(figsize=(6.0, 4.4))
    ax.scatter(df["Price"], df["Fuel_tank_capacity"],
               s=28, color="#9e9e9e", edgecolors="white",
               linewidths=0.4)
    xs, ys = _loess(df["Price"].values, df["Fuel_tank_capacity"].values,
                     span=0.5)
    ax.plot(xs, ys, color=PRIMARY_BLUE, linewidth=2.2)
    ax.set_xticks([20, 40, 60])
    ax.set_xticklabels(["$20,000", "$40,000", "$60,000"])
    ax.set_xlabel("price (USD)")
    ax.set_ylabel("fuel-tank capacity\n(US gallons)")
    grid(ax)
    save(fig, "trends", "tank_capacity_loess")


if __name__ == "__main__":
    render()
