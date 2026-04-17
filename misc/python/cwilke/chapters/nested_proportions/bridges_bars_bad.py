"""Bars of mixed, overlapping categories (Wilke fig 11.2, "bad").

Not technically wrong — bars don't imply a sum to 100% — but the
reader has no way to see that "steel" and "modern" aren't disjoint.
Shown alongside the pie and mosaic versions to make the point.
"""

from __future__ import annotations

import matplotlib.pyplot as plt

from cwilke import data as D
from cwilke.theme import apply_base, hgrid, save, stamp_bad


def render() -> None:
    apply_base()
    df = D.bridges()
    n = len(df)

    mat_counts = df["material"].value_counts().to_dict()
    era_counts = df["erected"].value_counts().to_dict()

    labels = ["steel", "wood", "iron", "modern", "crafts"]
    values = [mat_counts.get(l, 0) / n * 100 if l in mat_counts
               else era_counts.get(l, 0) / n * 100 for l in labels]
    colors = {
        "iron":   "#D55E00",
        "steel":  "#0072B2",
        "wood":   "#009E73",
        "crafts": "#F0E442",
        "modern": "#56B4E9",
    }

    fig, ax = plt.subplots(figsize=(6.6, 4.0))
    ax.bar(labels, values, color=[colors[l] for l in labels], alpha=0.9)
    ax.set_ylabel("proportion of bridges (%)")
    ax.set_ylim(0, 70)
    hgrid(ax)
    ax.tick_params(axis="x", length=0)
    stamp_bad(fig)
    fig.tight_layout()
    save(fig, "nested_proportions", "bridges_bars_bad")


if __name__ == "__main__":
    render()
