"""Horizontal bars of RI county populations (Wilke 17.12)."""

from __future__ import annotations

import matplotlib.pyplot as plt

from cwilke.data import ri_population
from cwilke.theme import OKABE_ITO, apply_base, save, vgrid


def render() -> None:
    apply_base()
    df = ri_population().sort_values("pop2010")
    colors = [OKABE_ITO[i] for i in (7, 3, 2, 1, 5)]  # reversed order

    fig, ax = plt.subplots(figsize=(6.6, 3.8))
    ax.barh(df["county"], df["pop2010"],
            color=colors, edgecolor="#2c3e50", linewidth=0.5, height=0.7)
    ax.set_xlim(0, 700000)
    ax.set_xticks([0, 2e5, 4e5, 6e5])
    ax.set_xticklabels(["0", "200,000", "400,000", "600,000"])
    ax.set_xlabel("number of inhabitants")
    ax.set_ylabel("county")
    vgrid(ax)
    save(fig, "proportional_ink", "ri_pop_bars")


if __name__ == "__main__":
    render()
