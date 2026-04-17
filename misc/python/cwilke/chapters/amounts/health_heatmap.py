"""Heatmap: synthetic vaccination rates, 10 states × 20 years (Wilke fig 6.16)."""

from __future__ import annotations

import numpy as np
import matplotlib.pyplot as plt

from cwilke.theme import apply_base, grid, save


def render() -> None:
    apply_base()

    rng = np.random.default_rng(42)
    states = ["AL", "CA", "FL", "IL", "MA", "NY", "OH", "PA", "TX", "WA"]
    years = np.arange(1998, 2018)

    # Simulate a slow increase over time with state-level offsets + noise.
    base = np.linspace(0.55, 0.92, years.size)[None, :]
    state_offset = rng.uniform(-0.12, 0.08, size=(len(states), 1))
    noise = rng.normal(0, 0.04, size=(len(states), years.size))
    rates = np.clip(base + state_offset + noise, 0.0, 1.0)

    fig, ax = plt.subplots(figsize=(8.0, 4.2))
    im = ax.imshow(rates, aspect="auto", cmap="viridis",
                   vmin=0.0, vmax=1.0, origin="upper")
    ax.set_xticks(np.arange(years.size)[::2])
    ax.set_xticklabels(years[::2], rotation=0)
    ax.set_yticks(np.arange(len(states)))
    ax.set_yticklabels(states)
    ax.set_xlabel("year")
    ax.set_ylabel("state")
    ax.tick_params(axis="both", length=0)
    grid(ax)
    ax.grid(False)  # heatmaps don't need gridlines on top of cells

    cbar = fig.colorbar(im, ax=ax, shrink=0.9, pad=0.02)
    cbar.set_label("vaccination rate")
    save(fig, "amounts", "health_heatmap")


if __name__ == "__main__":
    render()
