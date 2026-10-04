"""Hands-on family: the rendered output of the Matplotlib snippets of
lecture 08, so each code slide shows its result beside the code.

Two groups of figures.

- The section "A First Plot": the two running examples of the course, read
  from `lectures/workbook/docs/data/`. The pendulum table as a line and as
  points with labelled axes, the mass column `M` of `D0_KPi.csv` as a
  histogram with the default binning, with three bin widths, and with the
  binning the slides settle on (1810 to 1920 MeV/c², 55 bins of 2 MeV/c²).
  These keep Matplotlib's default geometry (a box, no grid), so that the
  room sees the shape it will get on its own laptop.
- The section "Hands-on Matplotlib": the minimal bar chart, the pendulum
  points with the curve of the formula, and the mass histogram as points
  with error bars, a title and an annotation.

The plotting calls mirror the slide snippets line for line (same data,
colours, limits); only the canvas is the course dark style and the figure
size is set for the slide.
"""
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle

import style

DATA = style.ROOT / "lectures" / "workbook" / "docs" / "data"

# Matplotlib's own geometry in the course colours: a box, no grid.
MPL_DEFAULT = {
    "axes.grid": False,
    "axes.spines.top": True,
    "axes.spines.right": True,
}

# The binning of the mass histogram, stated on the slides.
M_LO, M_HI, M_BINS = 1810, 1920, 55
MASS_LABEL = r"$K^-\pi^+$ mass $M$ (MeV/$c^2$)"


def _pendulum():
    data = np.loadtxt(DATA / "pendulum.csv", delimiter=",", skiprows=1)
    return data[:, 0], data[:, 1]


def _mass():
    return np.loadtxt(DATA / "D0_KPi.csv", delimiter=",", skiprows=1, usecols=0)


# ---------------------------------------------------------------------------
# A First Plot
# ---------------------------------------------------------------------------

def _figure_axes():
    """Figure, Axes and artists, each named by the call that makes it."""
    length, t10 = _pendulum()
    fig = plt.figure(figsize=(5.4, 3.75), layout="none")
    fig.add_artist(Rectangle((0.012, 0.016), 0.976, 0.968, transform=fig.transFigure,
                             fill=False, ls=(0, (5, 4)), lw=1.4, ec=style.CYCLE[1]))
    ax = fig.add_axes([0.16, 0.25, 0.47, 0.50])
    ax.grid(False)
    for side in ("top", "right"):
        ax.spines[side].set_visible(True)
    for spine in ax.spines.values():
        spine.set_edgecolor(style.CYCLE[2])
        spine.set_linewidth(1.4)
    ax.plot(length, t10, "o", color=style.ACCENT)
    ax.set_xlabel("length (cm)")
    ax.set_ylabel("time of 10 swings (s)")
    ax.set_title("Pendulum", fontsize=13)
    ax.set_xlim(0, 110)
    ax.set_ylim(0, 22)

    mono = {"family": "DejaVu Sans Mono", "fontsize": 10.5}
    fig.text(0.035, 0.925, "Figure", color=style.CYCLE[1], fontsize=13, fontweight="bold")
    fig.text(0.175, 0.925, "fig", color=style.CYCLE[1], **mono)
    fig.text(0.035, 0.855, "Axes", color=style.CYCLE[2], fontsize=13, fontweight="bold")
    fig.text(0.145, 0.855, "ax", color=style.CYCLE[2], **mono)

    arrow = dict(arrowstyle="-", color=style.DIM, lw=1.0, shrinkA=2, shrinkB=3)

    def call(text, xy_fig, xy_text):
        fig.text(*xy_text, text, color=style.FG, va="center", **mono)
        ax.annotate("", xy=xy_fig, xytext=(xy_text[0] - 0.008, xy_text[1]),
                    xycoords="figure fraction", textcoords="figure fraction",
                    arrowprops=arrow)

    call("ax.set_title(...)", (0.475, 0.80), (0.67, 0.80))
    call('ax.plot(x, y, "o")', (0.512, 0.652), (0.67, 0.62))
    call("ax.set_ylim(0, 22)", (0.63, 0.44), (0.67, 0.44))
    call("ax.set_xlabel(...)", (0.50, 0.125), (0.67, 0.26))
    fig.text(0.67, 0.085, "fig.savefig(...)", color=style.CYCLE[1],
             va="center", **mono)
    style.save(fig, "viz_handson_figure_axes", tight=False)


def _pendulum_default():
    length, t10 = _pendulum()
    with mpl.rc_context(MPL_DEFAULT):
        fig, ax = plt.subplots(figsize=(5.2, 3.6))
        ax.plot(length, t10)
        style.save(fig, "viz_handson_pendulum_default")


