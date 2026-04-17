"""Histogram drawn as empty outlined bars — confusing (Wilke fig 22.1)."""

from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np

from cwilke import data as D
from cwilke.theme import apply_base, hgrid, save, stamp_bad


def render() -> None:
    apply_base()
    df = D.titanic_all()

    bins = np.arange(0, 76, 3)
    fig, ax = plt.subplots(figsize=(7.2, 4.2))
    ax.hist(df["age"], bins=bins, facecolor="none",
            edgecolor="#2c3e50", linewidth=1.3)
    ax.set_xlim(0, 75)
    ax.set_ylim(0, 110)
    ax.set_xlabel("age")
    ax.set_ylabel("count")
    hgrid(ax)

    stamp_bad(fig)
    fig.tight_layout()
    save(fig, "avoid_line_drawings", "titanic_ages_lines")


if __name__ == "__main__":
    render()
