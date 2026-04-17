"""HOP schematic for mpg ~ displ fits (Wilke fig 16.20)."""

from __future__ import annotations

import numpy as np
import matplotlib.pyplot as plt

from cwilke.chapters.uncertainty.mpg_uncertain import _fit_and_draws
from cwilke.theme import apply_base, grid, save


def render() -> None:
    apply_base()
    df, x_grid, y_grid, se, _all_draws, Xg = _fit_and_draws()
    rng = np.random.default_rng(8692276)
    # Re-draw 6 with a fresh seed
    from scipy.stats import t  # unused here; kept for parity
    cov = np.cov(_all_draws.T)  # rough — not used
    draws = _all_draws[:6]

    fig, axes = plt.subplots(2, 3, figsize=(9.2, 5.0), sharex=True, sharey=True)
    axes_flat = axes.flatten()
    for ax, d in zip(axes_flat, draws):
        ax.scatter(df["disp"], df["mpg"], color="#777777", s=20)
        ax.plot(x_grid, Xg @ d, color="#0072B2", linewidth=1.2)
        ax.set_ylim(8.5, 35)
        grid(ax)
    for ax in axes[1]:
        ax.set_xlabel("displacement (cu. in.)")
    for ax in axes[:, 0]:
        ax.set_ylabel("fuel efficiency (mpg)")
    fig.tight_layout()
    save(fig, "uncertainty", "mpg_uncertain_hop_static")


if __name__ == "__main__":
    render()
