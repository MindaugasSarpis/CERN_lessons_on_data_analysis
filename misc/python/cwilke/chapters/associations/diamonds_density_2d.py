"""Diamonds carat vs price as 2D hexbin density (Wilke fig 18.4)."""

from __future__ import annotations

import matplotlib.pyplot as plt

from cwilke import data as D
from cwilke.theme import apply_base, open_axes, save


def render() -> None:
    apply_base()
    df = D.diamonds(n=2000)

    fig, ax = plt.subplots(figsize=(6.6, 4.4))
    hb = ax.hexbin(df["carat"], df["price"],
                   gridsize=40, cmap="cividis", mincnt=1)
    ax.set_xlabel("carat")
    ax.set_ylabel("price (USD)")
    cbar = fig.colorbar(hb, ax=ax, pad=0.02)
    cbar.set_label("count")
    open_axes(ax)
    save(fig, "associations", "diamonds_density_2d")


if __name__ == "__main__":
    render()
