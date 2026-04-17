"""Correlogram with circle size ∝ |r| (Wilke fig 12.7)."""

from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np

from cwilke import data as D
from cwilke.theme import apply_base, save


def render() -> None:
    apply_base()
    df = D.forensic_glass()
    cols = ["Mg", "Ca", "Fe", "K", "Na", "Al", "Ba"]
    corr = df[cols].corr().values
    n = len(cols)

    fig, ax = plt.subplots(figsize=(5.4, 5.0))
    cmap = plt.get_cmap("RdBu_r")
    # Map |r| to circle area (points^2).
    max_area = 700
    for i in range(n):
        for j in range(n):
            if j >= i:
                continue
            v = corr[i, j]
            area = max_area * min(abs(v) / 0.8, 1.0)
            color = cmap((v + 0.8) / 1.6)
            ax.scatter(j, i, s=area, facecolors=color,
                       edgecolors="white", linewidths=0.5)

    ax.set_xticks(range(n))
    ax.set_yticks(range(n))
    ax.set_xticklabels(cols)
    ax.set_yticklabels(cols)
    ax.set_xlim(-0.5, n - 0.5)
    ax.set_ylim(n - 0.5, -0.5)
    ax.set_aspect("equal")
    ax.tick_params(length=0)
    for spine in ax.spines.values():
        spine.set_visible(False)
    ax.grid(True, which="major", color="#e0e0e0", linewidth=0.6)
    ax.set_axisbelow(True)

    sm = plt.cm.ScalarMappable(cmap=cmap,
                                norm=plt.Normalize(vmin=-0.8, vmax=0.8))
    cbar = fig.colorbar(sm, ax=ax, shrink=0.7, pad=0.03,
                        orientation="horizontal")
    cbar.set_label("correlation")
    cbar.set_ticks([-0.5, 0, 0.5])
    save(fig, "associations", "forensic_glass_corr_circles")


if __name__ == "__main__":
    render()
