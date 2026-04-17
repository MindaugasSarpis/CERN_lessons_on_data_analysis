"""Vertical bar chart: top-5 box-office gross (Wilke fig 6.1)."""

from __future__ import annotations

import matplotlib.pyplot as plt

from cwilke import data as D
from cwilke.theme import PRIMARY_BLUE, apply_base, hgrid, save


def render() -> None:
    apply_base()
    df = D.boxoffice().sort_values("amount", ascending=False)

    fig, ax = plt.subplots(figsize=(7.2, 4.2))
    ax.bar(df["title_short"], df["amount"] / 1e6,
           color=PRIMARY_BLUE, alpha=0.9, width=0.65)
    ax.set_ylabel("weekend gross (million USD)")
    ax.set_ylim(0, 75)
    ax.set_yticks([0, 20, 40, 60])
    hgrid(ax)
    ax.tick_params(axis="x", length=0)
    for label in ax.get_xticklabels():
        label.set_rotation(25)
        label.set_ha("right")
    save(fig, "amounts", "boxoffice_vertical")


if __name__ == "__main__":
    render()
