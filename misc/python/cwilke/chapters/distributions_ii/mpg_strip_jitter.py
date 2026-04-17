"""Jittered strip plot of mtcars mpg by cylinder count (Wilke fig 9.10)."""

from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np

from cwilke import data as D
from cwilke.theme import PRIMARY_BLUE, apply_base, hgrid, save


def render() -> None:
    apply_base()
    df = D.mtcars()
    cyls = [4, 6, 8]
    rng = np.random.default_rng(0)

    fig, ax = plt.subplots(figsize=(6.0, 4.2))
    for i, c in enumerate(cyls):
        y = df.loc[df["cyl"] == c, "mpg"].values
        x = i + rng.uniform(-0.18, 0.18, size=y.size)
        ax.scatter(x, y, s=36, color=PRIMARY_BLUE, alpha=0.75,
                   edgecolors="#2c3e50", linewidths=0.6)

    ax.set_xticks(range(len(cyls)))
    ax.set_xticklabels([str(c) for c in cyls])
    ax.set_xlim(-0.6, len(cyls) - 0.4)
    ax.set_xlabel("number of cylinders")
    ax.set_ylabel("fuel efficiency (mpg)")
    ax.set_ylim(8, 36)
    hgrid(ax)
    save(fig, "distributions_ii", "mpg_strip_jitter")


if __name__ == "__main__":
    render()
