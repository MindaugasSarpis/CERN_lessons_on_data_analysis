"""Lecture 02 (Introduction to Data): the lifecycle of research data.

  viz_lifecycle_rdm   the six stages of the slide "Data Has a Lifecycle", in
                      its words and order, as a cycle with arrows

The course's own drawing, after the research data lifecycle of Harvard
Medical School (https://datamanagement.hms.harvard.edu/). It is drawn like
the Lecture 06 diagrams (git.py): hairline panels like the deck's cards, text
in Space Grotesk (embedded as outlines), the deck's cyan for the arrows.

The canvas is laid out in pixels (100 per inch, y downwards). The slide shows
it about 422 pixels wide, so the 21-pixel names read at about 15 pixels, as
the text of the Lecture 06 diagrams does.

Run:  python figures/src/build.py --only lifecycle
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.font_manager import FontProperties
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch
from matplotlib.path import Path as MPath

import style

FONTS = Path(__file__).resolve().parents[1] / "fonts" / "git"
SANS = FontProperties(fname=FONTS / "SpaceGrotesk-Medium.ttf")

# the deck's tokens (lectures/content/theme/styles/tokens.css)
FG, ACC = "#f2f5f9", "#7dd3fc"
HAIR = (139 / 255, 151 / 255, 166 / 255, 0.34)   # --hair-strong
PANEL = (1, 1, 1, 0.018)                          # --panel
PT = 0.72  # points per canvas pixel

# the card's six stages, clockwise from the top
STAGES = ["Collect", "Store", "Clean", "Analyse", "Decide", "Share and\narchive"]
W, H = 600, 470            # canvas
CX, CY = W / 2, H / 2      # centre of the ring
A, B = 245, 190            # half-axes of the ring
SIZE = 21                  # the names, in canvas pixels
BOX_W = 132                # "Share and" (99 px) and 16 px on each side
BOX_H, BOX_H2 = 48, 74     # a box of one line, of two lines
GAP = 9                    # between an arrow's end and a box


def _ring(theta):
    """The point of the ring at angle theta (degrees, counter-clockwise from 3 o'clock)."""
    t = np.radians(theta)
    return CX + A * np.cos(t), CY - B * np.sin(t)


def _inside(p, c, h, pad):
    return abs(p[0] - c[0]) <= BOX_W / 2 + pad and abs(p[1] - c[1]) <= h / 2 + pad


def rdm():
    fig = plt.figure(figsize=(W / 100, H / 100), layout="none")
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, W)
    ax.set_ylim(H, 0)
    ax.axis("off")

    angles = [90 - 60 * i for i in range(6)]
    centres = [_ring(a) for a in angles]
    heights = [BOX_H2 if "\n" in s else BOX_H for s in STAGES]

    # the arrows: the ring from one box to the next, clockwise
    for i in range(6):
        j = (i + 1) % 6
        sweep = np.linspace(angles[i], angles[i] - 60, 721)
        free = [a for a in sweep
                if not _inside(_ring(a), centres[i], heights[i], GAP)
                and not _inside(_ring(a), centres[j], heights[j], GAP)]
        pts = [_ring(a) for a in np.linspace(free[0], free[-1], 40)]
        path = MPath(pts, [MPath.MOVETO] + [MPath.LINETO] * (len(pts) - 1))
        head = 16
        ax.add_patch(FancyArrowPatch(
            path=path, color=ACC, lw=2.6, mutation_scale=1,
            arrowstyle=f"-|>,head_length={head * PT:.1f},head_width={head * PT * 0.45:.1f}",
            capstyle="round", joinstyle="round"))

    # the stages
    for (x, y), h, name in zip(centres, heights, STAGES):
        ax.add_patch(FancyBboxPatch((x - BOX_W / 2, y - h / 2), BOX_W, h,
                                    boxstyle="round,pad=0,rounding_size=9",
                                    fc=PANEL, ec=HAIR, lw=1.3))
        lines = name.split("\n")
        lead = SIZE * 1.2
        for k, line in enumerate(lines):
            # baseline a third of the size under the middle: the letters
            # (cap height about 0.7 of the size) sit centred in the box
            base = y + (k - (len(lines) - 1) / 2) * lead + SIZE * 0.35
            ax.text(x, base, line, fontsize=SIZE * PT, color=FG, fontproperties=SANS,
                    ha="center", va="baseline")
    style.save(fig, "viz_lifecycle_rdm", tight=False)


FIGURES = {"viz_lifecycle_rdm": rdm}

if __name__ == "__main__":
    style.use()
    for fn in FIGURES.values():
        fn()
