"""Movie rankings vs. vote counts by year — small multiples (Wilke fig 21.2).

100-year window laid out as a 10×10 grid of tiny scatter + regression
panels. Demonstrates how many facets can be squeezed into a single
figure when all panels share the same axes.
"""

from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np

from cwilke import data as D
from cwilke.theme import PRIMARY_BLUE, apply_base, save


def render() -> None:
    apply_base()
    df = D.movie_rankings()
    years = np.arange(1906, 2006)
    assert len(years) == 100

    fig, axes = plt.subplots(10, 10, figsize=(12.0, 12.0),
                             sharex=True, sharey=True)

    for year, ax in zip(years, axes.ravel()):
        sub = df[df["year"] == year]
        # subsample to keep the scatter light
        if len(sub) > 200:
            sub = sub.sample(200, random_state=year)
        ax.scatter(sub["votes"], sub["rating"], s=1.2,
                   color=PRIMARY_BLUE, alpha=0.32, linewidths=0)

        # Linear regression on log10(votes)
        lx = np.log10(sub["votes"].values)
        slope, intercept = np.polyfit(lx, sub["rating"].values, 1)
        xs_fit = np.array([10, 1e5])
        ys_fit = slope * np.log10(xs_fit) + intercept
        ax.plot(xs_fit, ys_fit, color="#D55E00", linewidth=1.0)

        ax.set_xscale("log")
        ax.set_xlim(8, 3e5)
        ax.set_ylim(0, 10)
        ax.text(0.04, 0.93, str(year), transform=ax.transAxes,
                ha="left", va="top", fontsize=7, color="#455a64",
                bbox=dict(facecolor="white", edgecolor="none",
                          alpha=0.75, pad=1))
        ax.set_xticks([10, 1000, 100000])
        ax.set_yticks([0, 5, 10])
        ax.tick_params(axis="both", labelsize=7, length=2)
        for sp in ("top", "right"):
            ax.spines[sp].set_visible(False)

    fig.supxlabel("number of votes", fontsize=12)
    fig.supylabel("average rating", fontsize=12)
    fig.tight_layout()
    save(fig, "multi_panel", "movie_rankings_small_multiples")


if __name__ == "__main__":
    render()
