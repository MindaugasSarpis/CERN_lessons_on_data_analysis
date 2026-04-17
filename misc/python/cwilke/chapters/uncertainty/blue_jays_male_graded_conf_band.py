"""80%/95%/99% confidence bands stacked on a linear fit (Wilke fig 16.17)."""

from __future__ import annotations

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import t as student_t

from cwilke.data import blue_jays
from cwilke.theme import apply_base, open_axes, save


def render() -> None:
    apply_base()
    df = blue_jays()
    males = df[df["sex"] == "M"]
    x = males["body_mass_g"].values
    y = males["head_length_mm"].values

    slope, intercept = np.polyfit(x, y, 1)
    n = len(x)
    dof = n - 2
    y_hat = slope * x + intercept
    sigma2 = ((y - y_hat) ** 2).sum() / dof
    x_mean = x.mean()
    sxx = ((x - x_mean) ** 2).sum()

    x_grid = np.linspace(59, 82, 150)
    y_grid = slope * x_grid + intercept
    se = np.sqrt(sigma2 * (1 / n + (x_grid - x_mean) ** 2 / sxx))

    levels = [
        ("99%", 0.99, "#dceaf5"),
        ("95%", 0.95, "#a8cbe6"),
        ("80%", 0.80, "#5f92bf"),
    ]

    fig, ax = plt.subplots(figsize=(6.0, 4.2))
    for name, lev, col in levels:
        crit = student_t.ppf(0.5 + lev / 2, dof)
        ax.fill_between(x_grid, y_grid - crit * se, y_grid + crit * se,
                         color=col, linewidth=0, label=name)
    ax.scatter(x, y, color="#555555", s=18, zorder=3)
    ax.plot(x_grid, y_grid, color="#0f4c75", linewidth=1.6)
    ax.set_xlim(59, 82)
    ax.set_ylim(52, 61)
    ax.set_xlabel("body mass (g)")
    ax.set_ylabel("head length (mm)")
    ax.legend(title="confidence level", loc="lower right", frameon=False,
              ncol=3)
    open_axes(ax)
    save(fig, "uncertainty", "blue_jays_male_graded_conf_band")


if __name__ == "__main__":
    render()
