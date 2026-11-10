"""Coordinates & axes family: labelling, aspect ratio, polar vs cartesian,
square-root scale. Fills the family-fanout gap found at integration (these
four figures were missing from the plan's family tables).
"""
import matplotlib.pyplot as plt
import numpy as np

import style

RNG = np.random.default_rng(42)


def _labels_bad_good():
    """Two panels: unlabeled/cryptic axes vs labeled axes with units."""
    x = np.linspace(0, 24, 49)
    y = 12 + 8 * np.sin((x - 8) * np.pi / 12) + RNG.normal(0, 0.6, x.size)
    fig, axes = style.new_fig(9, 3.6)
    fig.clf()
    ax1, ax2 = fig.subplots(1, 2)
    for ax, good in ((ax1, False), (ax2, True)):
        ax.plot(x, y, color=style.ACCENT if good else style.BAD)
        if good:
            ax.set_xlabel("time of day (h)")
            ax.set_ylabel("temperature (°C)")
        else:
            ax.set_xlabel("x")
            ax.set_ylabel("val")
    style.save(fig, "viz_coordinates_axes_axes_labels_bad_good")


def _aspect_ratios():
    """Same seasonal series at three aspect ratios — banking changes the read."""
    x = np.arange(0, 365)
    y = 15 + 10 * np.sin((x - 90) * 2 * np.pi / 365) + RNG.normal(0, 1.2, x.size)
    # three boxes of different shape in one row: wide, square, tall
    fig, (ax_wide, ax_sq, ax_tall) = plt.subplots(
        1, 3, figsize=(12, 3.6), width_ratios=[3.2, 1, 0.5])
    for ax, label, box in ((ax_wide, "wide: shallow slopes", 0.31),
                           (ax_sq, "square: slopes\nnear 45°", 1.0),
                           (ax_tall, "tall: steep\nslopes", 2.0)):
        ax.plot(x, y, lw=1.1, color=style.ACCENT)
        ax.set_box_aspect(box)
        ax.set_title(label, fontsize=12, color=style.FG)
        ax.set_xticks([0, 180, 365])
        ax.set_xlabel("day of the year")
    ax_wide.set_ylabel("temperature (°C)")
    style.save(fig, "viz_coordinates_axes_houston_temps_aspect_ratios")


def _polar_vs_cartesian():
    """Same periodic data in cartesian and polar coordinates."""
    theta = np.linspace(0, 2 * np.pi, 145)
    r = 10 + 4 * np.sin(3 * theta) + RNG.normal(0, 0.3, theta.size)
    fig, ax = style.new_fig(9, 3.8)
    fig.clf()
    ax1 = fig.add_subplot(1, 2, 1)
    ax1.plot(np.degrees(theta), r, color=style.ACCENT)
    ax1.set_xlabel("angle (°)")
    ax1.set_ylabel("value")
    ax1.set_title("on a straight axis: 0° and 360° far apart", color=style.FG)
    ax2 = fig.add_subplot(1, 2, 2, projection="polar")
    ax2.plot(theta, r, color=style.CYCLE[1])
    ax2.set_title("on a circle: 360° meets 0°", color=style.FG)
    ax2.tick_params(colors=style.DIM, labelsize=10)
    ax2.grid(color=style.GRID)  # a polar plot is read off its circles and rays
    style.save(fig, "viz_coordinates_axes_polar_vs_cartesian")


def _sqrt_scale():
    """Counts spanning a wide range: linear axis vs square-root axis."""
    cats = [f"ch {i}" for i in range(1, 11)]
    # ten counts down to zero; each carries its scatter, ± √N
    counts = np.array([48, 40, 33, 25, 18, 12, 7, 3, 1, 0])
    fig, ax = style.new_fig(9, 3.6)
    fig.clf()
    ax1, ax2 = fig.subplots(1, 2)
    for ax, scale, label in ((ax1, "linear", "linear — small counts vanish"),
                             (ax2, "sqrt", "square-root — every count visible")):
        # Dots, not bars: a non-linear axis has no honest bar base.
        ax.errorbar(cats, counts, yerr=np.sqrt(counts), fmt="o", ms=5,
                    color=style.ACCENT, ecolor=style.FG, elinewidth=1.0,
                    capsize=2, zorder=3)
        ax.set_ylim(0, (counts + np.sqrt(counts)).max() * 1.06)
        if scale == "sqrt":
            ax.set_yscale("function", functions=(np.sqrt, np.square))
            ax.set_yticks([0, 1, 5, 10, 20, 30, 50])
        ax.set_title(label, fontsize=12)
        ax.set_ylabel("events")
    style.save(fig, "viz_coordinates_axes_sqrt_scale")


# ---------------------------------------------------------------------------
# A legend without samples, and its repair. GDP growth of China and India,
# 2010-2014, % per year (World Bank, rounded as first published).
YEARS_GDP = [2010, 2011, 2012, 2013, 2014]
GDP = {"China": [10.6, 9.5, 7.9, 7.8, 7.3], "India": [10.3, 6.6, 5.6, 6.6, 7.2]}


def _legend_samples_bad():
    fig, ax = style.new_fig(5.1, 3.4)
    for (name, v), c in zip(GDP.items(), (style.BAD, "#6f8cff")):
        ax.plot(YEARS_GDP, v, color=c, lw=1.6)
    # names only: no line samples beside them
    ax.legend([plt.Line2D([], [], lw=0)] * 2, list(GDP), loc="upper right",
              handlelength=0, handletextpad=0, frameon=True, edgecolor=style.DIM)
    ax.set_xticks(YEARS_GDP)
    ax.set_ylim(-5, 15)
    ax.set_xlabel("year")
    ax.set_ylabel("growth rate")
    style.save(fig, "viz_legend_samples_bad")


def _legend_samples_good():
    fig, ax = style.new_fig(5.1, 3.4)
    for (name, v), c in zip(GDP.items(), (style.CYCLE[1], style.ACCENT)):
        ax.plot(YEARS_GDP, v, color=c, lw=1.6)
        ax.text(YEARS_GDP[-1] + 0.12, v[-1] + (0.35 if name == "China" else -0.35),
                name, color=c, va="center", fontsize=11)
    ax.set_xticks(YEARS_GDP)
    ax.set_xlim(2009.8, 2014.9)
    ax.set_ylim(0, 12)
    ax.set_xlabel("year")
    ax.set_ylabel("GDP growth (% per year)")
    style.save(fig, "viz_legend_samples_good")


FIGURES = {
    "viz_legend_samples_bad": _legend_samples_bad,
    "viz_legend_samples_good": _legend_samples_good,
    "viz_coordinates_axes_axes_labels_bad_good": _labels_bad_good,
    "viz_coordinates_axes_houston_temps_aspect_ratios": _aspect_ratios,
    "viz_coordinates_axes_polar_vs_cartesian": _polar_vs_cartesian,
    "viz_coordinates_axes_sqrt_scale": _sqrt_scale,
}
