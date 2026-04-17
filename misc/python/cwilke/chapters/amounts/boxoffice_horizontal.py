"""Horizontal bar chart: top-5 box-office gross (Wilke fig 6.2)."""

from __future__ import annotations

import matplotlib.pyplot as plt

from cwilke import data as D
from cwilke.theme import PRIMARY_BLUE, apply_base, save, vgrid


def render() -> None:
    apply_base()
    df = D.boxoffice().sort_values("amount")  # smallest at bottom

    fig, ax = plt.subplots(figsize=(7.2, 3.6))
    ax.barh(df["title_short"], df["amount"] / 1e6,
            color=PRIMARY_BLUE, alpha=0.9, height=0.6)
    ax.set_xlabel("weekend gross (million USD)")
    ax.set_xlim(0, 75)
    ax.set_xticks([0, 20, 40, 60])
    vgrid(ax)
    ax.tick_params(axis="y", length=0)
    save(fig, "amounts", "boxoffice_horizontal")


if __name__ == "__main__":
    render()
