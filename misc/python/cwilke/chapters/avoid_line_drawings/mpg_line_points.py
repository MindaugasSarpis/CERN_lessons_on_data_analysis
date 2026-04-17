"""Scatter drawn with open line-drawn markers — noisy (Wilke fig 22.6)."""

from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np

from cwilke import data as D
from cwilke.theme import apply_base, open_axes, save, stamp_ugly


def render() -> None:
    apply_base()
    df = D.mpg().copy()

    # Small jitter
    rng = np.random.default_rng(7384)
    df["displ_j"] = df["displ"] + rng.normal(0, 0.05, len(df))
    df["cty_j"] = df["cty"] + rng.normal(0, 0.25, len(df))

    markers = {"f": "x", "r": "o", "4": "^"}
    labels = {"f": "FWD", "r": "RWD", "4": "4WD"}

    fig, ax = plt.subplots(figsize=(7.2, 4.6))
    for drv, mk in markers.items():
        sub = df[df["drv"] == drv]
        ax.scatter(sub["displ_j"], sub["cty_j"], s=28, marker=mk,
                   facecolors="none", edgecolors="#2c3e50",
                   linewidths=1.0, label=labels[drv])
    ax.set_xlabel("displacement (l)")
    ax.set_ylabel("fuel economy (mpg)")
    ax.legend(loc="upper right", title="drive train", fontsize=9,
              frameon=False)
    open_axes(ax)

    stamp_ugly(fig)
    fig.tight_layout()
    save(fig, "avoid_line_drawings", "mpg_line_points")


if __name__ == "__main__":
    render()
