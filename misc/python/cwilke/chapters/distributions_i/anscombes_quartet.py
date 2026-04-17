"""Anscombe's quartet — four datasets with identical summary statistics
but wildly different shapes. The canonical argument for always plotting
your data before summarising it."""

from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np

from cwilke.theme import PRIMARY_BLUE, apply_base, open_axes, save


# Anscombe (1973). Same mean, variance, correlation, and regression line.
_X_I = [10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5]
_Y_I = [8.04, 6.95, 7.58, 8.81, 8.33, 9.96, 7.24, 4.26, 10.84, 4.82, 5.68]
_X_II = _X_I
_Y_II = [9.14, 8.14, 8.74, 8.77, 9.26, 8.10, 6.13, 3.10, 9.13, 7.26, 4.74]
_X_III = _X_I
_Y_III = [7.46, 6.77, 12.74, 7.11, 7.81, 8.84, 6.08, 5.39, 8.15, 6.42, 5.73]
_X_IV = [8, 8, 8, 8, 8, 8, 8, 19, 8, 8, 8]
_Y_IV = [6.58, 5.76, 7.71, 8.84, 8.47, 7.04, 5.25, 12.50, 5.56, 7.91, 6.89]


def render() -> None:
    apply_base()
    datasets = [("I", _X_I, _Y_I), ("II", _X_II, _Y_II),
                ("III", _X_III, _Y_III), ("IV", _X_IV, _Y_IV)]

    fig, axes = plt.subplots(2, 2, figsize=(7.6, 5.2),
                              sharex=True, sharey=True)
    xs = np.linspace(3, 20, 100)
    for ax, (label, x, y) in zip(axes.flat, datasets):
        x = np.array(x, dtype=float)
        y = np.array(y, dtype=float)
        slope, intercept = np.polyfit(x, y, 1)
        ax.plot(xs, slope * xs + intercept,
                color="#b0bec5", linewidth=1.4, zorder=1)
        ax.scatter(x, y, s=36, color=PRIMARY_BLUE,
                    edgecolor="#2c3e50", linewidth=0.6, zorder=2)
        ax.set_title(f"dataset {label}", fontsize=11)
        ax.set_xlim(3, 20)
        ax.set_ylim(2, 14)
        open_axes(ax)

    for ax in axes[-1, :]:
        ax.set_xlabel("x")
    for ax in axes[:, 0]:
        ax.set_ylabel("y")

    fig.suptitle("four datasets · same mean, variance, correlation, fit",
                 fontsize=12, y=0.995)
    fig.tight_layout()
    save(fig, "distributions_i", "anscombes_quartet")


if __name__ == "__main__":
    render()
