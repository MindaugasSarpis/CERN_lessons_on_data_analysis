"""Cleveland dot plot of weekend box-office gross (Wilke fig 6.12).

A dot plot is often preferable to a bar chart for ranked categorical
comparisons: less ink, easier comparison, and the eye is drawn to the
position of each dot rather than a bar endpoint.
"""

from __future__ import annotations

import matplotlib.pyplot as plt

from cwilke import data as D
from cwilke.theme import MUTED, PRIMARY_BLUE, apply_base, save, vgrid


def render() -> None:
    apply_base()
    df = D.boxoffice().sort_values("amount")  # smallest at bottom

    fig, ax = plt.subplots(figsize=(7.2, 3.6))
    y = range(len(df))
    values = df["amount"].values / 1e6

    # Horizontal reference segments from 0 to each dot
    for yi, xi in zip(y, values):
        ax.hlines(yi, 0, xi, color=MUTED, alpha=0.4, linewidth=1.0, zorder=1)

    ax.scatter(values, list(y), s=110, color=PRIMARY_BLUE,
               edgecolor="#2c3e50", linewidth=0.8, zorder=3)

    ax.set_yticks(list(y))
    ax.set_yticklabels(df["title_short"].tolist())
    ax.set_xlabel("weekend gross (million USD)")
    ax.set_xlim(0, 75)
    ax.set_xticks([0, 20, 40, 60])
    vgrid(ax)
    ax.tick_params(axis="y", length=0)
    save(fig, "amounts", "cleveland_dot_plot")


if __name__ == "__main__":
    render()
