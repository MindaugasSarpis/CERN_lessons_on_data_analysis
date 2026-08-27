"""Anatomy of a figure: the D0 -> K-pi+ spectrum built element by element.
Six cumulative stages with IDENTICAL geometry/limits, for a v-click build-up
slide. Synthetic stand-in for the real seminar data: Gaussian peak at
1865 MeV on a falling background, fixed seed.
"""
import numpy as np

import style

LO, HI, NBINS = 1780, 1950, 60

def _data():
    # Fresh generator per call: every stage MUST draw the identical dataset,
    # or points and y-limits jump between v-click reveals.
    rng = np.random.default_rng(1865)
    bkg = rng.uniform(LO, HI, 6000)
    sig = rng.normal(1865, 8.5, 2200)
    counts, edges = np.histogram(np.concatenate([bkg, sig]), bins=NBINS, range=(LO, HI))
    centers = 0.5 * (edges[:-1] + edges[1:])
    return centers, counts

def _stage(n: int):
    """Build the figure up to stage n (1..6) and save viz_anatomy_stage{n}.

    Stages are stacked as v-click layers in the slide, so each must be an
    OPAQUE dark canvas of identical geometry: fixed margins (no constrained
    layout, no tight bbox) so every element sits at the same pixel in every
    stage, and a solid background so stage n fully covers stage n-1.
    """
    import matplotlib.pyplot as plt
    centers, counts = _data()
    fig, ax = plt.subplots(figsize=(7.6, 4.4), layout="none")
    fig.subplots_adjust(left=0.1, right=0.97, top=0.88, bottom=0.14)
    ax.set_xlim(LO, HI)
    ax.set_ylim(0, counts.max() * 1.25)
    if n < 2:
        ax.set_xticklabels([]); ax.set_yticklabels([])
        ax.grid(False)
    if n >= 2:
        ax.set_xlabel(r"$m(K^-\pi^+)$ [MeV/$c^2$]")
        ax.set_ylabel(f"Candidates / {(HI-LO)//NBINS} MeV")
    if n >= 3:
        ax.plot(centers, counts, "o", ms=3.5, color=style.ACCENT, zorder=3)
    if n >= 4:
        ax.errorbar(centers, counts, yerr=np.sqrt(counts), fmt="none",
                    ecolor=style.DIM, elinewidth=1, zorder=2)
    if n >= 5:
        ax.axvline(1865, color=style.CYCLE[1], lw=1.2, ls="--")
        ax.annotate(r"$D^0$ peak (~1865 MeV)", xy=(1865, counts.max() * 1.02),
                    xytext=(1890, counts.max() * 1.12), color=style.CYCLE[1],
                    arrowprops=dict(arrowstyle="->", color=style.CYCLE[1]))
    if n >= 6:
        # Stage 6 = the title as the FINDING, not a description of the axes.
        ax.set_title(r"A clear $D^0$ peak at 1865 MeV above a flat background")
    style.save(fig, f"viz_anatomy_stage{n}", opaque=True, tight=False)

FIGURES = {f"viz_anatomy_stage{n}": (lambda n=n: _stage(n)) for n in range(1, 7)}
