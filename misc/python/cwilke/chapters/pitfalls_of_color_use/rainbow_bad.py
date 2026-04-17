"""Canonical 'rainbow is bad' example (Wilke ch. 19).

Mapping categorical species to a rainbow (hsv/jet) palette invents
perceptual structure where none exists: some hues pop harshly, the
sequence reads as ordinal (it isn't), and colour-blind readers cannot
disambiguate red/green. Paired with `rainbow_fix.py` below.
"""

from __future__ import annotations

import matplotlib.pyplot as plt

from cwilke import data as D
from cwilke.theme import apply_base, open_axes, save, stamp_bad


def render() -> None:
    apply_base()
    df = D.iris()

    fig, ax = plt.subplots(figsize=(6.8, 5.0))
    species = sorted(df["species"].unique())
    # hsv / jet: the classic rainbow. Misleading for categorical data.
    rainbow = plt.cm.hsv([0.05, 0.45, 0.85])
    for sp, col in zip(species, rainbow):
        sub = df[df["species"] == sp]
        ax.scatter(sub["sepal_length"], sub["sepal_width"],
                   s=58, color=col, alpha=0.85,
                   edgecolor="white", linewidth=0.5, label=sp)

    ax.set_xlabel("sepal length (cm)")
    ax.set_ylabel("sepal width (cm)")
    ax.set_title("Iris · rainbow palette (hsv)")
    ax.legend(loc="upper right", fontsize=10, title="species")
    open_axes(ax)
    stamp_bad(fig)
    fig.tight_layout()
    save(fig, "pitfalls_of_color_use", "rainbow_bad")


if __name__ == "__main__":
    render()
