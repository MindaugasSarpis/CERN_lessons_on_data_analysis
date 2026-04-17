"""Blue jays bubble chart — head length vs body mass, bubbles = skull size,
faceted by sex (Wilke fig 12.3)."""

from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np

from cwilke import data as D
from cwilke.theme import apply_base, grid, save


def render() -> None:
    apply_base()
    df = D.blue_jays()

    fig, axes = plt.subplots(1, 2, figsize=(9.4, 4.0), sharey=True)
    colors = {"F": "#D55E00", "M": "#0072B2"}
    titles = {"F": "female birds", "M": "male birds"}
    # Scale skull size to bubble area (pt^2).
    skull_min, skull_max = 28.0, 34.0
    size_min, size_max = 20, 230
    for ax, s in zip(axes, ("F", "M")):
        sub = df[df["sex"] == s]
        skull = np.clip(sub["skull_size_mm"].values, skull_min, skull_max)
        size = size_min + (size_max - size_min) * (skull - skull_min) / (skull_max - skull_min)
        ax.scatter(sub["body_mass_g"], sub["head_length_mm"],
                   s=size, facecolors=colors[s],
                   edgecolors="white", linewidths=0.7, alpha=0.9)
        ax.set_xlabel("body mass (g)")
        ax.set_title(titles[s])
        grid(ax)
    axes[0].set_ylabel("head length (mm)")

    # Shared bubble legend on the right axis.
    for skull_val in (28, 30, 32, 34):
        s_ = size_min + (size_max - size_min) * (skull_val - skull_min) / (skull_max - skull_min)
        axes[1].scatter([], [], s=s_, facecolors="#666666",
                        edgecolors="white", linewidths=0.6,
                        label=f"{skull_val}")
    axes[1].legend(title="skull size (mm)", loc="lower right",
                   frameon=False, labelspacing=1.2,
                   handletextpad=0.8, borderpad=0.8)

    fig.tight_layout()
    save(fig, "associations", "blue_jays_bubble")


if __name__ == "__main__":
    render()
