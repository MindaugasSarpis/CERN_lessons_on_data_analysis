"""Blue jays scatter coloured by sex (Wilke fig 12.2)."""

from __future__ import annotations

import matplotlib.pyplot as plt

from cwilke import data as D
from cwilke.theme import apply_base, grid, save


def render() -> None:
    apply_base()
    df = D.blue_jays()

    fig, ax = plt.subplots(figsize=(6.0, 4.2))
    colors = {"F": "#D55E00", "M": "#0072B2"}
    labels = {"F": "female birds", "M": "male birds"}
    for s in ("F", "M"):
        sub = df[df["sex"] == s]
        ax.scatter(sub["body_mass_g"], sub["head_length_mm"],
                   s=40, facecolors=colors[s], edgecolors="white",
                   linewidths=0.7, label=labels[s])
    ax.set_xlabel("body mass (g)")
    ax.set_ylabel("head length (mm)")
    ax.legend(loc="lower right", frameon=False)
    grid(ax)
    save(fig, "associations", "blue_jays_scatter_sex")


if __name__ == "__main__":
    render()
