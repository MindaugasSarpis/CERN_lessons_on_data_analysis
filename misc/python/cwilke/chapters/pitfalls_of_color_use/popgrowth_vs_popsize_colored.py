"""Too many colours: 51 states each its own hue (Wilke fig 19.1, bad)."""

from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np

from cwilke import data as D
from cwilke.theme import apply_base, grid, save, stamp_bad


def render() -> None:
    apply_base()

    df = D.us_popgrowth().sort_values("state").reset_index(drop=True)
    n = len(df)

    # Big rainbow palette mirroring the "too many colours" look
    cmap = plt.get_cmap("hsv")
    colours = [cmap(i / n) for i in range(n)]

    fig, ax = plt.subplots(figsize=(8.2, 5.8))
    for i, (_, row) in enumerate(df.iterrows()):
        ax.scatter(row["pop2000"], row["popgrowth"] * 100,
                   s=58, color=colours[i],
                   edgecolor="white", linewidth=0.4,
                   label=row["state"])

    ax.set_xscale("log")
    ax.set_xlabel("population size in 2000")
    ax.set_ylabel("population growth, 2000 to 2010 (%)")
    grid(ax)

    # Split legend into columns next to the plot
    ax.legend(loc="center left", bbox_to_anchor=(1.02, 0.5),
              ncol=3, fontsize=7, frameon=False,
              handletextpad=0.3, columnspacing=0.8)

    fig.subplots_adjust(left=0.08, right=0.68, top=0.95, bottom=0.10)
    stamp_bad(fig)
    save(fig, "pitfalls_of_color_use", "popgrowth_vs_popsize_colored")


if __name__ == "__main__":
    render()
