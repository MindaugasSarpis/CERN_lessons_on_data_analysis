"""Grouped bar chart: goals ascribed to popularity by grade (Wilke fig 6.4)."""

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
    colors = [OKABE_ITO[5], OKABE_ITO[1], OKABE_ITO[3]]  # blue, orange, green

    pivot = df.pivot(index="grade", columns="goal", values="percent").loc[grades, goals]

    x = np.arange(len(grades))
    width = 0.26

    fig, ax = plt.subplots(figsize=(7.2, 4.2))
    for i, goal in enumerate(goals):
        ax.bar(x + (i - 1) * width, pivot[goal].values, width,
               label=goal, color=colors[i], alpha=0.9)

    ax.set_xticks(x)
    ax.set_xticklabels(grades)
    ax.set_xlabel("grade")
    ax.set_ylabel("% of students")
    ax.set_ylim(0, 60)
    hgrid(ax)
    ax.tick_params(axis="x", length=0)
    ax.legend(loc="upper right", ncol=3, frameon=False)
    save(fig, "amounts", "students_grouped_bars")


if __name__ == "__main__":
    render()
