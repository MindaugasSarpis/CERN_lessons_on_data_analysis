"""Rwandan parliament gender composition over time (Wilke fig 10.7).

Time-series stacked bars — the rare case where stacking really works,
because there are only two segments per bar. Dashed line at 50% helps
the reader pinpoint when the majority flipped.
"""

from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np

from cwilke import data as D
from cwilke.theme import apply_base, save


WOMEN = "#D55E00"
MEN = "#0072B2"


def render() -> None:
    apply_base()
    df = D.women_parliament_rwanda()
    years = df["year"].values
    women = df["perc_women"].values
    men = 100 - women

    fig, ax = plt.subplots(figsize=(8.2, 4.2))
    ax.bar(years, men, width=1, color=MEN, alpha=0.85,
           edgecolor="white", linewidth=0.8, label="men")
    ax.bar(years, women, width=1, bottom=men, color=WOMEN, alpha=0.85,
           edgecolor="white", linewidth=0.8, label="women")

    ax.axhline(50, color="black", linewidth=1.0, linestyle="--")
    ax.set_ylim(0, 100)
    ax.set_xlim(years.min() - 0.5, years.max() + 0.5)
    ax.set_ylabel("relative proportion (%)")
    ax.set_xticks(np.arange(years.min(), years.max() + 1, 2))

    # Labels at the right edge.
    final_men = men[-1]
    final_women = women[-1]
    ax.text(years.max() + 0.7, final_men / 2, "men",
            color=MEN, va="center", fontweight="bold")
    ax.text(years.max() + 0.7, final_men + final_women / 2, "women",
            color=WOMEN, va="center", fontweight="bold")

    for sp in ("top", "right"):
        ax.spines[sp].set_visible(False)
    fig.tight_layout()
    save(fig, "proportions", "women_parliament_stacked")


if __name__ == "__main__":
    render()
