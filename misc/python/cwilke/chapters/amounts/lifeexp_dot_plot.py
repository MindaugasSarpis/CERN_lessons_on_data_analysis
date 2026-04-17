"""Dot plot of life expectancies in the Americas, 2007 (Wilke fig 6.10).

Dots are preferable to bars when the quantity of interest does not
naturally start at zero. With bars, the full range (0..81 years) would
dominate visually and drown out the 20-year spread that is the actual
story.
"""

from __future__ import annotations

import matplotlib.pyplot as plt

from cwilke.theme import PRIMARY_BLUE, apply_base, grid, save


# 2007 Gapminder subset: countries of the Americas and their life expectancies.
# Values inlined to avoid depending on the synthetic D.gapminder() output.
_DATA = [
    ("Canada", 80.653), ("Chile", 78.553), ("Costa Rica", 78.782),
    ("Cuba", 78.273), ("Uruguay", 76.384), ("Mexico", 76.195),
    ("Argentina", 75.320), ("United States", 78.242),
    ("Venezuela", 73.747), ("Panama", 75.537), ("Ecuador", 74.994),
    ("Brazil", 72.390), ("Puerto Rico", 78.746),
    ("Jamaica", 72.567), ("Colombia", 72.889), ("Peru", 71.421),
    ("Dominican Republic", 72.235), ("El Salvador", 71.878),
    ("Paraguay", 71.752), ("Guatemala", 70.259),
    ("Nicaragua", 72.899), ("Honduras", 70.198),
    ("Trinidad and Tobago", 69.819), ("Bolivia", 65.554),
    ("Haiti", 60.916),
]


def render() -> None:
    apply_base()

    # Sort ascending so highest life-expectancy country is at the top.
    data = sorted(_DATA, key=lambda x: x[1])
    labels = [r[0] for r in data]
    values = [r[1] for r in data]

    fig, ax = plt.subplots(figsize=(6.6, 7.0))
    y = range(len(data))
    ax.scatter(values, list(y), s=70, color=PRIMARY_BLUE,
               edgecolor="#2c3e50", linewidth=0.6, zorder=3)
    ax.set_yticks(list(y))
    ax.set_yticklabels(labels)
    ax.set_xlabel("life expectancy (years)")
    ax.set_xlim(59, 82)
    grid(ax)
    ax.tick_params(axis="y", length=0)
    fig.tight_layout()
    save(fig, "amounts", "lifeexp_dot_plot")


if __name__ == "__main__":
    render()
