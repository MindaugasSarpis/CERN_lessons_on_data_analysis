"""Accent colour: highlight track athletes among male Aus. Institute (Wilke fig 4.5)."""

from __future__ import annotations

import matplotlib.pyplot as plt

from cwilke import data as D
from cwilke.theme import apply_base, grid, save


MARKERS = {
    "track":      "o",
    "field":      "s",
    "water polo": "^",
    "basketball": "D",
    "swimming":   "v",
}


def render() -> None:
    apply_base()
    df = D.aus_athletes()
    df = df[df["sex"] == "m"].copy()
    df["sport"] = df["sport"].replace(
        {"track (400m)": "track", "track (sprint)": "track"}
    )
    df = df[df["sport"].isin(MARKERS.keys())]

    fig, ax = plt.subplots(figsize=(6.6, 4.6))

    # non-highlighted first (grey)
    for sport, marker in MARKERS.items():
        if sport == "track":
            continue
        sub = df[df["sport"] == sport]
        ax.scatter(sub["height"], sub["pcBfat"],
                   s=42, marker=marker,
                   facecolor="#80808080", edgecolor="#808080",
                   linewidth=0.6, label=sport)
    # highlighted (red)
    sub = df[df["sport"] == "track"]
    ax.scatter(sub["height"], sub["pcBfat"],
               s=52, marker="o",
               facecolor="#BD3828D0", edgecolor="#BD3828",
               linewidth=0.8, label="track")

    ax.set_xlabel("height (cm)")
    ax.set_ylabel("% body fat")
    ax.legend(loc="upper left", fontsize=9, frameon=False, ncol=2)
    grid(ax)

    fig.tight_layout()
    save(fig, "color", "aus_athletes_track")


if __name__ == "__main__":
    render()
