"""Equally likely draw lines within the CI band (Wilke fig 16.16)."""

from __future__ import annotations

import numpy as np
import matplotlib.pyplot as plt

from cwilke.data import blue_jays
from cwilke.theme import apply_base, open_axes, save


def render() -> None:
    apply_base()
    df = blue_jays()
    males = df[df["sex"] == "M"]
    x = males["body_mass_g"].values
    y = males["head_length_mm"].values

    # OLS
    slope, intercept = np.polyfit(x, y, 1)
    n = len(x)
    dof = n - 2
    y_hat = slope * x + intercept
    sigma2 = ((y - y_hat) ** 2).sum() / dof
    x_mean = x.mean()
    sxx = ((x - x_mean) ** 2).sum()
    # Covariance of (intercept, slope)
    var_slope = sigma2 / sxx
    var_int = sigma2 * (1 / n + x_mean ** 2 / sxx)
    cov_is = -sigma2 * x_mean / sxx
    cov = np.array([[var_int, cov_is], [cov_is, var_slope]])

    rng = np.random.default_rng(7)
    draws = rng.multivariate_normal([intercept, slope], cov, size=15)

    x_grid = np.linspace(59, 82, 100)

    # Confidence band for context
    from scipy.stats import t
    crit = t.ppf(0.975, dof)
    se = np.sqrt(sigma2 * (1 / n + (x_grid - x_mean) ** 2 / sxx))
    y_grid = slope * x_grid + intercept

    fig, ax = plt.subplots(figsize=(6.0, 4.2))
    ax.fill_between(x_grid, y_grid - crit * se, y_grid + crit * se,
                     color="#cccccc", alpha=0.5, linewidth=0)
    ax.scatter(x, y, color="#8a8a8a", s=18, zorder=3)
    for b0, b1 in draws:
        ax.plot(x_grid, b0 + b1 * x_grid, color="#0072B2",
                linewidth=0.4, alpha=0.85)
    ax.set_xlim(59, 82)
    ax.set_ylim(52, 61)
    ax.set_xlabel("body mass (g)")
    ax.set_ylabel("head length (mm)")
    open_axes(ax)
    save(fig, "uncertainty", "blue_jays_male_fitted_draws")


if __name__ == "__main__":
    render()
