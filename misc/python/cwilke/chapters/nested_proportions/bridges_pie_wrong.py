"""Combining two overlapping breakdowns in one pie (Wilke fig 11.1).

Plotting "material" + "era" in a single pie double-counts every bridge,
so the slices sum to more than 100%. A dramatic warning about mixing
overlapping categorical variables.
"""

from __future__ import annotations

import matplotlib.pyplot as plt

from cwilke import data as D
from cwilke.theme import apply_base, save, stamp_wrong


def render() -> None:
    apply_base()
    df = D.bridges()
    n = len(df)

    # Material counts (iron/steel/wood) — sum to 100%.
    mat_counts = df["material"].value_counts()
    # Era-derived extra slices for "crafts" and "modern" only.
    era_counts = df["erected"].value_counts().loc[["crafts", "modern"]]

    labels = (list(mat_counts.index) + list(era_counts.index))
    values = list(mat_counts.values) + list(era_counts.values)

    colors = {
        "iron":   "#D55E00",
        "steel":  "#0072B2",
        "wood":   "#009E73",
        "crafts": "#F0E442",
        "modern": "#56B4E9",
    }
    color_list = [colors[l] for l in labels]

    fig, ax = plt.subplots(figsize=(6.2, 5.4))
    ax.pie(values, labels=labels, colors=color_list, startangle=90,
           counterclock=False,
           autopct=lambda p: f"{p:.0f}%",
           wedgeprops=dict(edgecolor="white", linewidth=1.2),
           textprops=dict(fontsize=11))
    ax.set_aspect("equal")
    ax.set_title(f"pie slices sum to {sum(values) / n * 100:.0f}% (!!)",
                  fontsize=11, color="#b0242c")
    stamp_wrong(fig)
    fig.tight_layout()
    save(fig, "nested_proportions", "bridges_pie_wrong")


if __name__ == "__main__":
    render()
