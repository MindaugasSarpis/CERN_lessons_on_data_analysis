"""Age pyramid — two histograms back-to-back (Wilke fig 7.8).

A staple of demography. Flips a histogram horizontally so male/female
(or any pair of) distributions can be compared along a shared age axis.
Only works for two groups.
"""

from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np

from cwilke import data as D
from cwilke.theme import apply_base, save, vgrid


MALE_COLOR = "#0072B2"
FEMALE_COLOR = "#D55E00"


def render() -> None:
    apply_base()
    df = D.titanic().dropna(subset=["age"])
    bins = np.arange(0, 78, 3)

    male_counts, _ = np.histogram(df.loc[df["sex"] == "male", "age"], bins=bins)
    female_counts, _ = np.histogram(df.loc[df["sex"] == "female", "age"], bins=bins)
    centres = (bins[:-1] + bins[1:]) / 2
    h = bins[1] - bins[0]

    fig, ax = plt.subplots(figsize=(7.0, 4.4))
    ax.barh(centres, -male_counts, height=h * 0.95,
            color=MALE_COLOR, alpha=0.9, align="center", label="male")
    ax.barh(centres, female_counts, height=h * 0.95,
            color=FEMALE_COLOR, alpha=0.9, align="center", label="female")

    ax.axvline(0, color="#2c3e50", linewidth=0.8)
    ax.set_ylabel("age (years)")
    ax.set_xlabel("count")
    # Symmetric tick labels around zero.
    xmax = max(male_counts.max(), female_counts.max()) + 5
    ticks = np.arange(-40, 25, 20)
    ax.set_xticks(ticks)
    ax.set_xticklabels([str(abs(t)) for t in ticks])
    ax.set_xlim(-xmax, xmax * 0.6)
    ax.set_ylim(0, 75)
    vgrid(ax)
    ax.text(-xmax + 2, 70, "male",   color=MALE_COLOR,   fontweight="bold")
    ax.text(xmax * 0.4, 70, "female", color=FEMALE_COLOR, fontweight="bold")
    fig.tight_layout()
    save(fig, "distributions_i", "titanic_age_pyramid")


if __name__ == "__main__":
    render()
