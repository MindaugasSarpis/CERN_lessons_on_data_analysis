"""Rainbow-colored state bars: loud, ordered-looking, no added info (Wilke fig 19.3)."""

from __future__ import annotations

import matplotlib.pyplot as plt

from cwilke import data as D
from cwilke.theme import apply_base, save, stamp_ugly, vgrid


def render() -> None:
    apply_base()

    df = D.us_popgrowth().sort_values("popgrowth").reset_index(drop=True)
    n = len(df)

    cmap = plt.get_cmap("hsv")
    colours = [cmap(i / n) for i in range(n)]

    fig, ax = plt.subplots(figsize=(6.2, 9.5))
    ax.barh(range(n), df["popgrowth"].values * 100,
            color=colours, edgecolor="white", linewidth=0.4)
    ax.set_yticks(range(n))
    ax.set_yticklabels(df["state"].values, fontsize=9)
    ax.set_xlabel("population growth, 2000 to 2010 (%)")
    ax.set_xlim(-2, 37.5)
    ax.axvline(0, color="#2c3e50", linewidth=0.6)
    vgrid(ax)
    ax.margins(y=0.008)

    fig.tight_layout()
    stamp_ugly(fig)
    save(fig, "pitfalls_of_color_use", "popgrowth_rainbow")


if __name__ == "__main__":
    render()
