"""Correlogram tiles for the forensic-glass dataset (Wilke fig 12.6)."""

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

    # Only the strict lower triangle.
    mask = np.tri(n, k=-1, dtype=bool)
    data = np.where(mask, corr, np.nan)

    fig, ax = plt.subplots(figsize=(5.4, 5.0))
    im = ax.imshow(data, cmap="RdBu_r", vmin=-0.8, vmax=0.8,
                   aspect="equal")
    ax.set_xticks(range(n))
    ax.set_yticks(range(n))
    ax.set_xticklabels(cols)
    ax.set_yticklabels(cols)
    ax.tick_params(length=0)
    for spine in ax.spines.values():
        spine.set_visible(False)

    for i in range(n):
        for j in range(n):
            if mask[i, j]:
                v = corr[i, j]
                txt_color = "white" if abs(v) > 0.5 else "#2c3e50"
                ax.text(j, i, f"{v:.2f}", ha="center", va="center",
                        color=txt_color, fontsize=9)

    # minor gridlines between cells
    ax.set_xticks(np.arange(-0.5, n, 1), minor=True)
    ax.set_yticks(np.arange(-0.5, n, 1), minor=True)
    ax.grid(which="minor", color="white", linewidth=1.4)
    ax.tick_params(which="minor", length=0)

    cbar = fig.colorbar(im, ax=ax, shrink=0.7, pad=0.03,
                        orientation="horizontal")
    cbar.set_label("correlation")
    cbar.set_ticks([-0.5, 0, 0.5])
    save(fig, "associations", "forensic_glass_corr")


if __name__ == "__main__":
    render()