def _pendulum_points():
    length, t10 = _pendulum()
    with mpl.rc_context(MPL_DEFAULT):
        fig, ax = plt.subplots(figsize=(5.2, 3.6))
        ax.plot(length, t10, "o")
        ax.set_xlabel("length (cm)")
        ax.set_ylabel("time of 10 swings (s)")
        ax.set_xlim(0, 110)
        ax.set_ylim(0, 22)
        style.save(fig, "viz_handson_pendulum_points")


def _mass_default():
    m = _mass()
    with mpl.rc_context(MPL_DEFAULT):
        fig, ax = plt.subplots(figsize=(5.2, 3.6))
        ax.hist(m)
        style.save(fig, "viz_handson_mass_default")


def _mass_binwidths():
    """The same range, 1810 to 1920 MeV/c², with bins of 10, 2 and 0.2."""
    m = _mass()
    panels = [(11, "10 MeV/$c^2$ per bin: 11 bins", style.BAD),
              (55, "2 MeV/$c^2$ per bin: 55 bins", style.FG),
              (550, "0.2 MeV/$c^2$ per bin: 550 bins", style.BAD)]
    fig, axes = plt.subplots(1, 3, figsize=(10.4, 3.3))
    for ax, (bins, title, color) in zip(axes, panels):
        ax.hist(m, bins=bins, range=(M_LO, M_HI), color=style.ACCENT)
        ax.set_title(title, fontsize=12, fontweight="normal", color=color)
        ax.set_xlabel(MASS_LABEL)
        ax.xaxis.grid(False)
    axes[0].set_ylabel("candidates per bin")
    style.save(fig, "viz_handson_mass_binwidths")


def _mass_hist():
    m = _mass()
    with mpl.rc_context(MPL_DEFAULT):
        fig, ax = plt.subplots(figsize=(5.2, 3.6))
        ax.hist(m, bins=M_BINS, range=(M_LO, M_HI))
        ax.set_xlabel(MASS_LABEL)
        ax.set_ylabel("candidates per 2 MeV/$c^2$")
        style.save(fig, "viz_handson_mass_hist")


# ---------------------------------------------------------------------------
# Hands-on Matplotlib
# ---------------------------------------------------------------------------

def _bar_minimal():
    days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
    sales = [22, 25, 31, 28, 36]

    fig, ax = plt.subplots(figsize=(6, 3.2))
    ax.bar(days, sales, color="#56B4E9", width=0.7)
    ax.set(xlabel="weekday", ylabel="sales (M USD)", ylim=(0, 40))

    ax.yaxis.grid(True, color="#b0bec5", linewidth=0.6)
    ax.xaxis.grid(False)
    ax.set_axisbelow(True)
    for side in ("top", "right", "left"):
        ax.spines[side].set_visible(False)
    style.save(fig, "viz_handson_bar_minimal")


def _pendulum_curve():
    """The measured points and the curve of t10 = 10 · 2π√(L/g)."""
    length, t10 = _pendulum()

    L = np.linspace(0, 110, 200)
    formula = 10 * 2 * np.pi * np.sqrt(L / 100 / 9.81)

    fig, ax = plt.subplots(figsize=(5.2, 3.6))
    ax.plot(L, formula, color="#D55E00", label="formula, g = 9.81 m/s²")
    ax.plot(length, t10, "o", color="#56B4E9", label="measured")
    ax.set(xlabel="length (cm)", ylabel="time of 10 swings (s)",
           xlim=(0, 110), ylim=(0, 22))
    ax.legend(frameon=False, loc="lower right")
    style.save(fig, "viz_handson_pendulum_curve")


def _mass_errorbars():
    """Counts per 1 MeV/c² as points with error bars of sqrt(count)."""
    m = _mass()

    counts, edges = np.histogram(m, bins=110, range=(M_LO, M_HI))
    centres = (edges[:-1] + edges[1:]) / 2

    fig, ax = plt.subplots(figsize=(5.6, 3.6))
    ax.errorbar(centres, counts, yerr=np.sqrt(counts), fmt="o", ms=3,
                color="#56B4E9")
    arrow = {"arrowstyle": "->", "color": "#D55E00"}
    ax.annotate("$D^0$", xy=(1870, 1650), xytext=(1885, 1900), color="#D55E00",
                arrowprops=arrow)
    ax.set(xlabel=MASS_LABEL, ylabel="candidates per 1 MeV/$c^2$",
           ylim=(0, 2100))
    ax.set_title("A peak at 1865 MeV/$c^2$")
    style.save(fig, "viz_handson_mass_errorbars")


FIGURES = {
    "viz_handson_figure_axes": _figure_axes,
    "viz_handson_pendulum_default": _pendulum_default,
    "viz_handson_pendulum_points": _pendulum_points,
    "viz_handson_mass_default": _mass_default,
    "viz_handson_mass_binwidths": _mass_binwidths,
    "viz_handson_mass_hist": _mass_hist,
    "viz_handson_bar_minimal": _bar_minimal,
    "viz_handson_pendulum_curve": _pendulum_curve,
    "viz_handson_mass_errorbars": _mass_errorbars,
}
