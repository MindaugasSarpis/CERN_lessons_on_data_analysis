"""Small multiples without facet shading — bars float (Wilke fig 23.5)."""

from __future__ import annotations

import matplotlib.pyplot as plt

from cwilke import data as D
from cwilke.theme import apply_base, save, stamp_ugly


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
            ax.set_ylim(0, 200)
            if i == 0:
                ax.set_title(out, fontsize=11, color="#455a64")
            if j == 1:
                ax.text(1.06, 0.5, cls, transform=ax.transAxes,
                        rotation=-90, va="center", fontsize=11,
                        color="#455a64", fontweight="bold")
            # No grid, no panel background, no spines below.
            for sp in ("top", "right", "left", "bottom"):
                ax.spines[sp].set_visible(False)
            ax.tick_params(axis="both", length=0, labelsize=9)

    fig.supylabel("count", fontsize=11)
    stamp_ugly(fig)
    fig.tight_layout()
    save(fig, "balance_data_context", "titanic_survival_bad")


if __name__ == "__main__":
    render()
