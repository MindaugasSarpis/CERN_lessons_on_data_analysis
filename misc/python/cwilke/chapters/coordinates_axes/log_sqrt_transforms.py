"""Linear vs log x-axis on gapminder 2007 (Wilke ch. 3)."""

from __future__ import annotations

import matplotlib.pyplot as plt

from cwilke import data as D
from cwilke.theme import OKABE_ITO, apply_base, open_axes, save


def render() -> None:
    apply_base()

    df = D.gapminder()
    df = df[df["year"] == 2007].copy()

    continents = sorted(df["continent"].unique())
    palette = {c: OKABE_ITO[i + 1] for i, c in enumerate(continents)}
    colors = df["continent"].map(palette).values

    fig, axes = plt.subplots(1, 2, figsize=(10.0, 4.2))

    for ax in axes:
        ax.scatter(df["gdpPercap"], df["lifeExp"],
                   c=colors, s=40, alpha=0.85, edgecolors="white",
                   linewidths=0.6)
        ax.set_xlabel("GDP per capita (USD)")
        ax.set_ylabel("life expectancy (years)")
        open_axes(ax)

    axes[0].set_title("linear x")
    axes[1].set_title("log x")
    axes[1].set_xscale("log")

    # one shared legend
    handles = [plt.Line2D([0], [0], marker="o", linestyle="",
                          markerfacecolor=palette[c], markeredgecolor="white",
                          markersize=8, label=c)
               for c in continents]
    axes[1].legend(handles=handles, loc="lower right", fontsize=9)

    fig.tight_layout()
    save(fig, "coordinates_axes", "log_sqrt_transforms")


if __name__ == "__main__":
    render()
