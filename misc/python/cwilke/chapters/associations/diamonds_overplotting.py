"""Diamonds carat vs price showing overplotting (Wilke fig 18 context)."""

from __future__ import annotations

import matplotlib.pyplot as plt

from cwilke import data as D
from cwilke.theme import PRIMARY_BLUE, apply_base, open_axes, save


def render() -> None:
    apply_base()
    df = D.diamonds(n=2000)

    fig, ax = plt.subplots(figsize=(6.4, 4.4))
    ax.scatter(df["carat"], df["price"],
               s=18, color=PRIMARY_BLUE,
               edgecolors="none")
    ax.set_xlabel("carat")
    ax.set_ylabel("price (USD)")
    open_axes(ax)
    save(fig, "associations", "diamonds_overplotting")


if __name__ == "__main__":
    render()
