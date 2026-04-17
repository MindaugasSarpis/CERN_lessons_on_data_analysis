"""Per-capita CO2 emissions 1970 vs 2010 — paired log-log scatter
(Wilke fig 12.13)."""

from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np

from cwilke import data as D
from cwilke.theme import apply_base, open_axes, save


def render() -> None:
    apply_base()
    df = D.co2_emissions_pairs()

    fig, ax = plt.subplots(figsize=(5.2, 5.0))
    lo, hi = 0.008, 125
    xs = np.array([lo, hi])
    ax.plot(xs, xs, color="#888888", linewidth=1.0, zorder=1)
    ax.scatter(df["y1970"], df["y2010"],
               s=24, facecolors="#0072B2D0",
               edgecolors="white", linewidths=0.4, zorder=2)
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlim(lo, hi)
    ax.set_ylim(lo, hi)
    ax.set_xlabel("1970 CO$_2$ emissions (tons / person)")
    ax.set_ylabel("2010 CO$_2$ emissions (tons / person)")
    ax.set_aspect("equal")
    open_axes(ax)
    save(fig, "associations", "co2_paired_scatter")


if __name__ == "__main__":
    render()
