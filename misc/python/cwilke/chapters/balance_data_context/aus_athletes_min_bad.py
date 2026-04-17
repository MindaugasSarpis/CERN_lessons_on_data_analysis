"""Too little ink: faint labels, no grid, no frame — points float (Wilke fig 23.3)."""

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
                   edgecolor="white", linewidth=0.6, alpha=0.95,
                   label=sp)
    faint = "#cfd8dc"
    ax.set_xlim(169, 210)
    ax.set_ylim(5, 20)
    ax.set_xlabel("height (cm)", color=faint)
    ax.set_ylabel("% body fat", color=faint)
    ax.tick_params(colors=faint)
    for sp in ("top", "right", "bottom", "left"):
        ax.spines[sp].set_visible(False)
    leg = ax.legend(loc="upper right", fontsize=9, frameon=False,
                    labelcolor=faint)

    stamp_ugly(fig)
    fig.tight_layout()
    save(fig, "balance_data_context", "aus_athletes_min_bad")


if __name__ == "__main__":
    render()
