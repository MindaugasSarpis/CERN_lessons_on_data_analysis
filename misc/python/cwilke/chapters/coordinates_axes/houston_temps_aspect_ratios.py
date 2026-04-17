"""Same data, three aspect ratios — Houston daily temperature normal.

Demonstrates that stretching / compressing a plot changes the apparent
size of variations along the y axis. All three panels show identical
data (Wilke fig 3.2 idea, simplified into three stacked panels).
"""

from __future__ import annotations

import matplotlib.pyplot as plt

from cwilke import data as D
from cwilke.theme import PRIMARY_BLUE, apply_base, grid, save


def render() -> None:
    apply_base()

    df = D.ncdc_normals_4locs()
    hou = df[df["location"] == "Houston"].sort_values("day")

    fig = plt.figure(figsize=(9.6, 6.4))
    # Grid: two columns on top (tall + wide), one wide row below
    gs = fig.add_gridspec(2, 3, width_ratios=[1, 0.05, 2],
                          height_ratios=[1.5, 1], hspace=0.55, wspace=0.1)

    ax_a = fig.add_subplot(gs[0, 0])   # tall
    ax_b = fig.add_subplot(gs[0, 2])   # wide
    ax_c = fig.add_subplot(gs[1, :])   # short wide

    month_ticks = [1, 91, 182, 274, 366]
    month_labels = ["Jan", "Apr", "Jul", "Oct", "Jan"]

    for ax, title in ((ax_a, "a"), (ax_b, "b"), (ax_c, "c")):
        ax.plot(hou["day"], hou["temperature"],
                color=PRIMARY_BLUE, linewidth=1.8)
        ax.set_ylim(50, 90)
        ax.set_xlim(0, 366)
        ax.set_xticks(month_ticks)
        ax.set_xticklabels(month_labels)
        ax.set_xlabel("month")
        ax.set_ylabel("temperature (°F)")
        ax.set_title(title, loc="left", fontweight="bold",
                     fontsize=12, color="#455a64")
        grid(ax)

    save(fig, "coordinates_axes", "houston_temps_aspect_ratios")


if __name__ == "__main__":
    render()
