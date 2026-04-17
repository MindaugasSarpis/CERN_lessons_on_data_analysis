"""Boxplot of mtcars mpg by cylinder count (Wilke fig 9.3)."""

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
    bp = ax.boxplot(
        groups,
        positions=range(len(cyls)),
        widths=0.55,
        patch_artist=True,
        medianprops=dict(color="black", linewidth=1.6),
        boxprops=dict(facecolor=PRIMARY_BLUE, edgecolor="#2c3e50",
                      alpha=0.85, linewidth=1.0),
        whiskerprops=dict(color="#2c3e50", linewidth=1.0),
        capprops=dict(color="#2c3e50", linewidth=1.0),
        flierprops=dict(marker="o", markerfacecolor="#2c3e50",
                        markersize=4, markeredgecolor="none", alpha=0.7),
    )
    del bp  # silence unused
    ax.set_xticks(range(len(cyls)))
    ax.set_xticklabels([str(c) for c in cyls])
    ax.set_xlabel("number of cylinders")
    ax.set_ylabel("fuel efficiency (mpg)")
    ax.set_ylim(8, 36)
    hgrid(ax)
    save(fig, "distributions_ii", "mpg_boxplot")


if __name__ == "__main__":
    render()
