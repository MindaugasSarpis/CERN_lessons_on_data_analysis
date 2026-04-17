"""Two panels of the same data: badly labelled (no units, rotated ticks,
truncated axis) vs cleanly labelled. Direct illustration of axis hygiene."""

from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np

from cwilke.theme import PRIMARY_BLUE, apply_base, hgrid, open_axes, save


def render() -> None:
    apply_base()

    days = np.arange(1, 31)
    rng = np.random.default_rng(7)
    temp = 18 + 6 * np.sin(2 * np.pi * days / 30) + rng.normal(0, 1.2, days.size)

    fig, (ax_bad, ax_good) = plt.subplots(1, 2, figsize=(9.6, 3.8))

    # --- bad: no units on y, rotated integer x ticks, no title, truncated
    ax_bad.plot(days, temp, color=PRIMARY_BLUE, linewidth=1.6, marker="o",
                 markersize=3.5, markeredgewidth=0)
    ax_bad.set_ylabel("t")
    ax_bad.set_xlabel("d")
    ax_bad.set_ylim(10, 26)
    ax_bad.set_xticks(days[::2])
    ax_bad.tick_params(axis="x", rotation=60, labelsize=9)
    ax_bad.set_title("bad axes", color="#b34b4b", fontweight="bold")
    open_axes(ax_bad)

    # --- good: units, descriptive labels, clean ticks, titled
    ax_good.plot(days, temp, color=PRIMARY_BLUE, linewidth=1.6, marker="o",
                  markersize=3.5, markeredgewidth=0)
    ax_good.set_ylabel("temperature (°C)")
    ax_good.set_xlabel("day in May")
    ax_good.set_ylim(0, 30)
    ax_good.set_xticks([1, 5, 10, 15, 20, 25, 30])
    ax_good.set_title("good axes", color="#2c8a4b", fontweight="bold")
    hgrid(ax_good)

    fig.tight_layout()
    save(fig, "coordinates_axes", "axes_labels_bad_good")


if __name__ == "__main__":
    render()
