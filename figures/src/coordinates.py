"""Coordinates & axes family: labelling, aspect ratio, polar vs cartesian,
square-root scale. Fills the family-fanout gap found at integration (these
four figures were missing from the plan's family tables).
"""
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
            ax.set_xlabel("time of day [h]")
            ax.set_ylabel("temperature [°C]")
            ax.set_title("labeled, with units", color=style.FG)
        else:
            ax.set_xlabel("x")
            ax.set_ylabel("val")
            ax.set_title("cryptic labels, no units", color=style.BAD)
    style.save(fig, "viz_coordinates_axes_axes_labels_bad_good")


def _aspect_ratios():
    """Same seasonal series at three aspect ratios — banking changes the read."""
    x = np.arange(0, 365)
    y = 15 + 10 * np.sin((x - 90) * 2 * np.pi / 365) + RNG.normal(0, 1.2, x.size)
    fig, ax = style.new_fig(9, 4.6)
    fig.clf()
    gs = fig.add_gridspec(2, 2, height_ratios=[1, 1.6])
    ax_wide = fig.add_subplot(gs[0, :])
    ax_sq = fig.add_subplot(gs[1, 0])
    ax_tall = fig.add_subplot(gs[1, 1])
    for ax, label in ((ax_wide, "wide — day-to-day change readable"),
                      (ax_sq, "square"), (ax_tall, "tall — slope exaggerated")):
        ax.plot(x, y, lw=1.1, color=style.ACCENT)
        ax.set_title(label, fontsize=10, color=style.DIM)
        ax.set_xticks([0, 180, 365])
        ax.set_xlabel("day", fontsize=9)
    ax_wide.set_ylabel("temperature", fontsize=9)
    style.save(fig, "viz_coordinates_axes_houston_temps_aspect_ratios")


def _polar_vs_cartesian():
    """Same periodic data in cartesian and polar coordinates."""
    theta = np.linspace(0, 2 * np.pi, 145)
    r = 10 + 4 * np.sin(3 * theta) + RNG.normal(0, 0.3, theta.size)
    fig, ax = style.new_fig(9, 3.8)
    fig.clf()
    ax1 = fig.add_subplot(1, 2, 1)
    ax1.plot(np.degrees(theta), r, color=style.ACCENT)
    ax1.set_xlabel("angle [deg]")
    ax1.set_ylabel("r")
    ax1.set_title("cartesian", color=style.FG)
    ax2 = fig.add_subplot(1, 2, 2, projection="polar")
    ax2.plot(theta, r, color=style.CYCLE[1])
    ax2.set_title("polar — periodicity is visible", color=style.FG)
    ax2.tick_params(colors=style.DIM, labelsize=8)
    ax2.grid(color=style.GRID)
    style.save(fig, "viz_coordinates_axes_polar_vs_cartesian")


def _sqrt_scale():
    """Counts spanning a wide range: linear axis vs square-root axis."""
    cats = [f"ch {i}" for i in range(1, 11)]
    counts = np.sort(RNG.integers(4, 2200, 10))[::-1]
    fig, ax = style.new_fig(9, 3.6)
    fig.clf()
    ax1, ax2 = fig.subplots(1, 2)
    for ax, scale, label in ((ax1, "linear", "linear — small counts vanish"),
                             (ax2, "sqrt", "square-root — every count visible")):
        # Dots, not bars: a non-linear axis has no honest bar base.
        ax.plot(cats, counts, "o", ms=8, color=style.ACCENT, zorder=3)
        ax.set_ylim(0, counts.max() * 1.12)
        if scale == "sqrt":
            ax.set_yscale("function", functions=(np.sqrt, np.square))
            ax.set_yticks([10, 100, 500, 1000, 2000])
        ax.set_title(label, fontsize=10, color=style.DIM)
        ax.tick_params(axis="x", rotation=45, labelsize=8)
        ax.set_ylabel("events")
    style.save(fig, "viz_coordinates_axes_sqrt_scale")


FIGURES = {
    "viz_coordinates_axes_axes_labels_bad_good": _labels_bad_good,
    "viz_coordinates_axes_houston_temps_aspect_ratios": _aspect_ratios,
    "viz_coordinates_axes_polar_vs_cartesian": _polar_vs_cartesian,
    "viz_coordinates_axes_sqrt_scale": _sqrt_scale,
}
