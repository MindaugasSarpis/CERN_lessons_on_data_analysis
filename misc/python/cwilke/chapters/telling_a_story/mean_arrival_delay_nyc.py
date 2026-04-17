"""Simple NYC arrival-delay bar: highlight American / Delta (Wilke fig 29.4)."""

from __future__ import annotations

import matplotlib.pyplot as plt

from cwilke import data as D
from cwilke.theme import apply_base, save, vgrid


HIGHLIGHT = {"Delta", "American"}


def render() -> None:
    apply_base()

    df = D.nyc_airline_delays().sort_values("mean_delay", ascending=False)
    colours = ["#BD3828D0" if name in HIGHLIGHT else "#B0B0B0D0"
               for name in df["name"]]

    fig, ax = plt.subplots(figsize=(7.2, 5.4))
    ax.barh(df["name"], df["mean_delay"], color=colours,
            edgecolor="white", linewidth=0.4)
    ax.set_xlabel("mean arrival delay (min.)")
    ax.axvline(0, color="#2c3e50", linewidth=0.6)
    vgrid(ax)
    ax.margins(y=0.01)

    fig.tight_layout()
    save(fig, "telling_a_story", "mean_arrival_delay_nyc")


if __name__ == "__main__":
    render()
