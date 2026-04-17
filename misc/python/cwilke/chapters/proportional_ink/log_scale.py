"""Gapminder 2007: GDP per capita (log) vs. life expectancy (Wilke fig 17.5)."""

from __future__ import annotations

import matplotlib.pyplot as plt

from cwilke import data as D
from cwilke.theme import OKABE_ITO, apply_base, open_axes, save


def render() -> None:
    apply_base()
    df = D.gapminder()
    df_year = df[df["year"] == 2007]

    continents = sorted(df_year["continent"].unique())
    # Skip black (index 0); categorical continents get distinct hues.
    palette = {c: OKABE_ITO[1 + i] for i, c in enumerate(continents)}

    fig, ax = plt.subplots(figsize=(7.2, 4.6))
    for continent in continents:
        sub = df_year[df_year["continent"] == continent]
        ax.scatter(
            sub["gdpPercap"], sub["lifeExp"],
            s=60, color=palette[continent], alpha=0.85,
            edgecolors="#2c3e50", linewidths=0.5,
            label=continent,
        )

    ax.set_xscale("log")
    ax.set_xlabel("GDP per capita (USD, log scale)")
    ax.set_ylabel("life expectancy (years)")
    ax.legend(loc="lower right", title="continent", fontsize=9)
    open_axes(ax)
    save(fig, "proportional_ink", "log_scale")


if __name__ == "__main__":
    render()
