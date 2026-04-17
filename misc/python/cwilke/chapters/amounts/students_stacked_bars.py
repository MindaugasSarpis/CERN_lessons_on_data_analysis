"""Stacked bar chart: popularity goals by grade (Wilke fig 6.8)."""

from __future__ import annotations

import numpy as np
import matplotlib.pyplot as plt

from cwilke import data as D
from cwilke.theme import OKABE_ITO, apply_base, hgrid, save


def render() -> None:
    apply_base()
    df = D.students_popularity()

    grades = ["4th", "5th", "6th"]
    goals = ["Grades", "Popular", "Sports"]
    colors = [OKABE_ITO[5], OKABE_ITO[1], OKABE_ITO[3]]

    pivot = df.pivot(index="grade", columns="goal", values="percent").loc[grades, goals]

    fig, ax = plt.subplots(figsize=(6.2, 4.2))
    bottom = np.zeros(len(grades))
    for i, goal in enumerate(goals):
        vals = pivot[goal].values
        ax.bar(grades, vals, bottom=bottom, label=goal,
               color=colors[i], alpha=0.9, width=0.6)
        bottom = bottom + vals

    ax.set_xlabel("grade")
    ax.set_ylabel("% of students")
    ax.set_ylim(0, 105)
    hgrid(ax)
    ax.tick_params(axis="x", length=0)
    ax.legend(loc="center left", bbox_to_anchor=(1.02, 0.5), frameon=False)
    save(fig, "amounts", "students_stacked_bars")


if __name__ == "__main__":
    render()
