"""Hypothetical Outcome Plot: bootstrap fit lines on a scatter (Wilke fig 16.10)."""

from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np

from cwilke.theme import PRIMARY_BLUE, apply_base, open_axes, save


def render() -> None:
    apply_base()
    rng = np.random.default_rng(2)

    x = np.linspace(0, 10, 60)
    y = 0.8 * x + rng.normal(0, 1.1, size=x.size)

    fig, ax = plt.subplots(figsize=(6.4, 4.4))
    ax.scatter(
        x, y,
        s=28, color="#2c3e50", alpha=0.55,
        edgecolors="none",
    )

    # 8 bootstrap resamples with replacement.
    n_boot = 8
    x_grid = np.linspace(x.min(), x.max(), 50)
    for i in range(n_boot):
        idx = rng.integers(0, x.size, size=x.size)
        slope_b, intercept_b = np.polyfit(x[idx], y[idx], 1)
        ax.plot(x_grid, slope_b * x_grid + intercept_b,
                color="#7f8c8d", alpha=0.55, linewidth=1.2,
                label="bootstrap fits" if i == 0 else None)

    slope, intercept = np.polyfit(x, y, 1)
    ax.plot(x_grid, slope * x_grid + intercept,
            color=PRIMARY_BLUE, linewidth=2.6, label="mean fit")

    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.legend(loc="upper left")
    open_axes(ax)
    save(fig, "uncertainty", "hop_demo")


if __name__ == "__main__":
    render()
