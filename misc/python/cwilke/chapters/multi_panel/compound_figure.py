"""Compound figure: line chart on top, boxplot + histogram on bottom
(Wilke ch. 21)."""

from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import gridspec

from cwilke import data as D
from cwilke.theme import (BAD, MUTED, PRIMARY_BLUE, PRIMARY_ORANGE,
                           apply_base, hgrid, open_axes, save)


def _running_mean(y: np.ndarray, window: int = 31) -> np.ndarray:
    n = len(y)
    out = np.empty(n)
    half = window // 2
    for i in range(n):
        lo = max(0, i - half)
        hi = min(n, i + half + 1)
        out[i] = y[lo:hi].mean()
    return out


def render() -> None:
    apply_base()

    fig = plt.figure(figsize=(10.0, 6.2))
    gs = gridspec.GridSpec(2, 2, height_ratios=[1.2, 1.0],
                            hspace=0.45, wspace=0.25)

    # --- top row: lincoln temps raw + smooth ------------------------------
    ax_top = fig.add_subplot(gs[0, :])
    df = D.lincoln_temps()
    x = df["day"].values
    y = df["mean_temp_F"].values
    smooth = _running_mean(y, window=31)
    ax_top.scatter(x, y, s=10, color=MUTED, alpha=0.6,
                   edgecolors="none", label="daily mean")
    ax_top.plot(x, smooth, color=BAD, linewidth=2.2, label="smoothed")
    ax_top.set_xlabel("day of the year")
    ax_top.set_ylabel("mean temp (°F)")
    ax_top.set_title("a. Lincoln, NE — daily mean temperature")
    ax_top.legend(loc="lower center", ncol=2)
    open_axes(ax_top)

    # --- bottom left: mpg by cyl boxplot ---------------------------------
    ax_bl = fig.add_subplot(gs[1, 0])
    cars = D.mtcars()
    cyls = sorted(cars["cyl"].unique())
    groups = [cars.loc[cars["cyl"] == c, "mpg"].values for c in cyls]
    bp = ax_bl.boxplot(groups, patch_artist=True,
                        medianprops=dict(color="#2c3e50", linewidth=1.5),
                        boxprops=dict(edgecolor="#2c3e50", linewidth=1.0),
                        whiskerprops=dict(color="#2c3e50", linewidth=1.0),
                        capprops=dict(color="#2c3e50", linewidth=1.0),
                        flierprops=dict(marker="o", markersize=4,
                                        markerfacecolor=MUTED,
                                        markeredgecolor="none"))
    for patch in bp["boxes"]:
        patch.set_facecolor(PRIMARY_BLUE)
        patch.set_alpha(0.8)
    ax_bl.set_xticklabels([str(c) for c in cyls])
    ax_bl.set_xlabel("cylinders")
    ax_bl.set_ylabel("mpg")
    ax_bl.set_title("b. mpg by cylinders")
    hgrid(ax_bl)

    # --- bottom right: titanic age histogram ------------------------------
    ax_br = fig.add_subplot(gs[1, 1])
    tit = D.titanic()
    ax_br.hist(tit["age"].dropna(), bins=24, color=PRIMARY_ORANGE,
               alpha=0.9, edgecolor="white")
    ax_br.set_xlabel("age (years)")
    ax_br.set_ylabel("passengers")
    ax_br.set_title("c. titanic age distribution")
    hgrid(ax_br)

    save(fig, "multi_panel", "compound_figure")


if __name__ == "__main__":
    render()
