"""Same histogram drawn with solid filled bars — clear (Wilke fig 22.2)."""

from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np

from cwilke import data as D
from cwilke.theme import PRIMARY_BLUE, apply_base, hgrid, save


def render() -> None:
    apply_base()
    df = D.titanic_all()

    bins = np.arange(0, 76, 3)
    fig, ax = plt.subplots(figsize=(7.2, 4.2))
    ax.hist(df["age"], bins=bins, color=PRIMARY_BLUE,
            edgecolor="white", linewidth=0.6)
    ax.set_xlim(0, 75)
    ax.set_ylim(0, 110)
    ax.set_xlabel("age")
    ax.set_ylabel("count")
    hgrid(ax)

    fig.tight_layout()
    save(fig, "avoid_line_drawings", "titanic_ages_filled")


if __name__ == "__main__":
    render()
