"""Pie chart of RI county populations (Wilke 17.11)."""

from __future__ import annotations

import matplotlib.pyplot as plt

from cwilke.data import ri_population
from cwilke.theme import OKABE_ITO, apply_base, save


def render() -> None:
    apply_base()
    df = ri_population().sort_values("pop2010", ascending=False)
    colors = [OKABE_ITO[i] for i in (5, 1, 2, 3, 7)]

    fig, ax = plt.subplots(figsize=(6.4, 5.0))
    wedges, _ = ax.pie(
        df["pop2010"], labels=None, startangle=90, counterclock=False,
        colors=colors, wedgeprops={"edgecolor": "white", "linewidth": 1.2},
    )
    # Annotate each slice with population inside or just outside.
    import numpy as np

    total = df["pop2010"].sum()
    cum = 0.0
    for v, w, name in zip(df["pop2010"], wedges, df["county"]):
        frac = v / total
        mid = (cum + frac / 2)
        cum += frac
        angle = 90 - 360 * mid  # degrees, clockwise from top
        rad = np.deg2rad(angle)
        # small slices: put labels outside
        r = 0.55 if frac > 0.15 else 1.08
        x, y = r * np.cos(rad), r * np.sin(rad)
        ha = "center" if frac > 0.15 else ("left" if x >= 0 else "right")
        ax.text(x, y, f"{v:,}", ha=ha, va="center",
                fontsize=10, color="#2c3e50")
    ax.legend(wedges, df["county"], loc="center left",
              bbox_to_anchor=(1.0, 0.5), frameon=False, fontsize=10)
    ax.set_aspect("equal")
    save(fig, "proportional_ink", "ri_pop_pie")


if __name__ == "__main__":
    render()
