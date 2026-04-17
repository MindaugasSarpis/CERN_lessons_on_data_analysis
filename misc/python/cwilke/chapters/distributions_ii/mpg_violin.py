"""Violin plot of mtcars mpg by cylinder count (Wilke fig 9.7)."""

from __future__ import annotations

import matplotlib.pyplot as plt

from cwilke import data as D
from cwilke.theme import PRIMARY_BLUE, apply_base, hgrid, save


def render() -> None:
    apply_base()
    df = D.mtcars()
    cyls = [4, 6, 8]
    groups = [df.loc[df["cyl"] == c, "mpg"].values for c in cyls]

    fig, ax = plt.subplots(figsize=(6.0, 4.2))
    parts = ax.violinplot(
        groups,
        positions=range(len(cyls)),
        widths=0.8,
        showmeans=False,
        showmedians=True,
        showextrema=False,
    )
    for body in parts["bodies"]:
        body.set_facecolor(PRIMARY_BLUE)
        body.set_edgecolor("#2c3e50")
        body.set_alpha(0.85)
        body.set_linewidth(1.0)
    if "cmedians" in parts:
        parts["cmedians"].set_color("black")
        parts["cmedians"].set_linewidth(1.6)

    ax.set_xticks(range(len(cyls)))
    ax.set_xticklabels([str(c) for c in cyls])
    ax.set_xlabel("number of cylinders")
    ax.set_ylabel("fuel efficiency (mpg)")
    ax.set_ylim(8, 36)
    hgrid(ax)
    save(fig, "distributions_ii", "mpg_violin")


if __name__ == "__main__":
    render()
