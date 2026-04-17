"""Blue jays pairs/scatterplot-matrix (Wilke fig 12.4)."""

from __future__ import annotations

import matplotlib.pyplot as plt

from cwilke import data as D
from cwilke.theme import apply_base, grid, save


def render() -> None:
    apply_base()
    df = D.blue_jays()

    cols = [("head_length_mm", "head length (mm)"),
            ("body_mass_g",   "body mass (g)"),
            ("skull_size_mm", "skull size (mm)")]
    n = len(cols)
    colors = {"F": "#D55E00", "M": "#0072B2"}

    fig, axes = plt.subplots(n, n, figsize=(7.6, 6.8))
    for i, (yc, ylab) in enumerate(cols):
        for j, (xc, xlab) in enumerate(cols):
            ax = axes[i, j]
            if i == j:
                # diagonal: mini histogram
                for s in ("F", "M"):
                    sub = df[df["sex"] == s]
                    ax.hist(sub[xc], bins=15, alpha=0.6,
                            color=colors[s], edgecolor="white",
                            linewidth=0.4)
                ax.set_yticks([])
            else:
                for s in ("F", "M"):
                    sub = df[df["sex"] == s]
                    ax.scatter(sub[xc], sub[yc],
                               s=14, facecolors=colors[s] + "D0",
                               edgecolors="white", linewidths=0.3)
                grid(ax)
            if i == n - 1:
                ax.set_xlabel(xlab)
            if j == 0:
                ax.set_ylabel(ylab)
            ax.tick_params(labelsize=9)

    # legend on top
    for lbl, col in [("female birds", colors["F"]), ("male birds", colors["M"])]:
        axes[0, -1].scatter([], [], s=24, facecolors=col + "D0",
                            edgecolors="white", linewidths=0.3, label=lbl)
    axes[0, -1].legend(loc="upper right", frameon=False, fontsize=9)

    fig.tight_layout()
    save(fig, "associations", "blue_jays_scatter_matrix")


if __name__ == "__main__":
    render()
