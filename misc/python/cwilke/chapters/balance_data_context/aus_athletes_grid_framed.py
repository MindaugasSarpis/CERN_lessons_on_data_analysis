"""Clean plot with a single thin panel frame to separate legend (Wilke fig 23.4)."""

from __future__ import annotations

import matplotlib.pyplot as plt

from cwilke import data as D
from cwilke.theme import OKABE_ITO, apply_base, grid, save


SPORTS = ["field", "water polo", "basketball", "swimming", "track"]


def render() -> None:
    apply_base()
    df = D.aus_athletes()
    df = df[df["sex"] == "m"].copy()
    df["sport"] = df["sport"].str.replace("track.*", "track", regex=True)
    df = df[df["sport"].isin(SPORTS)]

    palette = {sp: OKABE_ITO[i + 1] for i, sp in enumerate(SPORTS)}
    markers = ["o", "s", "D", "^", "v"]
    marker_map = {sp: mk for sp, mk in zip(SPORTS, markers)}

    fig, ax = plt.subplots(figsize=(7.2, 4.6))
    for sp in SPORTS:
        sub = df[df["sport"] == sp]
        ax.scatter(sub["height"], sub["pcBfat"], s=44,
                   color=palette[sp], marker=marker_map[sp],
                   edgecolor="white", linewidth=0.6, alpha=0.95,
                   label=sp)

    ax.set_xlim(169, 210)
    ax.set_ylim(5, 20)
    ax.set_xlabel("height (cm)")
    ax.set_ylabel("% body fat")
    ax.legend(loc="upper right", fontsize=9, frameon=False)
    grid(ax)
    for sp in ("top", "right", "bottom", "left"):
        ax.spines[sp].set_visible(True)
        ax.spines[sp].set_color("#90a4ae")
        ax.spines[sp].set_linewidth(0.9)

    fig.tight_layout()
    save(fig, "balance_data_context", "aus_athletes_grid_framed")


if __name__ == "__main__":
    render()
