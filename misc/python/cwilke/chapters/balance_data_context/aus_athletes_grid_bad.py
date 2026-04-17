"""Too much non-data ink: frame, dense minor grid, boxed legend (Wilke fig 23.1)."""

from __future__ import annotations

import matplotlib.pyplot as plt

from cwilke import data as D
from cwilke.theme import OKABE_ITO, apply_base, save, stamp_ugly


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
                   edgecolor="#2c3e50", linewidth=0.7, alpha=0.9,
                   label=sp)

    # Busy chrome: all four spines, thick, dense grid
    for sp in ("top", "right", "bottom", "left"):
        ax.spines[sp].set_visible(True)
        ax.spines[sp].set_linewidth(1.3)
    ax.grid(True, which="major", linestyle="-", color="black",
            linewidth=0.5, alpha=0.6)
    ax.minorticks_on()
    ax.grid(True, which="minor", linestyle=":", color="black",
            linewidth=0.3, alpha=0.35)

    ax.set_xlim(169, 210)
    ax.set_ylim(5, 20)
    ax.set_xlabel("height (cm)")
    ax.set_ylabel("% body fat")

    leg = ax.legend(loc="upper right", fontsize=9, frameon=True,
                    edgecolor="black")
    leg.get_frame().set_linewidth(1.0)

    # Big outer frame around the whole figure
    fig.patch.set_edgecolor("black")
    fig.patch.set_linewidth(2)

    stamp_ugly(fig)
    fig.tight_layout()
    save(fig, "balance_data_context", "aus_athletes_grid_bad")


if __name__ == "__main__":
    render()
