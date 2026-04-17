"""Blue-green diverging swatch under CVD simulations (Wilke fig 19.7)."""

from __future__ import annotations

import matplotlib.patches as patches
import matplotlib.pyplot as plt

from cwilke._cvd import simulate
from cwilke.theme import apply_base, save


BLUE_GREEN = ["#284F9B", "#7E9CC7", "#E5E5E5", "#7EB085", "#056D05"]

PANELS = [
    ("original", "original"),
    ("deuteranopia simulation", "deuteranopia"),
    ("protanopia simulation",   "protanopia"),
    ("tritanopia simulation",   "tritanopia"),
]


def render() -> None:
    apply_base()

    fig, axes = plt.subplots(2, 2, figsize=(11.5, 3.0))
    for ax, (title, kind) in zip(axes.flatten(), PANELS):
        sim = [simulate(h, kind) for h in BLUE_GREEN]
        for i, colour in enumerate(sim):
            ax.add_patch(patches.Rectangle(
                (i, 0), 1, 1,
                facecolor=colour, edgecolor="white", linewidth=1.2,
            ))
        ax.set_xlim(0, len(sim))
        ax.set_ylim(0, 1)
        ax.set_xticks([])
        ax.set_yticks([])
        ax.set_title(title, fontsize=11, fontweight="bold",
                     color="#2c3e50", loc="left", pad=4)
        for spine in ax.spines.values():
            spine.set_visible(False)

    fig.subplots_adjust(left=0.01, right=0.99, top=0.89,
                        bottom=0.04, hspace=0.9, wspace=0.08)
    save(fig, "pitfalls_of_color_use", "blue_green_cvd_sim")


if __name__ == "__main__":
    render()
