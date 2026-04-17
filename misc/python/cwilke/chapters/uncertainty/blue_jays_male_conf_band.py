"""Linear fit with 95% CI band for male blue jays (Wilke fig 16.15)."""

from __future__ import annotations

import numpy as np
import matplotlib.pyplot as plt

from cwilke.data import blue_jays
from cwilke.theme import apply_base, open_axes, save


def _fit_and_band(x, y, x_grid, level=0.95):
    slope, intercept = np.polyfit(x, y, 1)
    y_hat = slope * x + intercept
    resid = y - y_hat
    n = len(x)
    dof = n - 2
    sigma2 = (resid ** 2).sum() / dof
    x_mean = x.mean()
    sxx = ((x - x_mean) ** 2).sum()
    y_grid = slope * x_grid + intercept
    se = np.sqrt(sigma2 * (1 / n + (x_grid - x_mean) ** 2 / sxx))
    from scipy.stats import t
    crit = t.ppf(0.5 + level / 2, dof)
    return y_grid, y_grid - crit * se, y_grid + crit * se


def render() -> None:
    apply_base()
    df = blue_jays()
    males = df[df["sex"] == "M"]
    x = males["body_mass_g"].values
    y = males["head_length_mm"].values
    x_grid = np.linspace(59, 82, 150)
    y_grid, lo, hi = _fit_and_band(x, y, x_grid, 0.95)

    fig, ax = plt.subplots(figsize=(6.0, 4.2))
    ax.fill_between(x_grid, lo, hi, color="#cccccc", alpha=0.6, linewidth=0)
    ax.scatter(x, y, color="#8a8a8a", s=18, zorder=3)
    ax.plot(x_grid, y_grid, color="#0072B2", linewidth=1.8)
    ax.set_xlim(59, 82)
    ax.set_ylim(52, 61)
    ax.set_xlabel("body mass (g)")
    ax.set_ylabel("head length (mm)")
    open_axes(ax)
    save(fig, "uncertainty", "blue_jays_male_conf_band")


if __name__ == "__main__":
    render()
