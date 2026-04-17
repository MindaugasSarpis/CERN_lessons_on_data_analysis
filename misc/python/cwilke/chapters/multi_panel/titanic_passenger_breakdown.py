"""Titanic passenger breakdown — 3×2 small-multiples bar grid (Wilke fig 21.1).

Rows: passenger class (1st, 2nd, 3rd). Columns: outcome (died, survived).
Each panel shows the bar counts of female vs. male passengers.
"""

from __future__ import annotations

import matplotlib.pyplot as plt

from cwilke import data as D
from cwilke.theme import apply_base, hgrid, save


def render() -> None:
    apply_base()
    df = D.titanic().copy()
    df["outcome"] = df["survived"].map({0: "died", 1: "survived"})
    df["class"] = df["pclass"].map({1: "1st", 2: "2nd", 3: "3rd"})

    colors = {"female": "#D55E00", "male": "#0072B2"}
    classes = ["1st", "2nd", "3rd"]
    outcomes = ["died", "survived"]

    fig, axes = plt.subplots(3, 2, figsize=(6.4, 6.4),
                             sharex=True, sharey=True)

    for i, cls in enumerate(classes):
        for j, out in enumerate(outcomes):
            ax = axes[i, j]
            counts = (df[(df["class"] == cls) & (df["outcome"] == out)]
                      .groupby("sex").size())
            ax.bar(["female", "male"],
                   [counts.get("female", 0), counts.get("male", 0)],
                   color=[colors["female"], colors["male"]],
                   alpha=0.85, width=0.68)
            if i == 0:
                ax.set_title(out, fontsize=11, color="#455a64")
            if j == 1:
                ax.text(1.06, 0.5, cls, transform=ax.transAxes,
                        rotation=-90, va="center", fontsize=11,
                        color="#455a64", fontweight="bold")
            ax.set_ylim(0, 200)
            hgrid(ax)
            ax.tick_params(axis="y", labelsize=9)
            ax.tick_params(axis="x", labelsize=9)

    fig.supylabel("count", fontsize=11)
    fig.tight_layout()
    save(fig, "multi_panel", "titanic_passenger_breakdown")


if __name__ == "__main__":
    render()
