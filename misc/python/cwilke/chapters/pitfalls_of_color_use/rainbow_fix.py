"""The fix for the rainbow pitfall: Okabe-Ito (Wilke ch. 19).

Same iris scatter, colour-mapped through the colour-blind-safe
Okabe-Ito palette. Three discriminable hues for three categorical
classes, no invented ordering.
"""

from __future__ import annotations

import matplotlib.pyplot as plt

from cwilke import data as D
from cwilke.theme import OKABE_ITO, apply_base, open_axes, save


def render() -> None:
    apply_base()
    df = D.iris()

    fig, ax = plt.subplots(figsize=(6.8, 5.0))
    species = sorted(df["species"].unique())
    palette = [OKABE_ITO[1], OKABE_ITO[2], OKABE_ITO[3]]
    for sp, col in zip(species, palette):
        sub = df[df["species"] == sp]
        ax.scatter(sub["sepal_length"], sub["sepal_width"],
                   s=58, color=col, alpha=0.9,
                   edgecolor="white", linewidth=0.5, label=sp)

    ax.set_xlabel("sepal length (cm)")
    ax.set_ylabel("sepal width (cm)")
    ax.set_title("Iris · Okabe-Ito (colour-blind safe)")
    ax.legend(loc="upper right", fontsize=10, title="species")
    open_axes(ax)
    fig.tight_layout()
    save(fig, "pitfalls_of_color_use", "rainbow_fix")


if __name__ == "__main__":
    render()
