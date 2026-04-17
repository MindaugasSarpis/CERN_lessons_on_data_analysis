"""Blue jays with 2D density contour lines (Wilke fig 18.8)."""

from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np

from cwilke import data as D
from cwilke.theme import apply_base, grid, save


def _kde2d(x, y, xgrid, ygrid, bw=1.0):
    """Tiny Gaussian KDE on a regular grid (no SciPy dependency)."""
    xg, yg = np.meshgrid(xgrid, ygrid)
    density = np.zeros_like(xg, dtype=float)
    for xi, yi in zip(x, y):
        density += np.exp(-((xg - xi) ** 2 + (yg - yi) ** 2) / (2 * bw ** 2))
    return density / (len(x) * 2 * np.pi * bw ** 2)


def render() -> None:
    apply_base()
    df = D.blue_jays()
    x = df["body_mass_g"].values
    y = df["head_length_mm"].values

    xgrid = np.linspace(57, 82, 80)
    ygrid = np.linspace(49, 61, 80)
    density = _kde2d(x, y, xgrid, ygrid, bw=1.3)

    fig, ax = plt.subplots(figsize=(6.4, 4.6))
    ax.contour(xgrid, ygrid, density, levels=6, colors="black",
               linewidths=0.9)
    ax.scatter(x, y, s=18, color="black", alpha=0.35, edgecolors="none")
    ax.set_xlim(57, 82)
    ax.set_ylim(49, 61)
    ax.set_xlabel("body mass (g)")
    ax.set_ylabel("head length (mm)")
    grid(ax)
    save(fig, "overlapping_points", "blue_jays_contour")


if __name__ == "__main__":
    render()
