"""Fully-labelled bubble scatter: body mass × head length × skull (Wilke fig 30.3)."""

from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np

from cwilke import data as D
from cwilke.theme import apply_base, grid, save


SEX_COLOURS = {"F": "#D55E00", "M": "#0072B2"}
SEX_LABELS = {"F": "female", "M": "male"}


def render() -> None:
    apply_base()

    df = D.blue_jays()

    fig, ax = plt.subplots(figsize=(7.0, 5.4))
    for sex, col in SEX_COLOURS.items():
        sub = df[df["sex"] == sex]
        # scale skull size to bubble area (2–7 pt radius)
        s_min, s_max = 28, 34
        r = np.interp(sub["skull_size_mm"], (s_min, s_max), (2, 7))
        sizes = np.pi * (r ** 2) * 3
        ax.scatter(sub["body_mass_g"], sub["head_length_mm"],
                   s=sizes, facecolor=col,
                   edgecolor="white", linewidth=0.8, alpha=0.8,
                   label=SEX_LABELS[sex])

    ax.set_xlabel("body mass (g)")
    ax.set_ylabel("head length (mm)")

    # custom "skull size" marker-size legend
    from matplotlib.lines import Line2D
    size_handles = []
    for sk in (28, 30, 32, 34):
        r = np.interp(sk, (28, 34), (2, 7))
        size_handles.append(Line2D(
            [], [], marker="o", linestyle="None",
            markerfacecolor="#2c3e50", markeredgecolor="none",
            markersize=r * 2, label=f"{sk}",
        ))
    sex_legend = ax.legend(title="sex", loc="upper left", fontsize=10)
    ax.add_artist(sex_legend)
    ax.legend(handles=size_handles, title="skull size (mm)",
              loc="lower right", fontsize=10,
              labelspacing=1.3, borderpad=0.8)

    grid(ax)
    fig.tight_layout()
    save(fig, "figure_titles_captions", "blue_jays_scatter_bubbles2")


if __name__ == "__main__":
    render()
