"""Correlation heatmap of numeric mtcars columns (Wilke fig 12.8)."""

from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np

from cwilke import data as D
from cwilke.theme import apply_base, save


def render() -> None:
    apply_base()
    df = D.mtcars()
    cols = ["mpg", "cyl", "disp", "hp", "drat", "wt", "qsec"]
    corr = df[cols].corr().values
    n = len(cols)

    fig, ax = plt.subplots(figsize=(6.2, 5.4))
    im = ax.imshow(corr, cmap="RdBu_r", vmin=-1, vmax=1, aspect="equal")

    ax.set_xticks(range(n))
    ax.set_yticks(range(n))
    ax.set_xticklabels(cols)
    ax.set_yticklabels(cols)
    ax.tick_params(axis="x", length=0)
    ax.tick_params(axis="y", length=0)
    for spine in ax.spines.values():
        spine.set_visible(False)

    # annotate cells
    for i in range(n):
        for j in range(n):
            val = corr[i, j]
            txt_color = "white" if abs(val) > 0.55 else "#2c3e50"
            ax.text(j, i, f"{val:.2f}", ha="center", va="center",
                    color=txt_color, fontsize=10)

    cbar = fig.colorbar(im, ax=ax, shrink=0.82, pad=0.03)
    cbar.set_label("correlation")
    cbar.set_ticks([-1, -0.5, 0, 0.5, 1])
    # minor gridlines between cells
    ax.set_xticks(np.arange(-0.5, n, 1), minor=True)
    ax.set_yticks(np.arange(-0.5, n, 1), minor=True)
    ax.grid(which="minor", color="white", linewidth=1.5)
    ax.tick_params(which="minor", length=0)

    save(fig, "associations", "mtcars_corr_heatmap")


if __name__ == "__main__":
    render()
