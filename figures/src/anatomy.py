"""Anatomy of a figure: the hourly temperatures of the weather log as a
histogram of 1 °C bins, built element by element. Six cumulative stages with
IDENTICAL geometry/limits, for a v-click build-up slide: the frame, the axes
with their units, the bars, the mean as a reference line, an annotation, the
title that states the finding. The data are the 87 552 measured hours of
weather.csv, read with the lecture's functions (handson.py).
"""
import numpy as np

import style
from handson import PATH, mean, temps

LO, HI, NBINS = -17, 33, 50          # 1 °C per bin, as on the slides


def _data():
    values = temps(PATH)
    counts, edges = np.histogram(values, bins=NBINS, range=(LO, HI))
    return edges, counts, mean(values)


def _stage(n: int):
    """Build the figure up to stage n (1..6) and save viz_anatomy_stage{n}.

    Stages are stacked as v-click layers in the slide, so each must be an
    OPAQUE dark canvas of identical geometry: fixed margins (no constrained
    layout, no tight bbox) so every element sits at the same pixel in every
    stage, and a solid background so stage n fully covers stage n-1.
    """
    import matplotlib.pyplot as plt
    edges, counts, m = _data()
    fig, ax = plt.subplots(figsize=(7.6, 4.4), layout="none")
    fig.subplots_adjust(left=0.1, right=0.97, top=0.88, bottom=0.14)
    ax.set_xlim(LO, HI)
    ax.set_ylim(0, counts.max() * 1.25)
    ax.xaxis.grid(False)
    if n < 2:
        ax.set_xticklabels([]); ax.set_yticklabels([])
        ax.grid(False)
    if n >= 2:
        ax.set_xlabel("temperature (°C)")
        ax.set_ylabel("hours per 1 °C")
    if n >= 3:
        ax.stairs(counts, edges, fill=True, color=style.ACCENT, zorder=3)
    if n >= 4:
        ax.axvline(m, color=style.CYCLE[1], lw=1.6, zorder=4)
    if n >= 5:
        ax.annotate(f"mean {m:.2f} °C, in the dip", xy=(m, counts.max() * 0.78),
                    xytext=(m + 6, counts.max() * 1.12), color=style.CYCLE[1],
                    fontsize=12, arrowprops=dict(arrowstyle="->", color=style.CYCLE[1]))
    if n >= 6:
        # Stage 6 = the title as the FINDING, not a description of the axes.
        ax.set_title("Ten years of hours form two peaks, and the mean lies between them")
    style.save(fig, f"viz_anatomy_stage{n}", opaque=True, tight=False)


FIGURES = {f"viz_anatomy_stage{n}": (lambda n=n: _stage(n)) for n in range(1, 7)}
