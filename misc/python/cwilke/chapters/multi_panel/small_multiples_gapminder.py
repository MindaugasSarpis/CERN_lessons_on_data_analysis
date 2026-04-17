"""Small multiples: one panel per continent (Wilke ch. 21)."""

from __future__ import annotations

import matplotlib.pyplot as plt

from cwilke import data as D
from cwilke.theme import OKABE_ITO, apply_base, open_axes, save


def render() -> None:
    apply_base()

    df = D.gapminder()
    df = df[df["year"] == 2007].copy()

    continents = ["Africa", "Americas", "Asia", "Europe", "Oceania"]
    # ensure a stable order; not every dataset has all 5
    continents = [c for c in continents if c in df["continent"].unique()]

    fig, axes = plt.subplots(2, 3, sharex=True, sharey=True,
                             figsize=(10.0, 5.6))
    axes = axes.flatten()

    for i, cont in enumerate(continents):
        ax = axes[i]
        sub = df[df["continent"] == cont]
        ax.scatter(sub["gdpPercap"], sub["lifeExp"],
                   s=36, color=OKABE_ITO[i + 1], alpha=0.9,
                   edgecolors="white", linewidths=0.6)
        ax.set_title(cont, fontsize=11)
        ax.set_xscale("log")
        open_axes(ax)

    # hide any leftover panels
    for j in range(len(continents), len(axes)):
        axes[j].axis("off")

    # shared labels
    for ax in axes[-3:]:
        if ax.get_visible():
            ax.set_xlabel("GDP per capita (USD, log)")
    for ax in axes[::3]:
        if ax.get_visible():
            ax.set_ylabel("life expectancy")

    fig.tight_layout()
    save(fig, "multi_panel", "small_multiples_gapminder")


if __name__ == "__main__":
    render()
