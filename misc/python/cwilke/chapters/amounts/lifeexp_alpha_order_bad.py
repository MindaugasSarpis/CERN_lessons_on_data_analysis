"""Dot plot ordered alphabetically — a Wilke "bad" example (fig 6.13).

Even a dot plot can fail when the category order carries no meaning.
Alphabetical order yields a noisy cloud that hides the real pattern;
prefer ordering the categories by their data values.
"""

from __future__ import annotations

import matplotlib.pyplot as plt

from cwilke.theme import PRIMARY_BLUE, apply_base, grid, save, stamp_bad


from cwilke.chapters.amounts.lifeexp_dot_plot import _DATA


def render() -> None:
    apply_base()

    # Alphabetical order (the wrong choice here).
    data = sorted(_DATA, key=lambda x: x[0].lower(), reverse=True)
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
    stamp_bad(fig)
    fig.tight_layout()
    save(fig, "amounts", "lifeexp_alpha_order_bad")


if __name__ == "__main__":
    render()
