"""Somewhat better, but still imbalanced labels (Wilke fig 24.2 — ugly)."""

from __future__ import annotations

import matplotlib.pyplot as plt

from cwilke import data as D
from cwilke.theme import OKABE_ITO, apply_base, grid, save, stamp_ugly


SPORTS = ["field", "water polo", "basketball", "swimming", "track"]


def _build(ax, df, *, font_sz, marker_sz):
    palette = {sp: OKABE_ITO[i + 1] for i, sp in enumerate(SPORTS)}
    markers = ["o", "s", "D", "^", "v"]
    marker_map = {sp: mk for sp, mk in zip(SPORTS, markers)}
    for sp in SPORTS:
        sub = df[df["sport"] == sp]
        ax.scatter(sub["height"], sub["pcBfat"], s=marker_sz,
                   color=palette[sp], marker=marker_map[sp],
                   edgecolor="white", linewidth=0.6, alpha=0.95,
                   label=sp)
    ax.set_xlim(169, 210)
    ax.set_ylim(5, 20)
    ax.set_xlabel("height (cm)", fontsize=font_sz)
    ax.set_ylabel("% body fat", fontsize=font_sz)
    ax.tick_params(axis="both", labelsize=font_sz)
    ax.legend(fontsize=font_sz, title="sport",
              title_fontsize=font_sz, frameon=False)
    grid(ax)


def render() -> None:
    apply_base()
    df = D.aus_athletes()
    df = df[df["sex"] == "m"].copy()
    df["sport"] = df["sport"].str.replace("track.*", "track", regex=True)
    df = df[df["sport"].isin(SPORTS)]

    fig, ax = plt.subplots(figsize=(7.2, 4.6))
    _build(ax, df, font_sz=9, marker_sz=22)
    stamp_ugly(fig)
    fig.tight_layout()
    save(fig, "small_axis_labels", "aus_athletes_small_ugly")


if __name__ == "__main__":
    render()
