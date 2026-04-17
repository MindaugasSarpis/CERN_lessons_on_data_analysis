"""Scatter with vertical error bars (Wilke fig 16.1 concept)."""

from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np

from cwilke.theme import PRIMARY_BLUE, apply_base, open_axes, save


def render() -> None:
    apply_base()
    rng = np.random.default_rng(0)

    x = np.arange(1, 9)
    y = 2.0 + 0.6 * x + rng.normal(0, 0.35, size=x.size)
    err = rng.uniform(0.3, 0.8, size=x.size)

    fig, ax = plt.subplots(figsize=(6.2, 4.2))
    ax.errorbar(
        x, y, yerr=err,
        fmt="o",
        color=PRIMARY_BLUE,
        ecolor="#2c3e50",
        elinewidth=1.1,
        capsize=3,
        markersize=7,
        markeredgecolor="#2c3e50",
        markeredgewidth=0.6,
    )
    ax.set_xlabel("sample")
    ax.set_ylabel("measured value")
    ax.set_xticks(x)
    open_axes(ax)
    save(fig, "uncertainty", "error_bars")


if __name__ == "__main__":
    render()
