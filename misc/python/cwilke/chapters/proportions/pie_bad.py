"""Pie chart (anti-pattern) of popularity goals for 4th-graders."""

from __future__ import annotations

import matplotlib.pyplot as plt

from cwilke import data as D
from cwilke.theme import OKABE_ITO, apply_base, save, stamp_ugly


def render() -> None:
    apply_base()
    df = D.students_popularity()
    sub = df[df["grade"] == "4th"].copy()

    goals = ["Grades", "Popular", "Sports"]
    colors = [OKABE_ITO[5], OKABE_ITO[1], OKABE_ITO[3]]
    values = sub.set_index("goal").loc[goals, "percent"].values

    fig, ax = plt.subplots(figsize=(5.2, 5.2))
    ax.pie(values, labels=goals, colors=colors,
           autopct="%1.0f%%", startangle=90,
           wedgeprops=dict(edgecolor="white", linewidth=1.5))
    ax.set_aspect("equal")
    stamp_ugly(fig)
    save(fig, "proportions", "pie_bad")


if __name__ == "__main__":
    render()
