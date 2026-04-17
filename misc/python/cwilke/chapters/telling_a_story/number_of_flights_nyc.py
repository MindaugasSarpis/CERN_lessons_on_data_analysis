"""NYC flight count by airline — supporting figure (Wilke fig 29.5)."""

from __future__ import annotations

import matplotlib.pyplot as plt

from cwilke import data as D
from cwilke.theme import apply_base, save, vgrid


HIGHLIGHT = {"Delta", "American"}


def render() -> None:
    apply_base()

    df = D.nyc_airline_delays().sort_values("n")
    colours = ["#BD3828D0" if name in HIGHLIGHT else "#B0B0B0D0"
               for name in df["name"]]

    fig, ax = plt.subplots(figsize=(7.2, 5.4))
    ax.barh(df["name"], df["n"], color=colours,
            edgecolor="white", linewidth=0.4)
    ax.set_xlabel("number of flights")
    vgrid(ax)
    ax.margins(y=0.01)

    fig.tight_layout()
    save(fig, "telling_a_story", "number_of_flights_nyc")


if __name__ == "__main__":
    render()
