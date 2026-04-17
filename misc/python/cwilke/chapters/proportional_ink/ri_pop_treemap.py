"""Treemap of RI county populations (Wilke 17.13).

Uses a simple "squarified"-style layout: biggest block on the left
occupies the full height, then the remaining area is stacked.
"""

from __future__ import annotations

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

from cwilke.data import ri_population
from cwilke.theme import OKABE_ITO, apply_base, save


def render() -> None:
    apply_base()
    df = ri_population().sort_values("pop2010", ascending=False).reset_index(drop=True)
    total = float(df["pop2010"].sum())

    W, H = 1.0, 1.0
    fig, ax = plt.subplots(figsize=(6.2, 4.6))

    colors = [OKABE_ITO[i] for i in (5, 1, 2, 3, 7)]

    # Largest block: full height on the left.
    largest = df.loc[0, "pop2010"]
    w0 = W * (largest / total)
    ax.add_patch(Rectangle((0, 0), w0, H,
                           facecolor=colors[0],
                           edgecolor="white", linewidth=2.5))
    ax.text(w0 / 2, H / 2, f"{df.loc[0, 'county']}\n{largest:,}",
            ha="center", va="center", fontsize=12, color="#2c3e50")

    # Remaining: stack the rest in a column to the right.
    x = w0
    remaining_total = total - largest
    y = 0.0
    for i in range(1, len(df)):
        h = H * (df.loc[i, "pop2010"] / remaining_total)
        ax.add_patch(Rectangle((x, y), W - w0, h,
                               facecolor=colors[i],
                               edgecolor="white", linewidth=2.5))
        label = f"{df.loc[i, 'county']}\n{df.loc[i, 'pop2010']:,}"
        ax.text(x + (W - w0) / 2, y + h / 2, label,
                ha="center", va="center", fontsize=10, color="#2c3e50")
        y += h

    ax.set_xlim(0, W)
    ax.set_ylim(0, H)
    ax.set_aspect("equal")
    ax.axis("off")
    save(fig, "proportional_ink", "ri_pop_treemap")


if __name__ == "__main__":
    render()
