"""Three accent colour scales stacked as swatch strips (Wilke fig 4.5, top)."""

from __future__ import annotations

import matplotlib.patches as patches
import matplotlib.pyplot as plt

from cwilke.theme import apply_base, save


# Okabe-Ito accent: first four desaturated / lightened, last three darkened
OKABE_ITO_ACCENT = [
    "#F1D49B", "#B7DCF2", "#E8C3D5", "#F6F0B8",   # subdued backdrop
    "#B97E00", "#00614A", "#004E80",              # accent trio (darkened)
]

GRAYS_WITH_ACCENTS = [
    "#999999", "#B3B3B3", "#CCCCCC", "#E6E6E6",
    "#C95C4F", "#83A121", "#6B8AD5",
]

COLORBREWER_ACCENT = [
    "#7FC97F", "#BEAED4", "#FDC086", "#FFFF99",
    "#386CB0", "#F0027F", "#BF5B17",
]

SCALES = [
    ("Okabe Ito Accent",     OKABE_ITO_ACCENT),
    ("Grays with accents",   GRAYS_WITH_ACCENTS),
    ("ColorBrewer Accent",   COLORBREWER_ACCENT),
]


def render() -> None:
    apply_base()

    fig, axes = plt.subplots(len(SCALES), 1, figsize=(11, 2.6))
    for ax, (title, palette) in zip(axes, SCALES):
        n = len(palette)
        for i, colour in enumerate(palette):
            ax.add_patch(patches.Rectangle(
                (i, 0), 1, 1,
                facecolor=colour, edgecolor="white", linewidth=1.5,
            ))
        ax.set_xlim(0, n)
        ax.set_ylim(0, 1)
        ax.set_xticks([])
        ax.set_yticks([])
        ax.set_title(title, fontsize=11, fontweight="bold",
                     color="#2c3e50", loc="left", pad=4)
        for spine in ax.spines.values():
            spine.set_visible(False)

    fig.subplots_adjust(left=0.01, right=0.99, top=0.93,
                        bottom=0.02, hspace=0.9)
    save(fig, "color", "accent_palettes")


if __name__ == "__main__":
    render()
