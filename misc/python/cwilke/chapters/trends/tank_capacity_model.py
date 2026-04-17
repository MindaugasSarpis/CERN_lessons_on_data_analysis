"""Fuel-tank capacity fit with y = A − B·exp(−m·x) (Wilke fig 14.6)."""

from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np

from cwilke import data as D
from cwilke.theme import PRIMARY_BLUE, apply_base, grid, save


def _fit_exp_saturating(x, y):
    """Fit y = A - B*exp(-m*x) by simple grid + refinement."""
    best = None
    for A in np.linspace(18, 28, 25):
        for m in np.linspace(0.02, 0.35, 30):
            # with A and m fixed, B = (A - y) / exp(-m*x) in least squares sense
            ex = np.exp(-m * x)
            denom = (ex ** 2).sum()
            if denom == 0:
                continue
            B = ((A - y) * ex).sum() / denom
            pred = A - B * ex
            err = ((y - pred) ** 2).sum()
            if best is None or err < best[0]:
                best = (err, A, B, m)
    return best[1], best[2], best[3]


def render() -> None:
    apply_base()
    df = D.cars93()
    x = df["Price"].values
    y = df["Fuel_tank_capacity"].values

    A, B, m = _fit_exp_saturating(x, y)
    xs = np.linspace(x.min(), x.max(), 200)
    ys = A - B * np.exp(-m * xs)

    fig, ax = plt.subplots(figsize=(6.0, 4.4))
    ax.scatter(x, y, s=28, color="#9e9e9e", edgecolors="white",
               linewidths=0.4)
    ax.plot(xs, ys, color=PRIMARY_BLUE, linewidth=2.2,
            label=f"A − B·exp(−m·x)\nA={A:.1f}, B={B:.1f}, m={m:.2f}")
    ax.set_xticks([20, 40, 60])
    ax.set_xticklabels(["$20,000", "$40,000", "$60,000"])
    ax.set_xlabel("price (USD)")
    ax.set_ylabel("fuel-tank capacity\n(US gallons)")
    ax.legend(loc="lower right", frameon=False)
    grid(ax)
    save(fig, "trends", "tank_capacity_model")


if __name__ == "__main__":
    render()
