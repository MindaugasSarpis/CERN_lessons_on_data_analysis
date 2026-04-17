"""Iris scatter with a rainbow (bad) vs. Okabe-Ito (good) palette (Wilke fig 19.1)."""

from __future__ import annotations

import matplotlib.pyplot as plt

from cwilke import data as D
from cwilke.theme import OKABE_ITO, apply_base, open_axes, save


def render() -> None:
    apply_base()
    df = D.iris()
    species = sorted(df["species"].unique())

    # Rainbow/hsv sampled at three equally-spaced points — the classic "bad" choice.
    rainbow_cmap = plt.get_cmap("hsv")
    rainbow_colors = [rainbow_cmap(i / len(species)) for i in range(len(species))]
    # Start Okabe-Ito at the orange entry (skip black for categorical data).
    okabe_colors = OKABE_ITO[1:1 + len(species)]

    fig, axes = plt.subplots(1, 2, figsize=(10, 4))

    for ax, palette, title in (
        (axes[0], rainbow_colors, "rainbow (hsv)"),
        (axes[1], okabe_colors, "Okabe-Ito"),
    ):
        for sp, colour in zip(species, palette):
            sub = df[df["species"] == sp]
            ax.scatter(
                sub["sepal_length"], sub["petal_length"],
                s=34, color=colour, alpha=0.8,
                edgecolors="#2c3e50", linewidths=0.4,
                label=sp,
            )
        ax.set_xlabel("sepal length (cm)")
        ax.set_ylabel("petal length (cm)")
        ax.set_title(title)
        ax.legend(loc="lower right", fontsize=9)
        open_axes(ax)

    fig.tight_layout()

    # Stamp only the left (rainbow) panel — figure-coordinate text placed
    # roughly over the centre of the first subplot.
    fig.text(
        0.25, 0.5, "bad",
        ha="center", va="center",
        fontsize=56, color="red", alpha=0.18,
        rotation=30, fontweight="bold",
    )

    save(fig, "color", "colorblind_simulation")


if __name__ == "__main__":
    render()
