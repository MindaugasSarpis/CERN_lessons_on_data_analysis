"""Balance of data ink vs context ink (Wilke ch. 23).

Left: a busy version of a scatter — full gridlines, all four spines,
heavy ticks. Right: minimal — only a horizontal grid, clean axes,
lighter marks. The data is identical. Clean wins.
"""

from __future__ import annotations

import matplotlib.pyplot as plt

from cwilke import data as D
from cwilke.theme import OKABE_ITO, PRIMARY_BLUE, apply_base, hgrid, save


def render() -> None:
    apply_base()
    df = D.blue_jays()

    fig, axes = plt.subplots(1, 2, figsize=(11.2, 5.0))

    # ------------------------ Left: busy ------------------------
    ax = axes[0]
    colors = {"M": OKABE_ITO[1], "F": OKABE_ITO[5]}
    for sex in ("M", "F"):
        sub = df[df["sex"] == sex]
        ax.scatter(sub["body_mass_g"], sub["head_length_mm"],
                   s=36, color=colors[sex],
                   edgecolor="#2c3e50", linewidth=0.6,
                   alpha=0.9, label=f"sex = {sex}")
    # Busy chrome
    for spine in ("top", "right", "bottom", "left"):
        ax.spines[spine].set_visible(True)
        ax.spines[spine].set_linewidth(1.2)
    ax.grid(True, which="major", linestyle="-", color="#90a4ae",
            alpha=0.6, linewidth=0.8)
    ax.minorticks_on()
    ax.grid(True, which="minor", linestyle=":", color="#b0bec5",
            alpha=0.5, linewidth=0.5)
    ax.tick_params(axis="both", which="major", length=6, width=1.1)
    ax.tick_params(axis="both", which="minor", length=3, width=0.8)
    ax.set_xlabel("body mass (g)")
    ax.set_ylabel("head length (mm)")
    ax.set_title("busy: full grid, frame, heavy ticks", fontsize=11)
    ax.legend(loc="lower right", fontsize=9)

    # ------------------------ Right: minimal ------------------------
    ax = axes[1]
    for sex in ("M", "F"):
        sub = df[df["sex"] == sex]
        ax.scatter(sub["body_mass_g"], sub["head_length_mm"],
                   s=36, color=colors[sex],
                   edgecolor="white", linewidth=0.5,
                   alpha=0.9, label=f"sex = {sex}")
    ax.set_xlabel("body mass (g)")
    ax.set_ylabel("head length (mm)")
    ax.set_title("minimal: only hgrid, no box", fontsize=11)
    ax.legend(loc="lower right", fontsize=9)
    hgrid(ax)

    # Match ranges so the two panels are visually directly comparable.
    xlim = (min(df["body_mass_g"]) - 2, max(df["body_mass_g"]) + 2)
    ylim = (min(df["head_length_mm"]) - 1, max(df["head_length_mm"]) + 1)
    for a in axes:
        a.set_xlim(*xlim)
        a.set_ylim(*ylim)

    fig.tight_layout()
    save(fig, "balance_data_context", "grid_vs_no_grid")


if __name__ == "__main__":
    render()
