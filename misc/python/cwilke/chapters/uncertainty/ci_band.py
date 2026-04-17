"""Fitted line with 95% CI band (Wilke fig 16.7 concept)."""

from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np

from cwilke.theme import PRIMARY_BLUE, apply_base, open_axes, save


def render() -> None:
    apply_base()
    rng = np.random.default_rng(2)

    x = np.linspace(0, 10, 60)
    y = 0.8 * x + rng.normal(0, 1.1, size=x.size)

    # Ordinary-least-squares fit.
    slope, intercept = np.polyfit(x, y, 1)
    y_hat = slope * x + intercept
    resid = y - y_hat

    n = x.size
    dof = n - 2
    sigma2 = (resid ** 2).sum() / dof
    x_mean = x.mean()
    sxx = ((x - x_mean) ** 2).sum()

    # Pointwise standard error of the mean response.
    x_grid = np.linspace(x.min(), x.max(), 200)
    y_grid = slope * x_grid + intercept
    se = np.sqrt(sigma2 * (1.0 / n + (x_grid - x_mean) ** 2 / sxx))
    # t-multiplier ≈ 2 for reasonable dof; good enough for a teaching figure.
    t_mult = 2.0
    lower = y_grid - t_mult * se
    upper = y_grid + t_mult * se

    fig, ax = plt.subplots(figsize=(6.4, 4.4))
    ax.scatter(
        x, y,
        s=28, color="#2c3e50", alpha=0.55,
        edgecolors="none",
    )
    ax.fill_between(x_grid, lower, upper,
                    color=PRIMARY_BLUE, alpha=0.25, linewidth=0,
                    label="95% CI")
    ax.plot(x_grid, y_grid, color=PRIMARY_BLUE, linewidth=2.2, label="fit")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.legend(loc="upper left")
    open_axes(ax)
    save(fig, "uncertainty", "ci_band")


if __name__ == "__main__":
    render()
