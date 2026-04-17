"""Blue jays — contour lines separated by sex (Wilke fig 18.10)."""

from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np

from cwilke import data as D
from cwilke.theme import apply_base, grid, save


def _kde2d(x, y, xgrid, ygrid, bw=1.0):
    xg, yg = np.meshgrid(xgrid, ygrid)
    density = np.zeros_like(xg, dtype=float)
    for xi, yi in zip(x, y):
        density += np.exp(-((xg - xi) ** 2 + (yg - yi) ** 2) / (2 * bw ** 2))
    return density / (len(x) * 2 * np.pi * bw ** 2)


def render() -> None:
    apply_base()
    df = D.blue_jays()
    xgrid = np.linspace(57, 82, 80)
    ygrid = np.linspace(49, 61, 80)
    colors = {"F": "#D55E00", "M": "#0072B2"}
    labels = {"F": "female birds", "M": "male birds"}

    fig, ax = plt.subplots(figsize=(6.4, 4.6))
    for s in ("F", "M"):
        sub = df[df["sex"] == s]
        d = _kde2d(sub["body_mass_g"].values, sub["head_length_mm"].values,
                   xgrid, ygrid, bw=1.2)
        ax.contour(xgrid, ygrid, d, levels=5, colors=colors[s],
                   linewidths=1.0)
        ax.scatter(sub["body_mass_g"], sub["head_length_mm"],
                   s=16, color=colors[s], alpha=0.7, edgecolors="none",
                   label=labels[s])
    ax.set_xlim(57, 82)
    ax.set_ylim(49, 61)
    ax.set_xlabel("body mass (g)")
    ax.set_ylabel("head length (mm)")
    ax.legend(loc="lower right", frameon=False)
    grid(ax)
    save(fig, "overlapping_points", "blue_jays_contour_by_sex")


if __name__ == "__main__":
    render()
