"""Diamonds carat vs price — density contours, faceted by cut
(Wilke fig 18.13)."""

from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np

from cwilke import data as D
from cwilke.theme import apply_base, grid, save


CUTS = ["Fair", "Good", "Very Good", "Premium", "Ideal"]


def _kde2d(x, y, xgrid, ygrid, bw=(0.12, 0.15)):
    xg, yg = np.meshgrid(xgrid, ygrid)
    bwx, bwy = bw
    density = np.zeros_like(xg, dtype=float)
    for xi, yi in zip(x, y):
        density += np.exp(
            -((xg - xi) ** 2 / (2 * bwx ** 2)
              + (yg - yi) ** 2 / (2 * bwy ** 2))
        )
    return density / (len(x) * 2 * np.pi * bwx * bwy)


def render() -> None:
    apply_base()
    df = D.diamonds(n=5000)
    df = df[df["carat"] <= 2.3].copy()
    df["log_price"] = np.log10(df["price"].clip(240))

    xgrid = np.linspace(0.05, 2.2, 90)
    ygrid = np.linspace(np.log10(240), np.log10(25000), 90)

    fig, axes = plt.subplots(2, 3, figsize=(10.4, 6.0),
                              sharex=True, sharey=True)
    axes_flat = axes.ravel()
    for ax, cut in zip(axes_flat, CUTS):
        sub = df[df["cut"] == cut]
        d = _kde2d(sub["carat"].values, sub["log_price"].values,
                   xgrid, ygrid)
        ax.contourf(xgrid, ygrid, d, levels=5,
                    colors=["#eef5fb", "#c8e0ef", "#9ec8e1",
                            "#6aa7cd", "#3680b2", "#1760a1"])
        ax.contour(xgrid, ygrid, d, levels=5,
                   colors="#084c80", linewidths=0.4)
        ax.set_title(cut.lower())
        ax.set_xlim(0.05, 2.2)
        ax.set_ylim(np.log10(240), np.log10(25000))
        # Pretty price ticks.
        ax.set_yticks([np.log10(300), np.log10(1000),
                       np.log10(3000), np.log10(10000)])
        ax.set_yticklabels(["$300", "$1,000", "$3,000", "$10,000"])
        grid(ax)
    # Hide the unused 6th axis.
    axes_flat[-1].set_visible(False)

    for ax in axes[1, :]:
        ax.set_xlabel("carat")
    for ax in axes[:, 0]:
        ax.set_ylabel("price (USD)")

    fig.tight_layout()
    save(fig, "overlapping_points", "diamonds_contour_facets")


if __name__ == "__main__":
    render()
