"""Blue jays 2D PCA illustration — raw, scaled, rotated (Wilke fig 12.10)."""

from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np

from cwilke import data as D
from cwilke.theme import apply_base, grid, save


def render() -> None:
    apply_base()
    df = D.blue_jays()
    colors = {"F": "#D55E00", "M": "#0072B2"}

    fig, axes = plt.subplots(1, 3, figsize=(12.0, 4.2))

    # panel a: raw
    ax = axes[0]
    for s in ("F", "M"):
        sub = df[df["sex"] == s]
        ax.scatter(sub["skull_size_mm"], sub["head_length_mm"],
                   s=22, facecolors=colors[s], edgecolors="white",
                   linewidths=0.4)
    ax.set_xlabel("skull size (mm)")
    ax.set_ylabel("head length (mm)")
    ax.set_title("(a) original data")
    grid(ax)

    # standardise
    skull = df["skull_size_mm"].values
    head = df["head_length_mm"].values
    skull_z = (skull - skull.mean()) / skull.std(ddof=0)
    head_z = (head - head.mean()) / head.std(ddof=0)

    # panel b: scaled with PC axes drawn
    ax = axes[1]
    for s in ("F", "M"):
        mask = df["sex"].values == s
        ax.scatter(skull_z[mask], head_z[mask],
                   s=22, facecolors=colors[s], edgecolors="white",
                   linewidths=0.4)
    # PC1 direction ~ (1,1)/sqrt 2; PC2 perpendicular.
    ax.annotate("", xy=(3, 3), xytext=(-3, -3),
                arrowprops=dict(arrowstyle="-|>", color="black", lw=1.4))
    ax.annotate("", xy=(-2, 2), xytext=(2, -2),
                arrowprops=dict(arrowstyle="-|>", color="black", lw=1.4))
    ax.text(3.1, 3.1, "PC 1", fontsize=11)
    ax.text(-2.2, 2.1, "PC 2", fontsize=11, ha="right")
    ax.set_xlim(-4, 4)
    ax.set_ylim(-4, 4)
    ax.set_xlabel("skull size (scaled)")
    ax.set_ylabel("head length (scaled)")
    ax.set_title("(b) scaled + PC axes")
    ax.set_aspect("equal")
    grid(ax)

    # panel c: rotated into PC coords (PC1 = skull+head, PC2 = head-skull, over √2)
    pc1 = (skull_z + head_z) / np.sqrt(2)
    pc2 = (head_z - skull_z) / np.sqrt(2)
    ax = axes[2]
    for s in ("F", "M"):
        mask = df["sex"].values == s
        ax.scatter(pc1[mask], pc2[mask],
                   s=22, facecolors=colors[s], edgecolors="white",
                   linewidths=0.4)
    ax.axhline(0, color="black", linewidth=0.8)
    ax.axvline(0, color="black", linewidth=0.8)
    ax.set_xlabel("PC 1")
    ax.set_ylabel("PC 2")
    ax.set_title("(c) projected")
    ax.set_aspect("equal")
    grid(ax)

    fig.tight_layout()
    save(fig, "associations", "blue_jays_pca")


if __name__ == "__main__":
    render()
