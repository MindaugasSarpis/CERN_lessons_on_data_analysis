"""Blue jays body mass vs head length, coloured by sex (Wilke fig 12.1)."""

from __future__ import annotations

import matplotlib.pyplot as plt

from cwilke import data as D
from cwilke.theme import PRIMARY_BLUE, PRIMARY_ORANGE, apply_base, open_axes, save


def render() -> None:
    apply_base()
    df = D.blue_jays()

    fig, ax = plt.subplots(figsize=(6.4, 4.4))
    colors = {"F": PRIMARY_ORANGE, "M": PRIMARY_BLUE}
    labels = {"F": "female", "M": "male"}
    for s in ("F", "M"):
        sub = df[df["sex"] == s]
        ax.scatter(
            sub["body_mass_g"], sub["head_length_mm"],
            s=40, color=colors[s], alpha=0.75,
            edgecolors="#2c3e50", linewidths=0.5,
            label=labels[s],
        )
    ax.set_xlabel("body mass (g)")
    ax.set_ylabel("head length (mm)")
    ax.legend(loc="lower right", title="sex")
    open_axes(ax)
    save(fig, "associations", "blue_jays_scatter")


if __name__ == "__main__":
    render()
