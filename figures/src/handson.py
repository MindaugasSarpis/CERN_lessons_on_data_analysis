"""Hands-on family: the rendered output of the Matplotlib snippets of
lecture 07, so each code slide shows its result beside the code.

Every figure is drawn from the weather station's hourly log,
`lectures/workbook/docs/data/weather.csv`, read with the functions of the
lecture's module `weather.py` (copied below, so the data reach Matplotlib as
the same plain lists the slides make). Two groups of figures.

- The opening, before any code: every hour at its time and the hours in
  bins of 1 °C with the mean as a line, drawn full width in the course style.
- The section "A First Plot": every hour as one line, with the default
  geometry and with the time on x; the 87 552 temperatures as a histogram
  with the default binning, with three bin widths, and with the binning the
  slides settle on (-17 to 33 °C, 50 bins of 1 °C). These keep Matplotlib's
  default geometry (a box, no grid), so that the room sees the shape it will
  get on its own laptop.
- The section "Hands-on Matplotlib": the hours below 0 °C per year as bars,
  the yearly means against the mean of the ten years, and the monthly means
  with an annotation and a title that states the finding.

One figure more is drawn for Lecture 9, whose opening slide still shows it:
the mass column `M` of `D0_KPi.csv` as points with error bars of sqrt(count).

The plotting calls mirror the slide snippets line for line (same data,
colours, limits); only the canvas is the course dark style and the figure
size is set for the slide.
"""
from datetime import datetime

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle

import style

PATH = style.ROOT / "lectures" / "workbook" / "docs" / "data" / "weather.csv"

# Matplotlib's own geometry in the course colours: a box, no grid.
MPL_DEFAULT = {
    "axes.grid": False,
    "axes.spines.top": True,
    "axes.spines.right": True,
}

TEMP_LABEL = "temperature (°C)"


# ---------------------------------------------------------------------------
# weather.py, as the lecture writes it
# ---------------------------------------------------------------------------

MISSING = -999.0


def read_lines(path):
    return open(path).read().splitlines()[1:]


def temp_of(line):
    return float(line.split(",")[1])


def temps(path):
    result = []
    for line in read_lines(path):
        temp = temp_of(line)
        if temp != MISSING:
            result.append(temp)
    return result


def mean(values):
    return sum(values) / len(values)


def hours(path):
    times = []
    result = []
    for line in read_lines(path):
        temp = temp_of(line)
        if temp != MISSING:
            times.append(datetime.fromisoformat(line[0:16]))
            result.append(temp)
    return times, result


def group(path, start, stop):
    groups = {}
    for line in read_lines(path):
        temp = temp_of(line)
        if temp == MISSING:
            continue
        key = line[start:stop]
        if key not in groups:
            groups[key] = []
        groups[key].append(temp)
    return groups


def _means(groups):
    names = []
    means = []
    for key in groups:
        names.append(key)
        means.append(mean(groups[key]))
    return names, means


# ---------------------------------------------------------------------------
# A First Plot
# ---------------------------------------------------------------------------

def _figure_axes():
    """Figure, Axes and artists, each named by the call that makes it."""
    names, means = _means(group(PATH, 5, 7))
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
    ax.plot(names, means, "o", color=style.ACCENT)
    ax.set_xlabel("month")
    ax.set_ylabel(TEMP_LABEL)
    ax.set_title("Monthly means", fontsize=13)
    ax.set_ylim(-5, 20)
    ax.set_xticks(["01", "04", "07", "10"])

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
    call('ax.plot(x, y, "o")', (0.468, 0.715), (0.67, 0.62))
    call("ax.set_ylim(-5, 20)", (0.63, 0.44), (0.67, 0.44))
    call("ax.set_xlabel(...)", (0.42, 0.125), (0.67, 0.26))
    fig.text(0.67, 0.085, "fig.savefig(...)", color=style.CYCLE[1],
             va="center", **mono)
    style.save(fig, "viz_handson_figure_axes", tight=False)


def _hours_default():
    values = temps(PATH)
    with mpl.rc_context(MPL_DEFAULT):
        fig, ax = plt.subplots(figsize=(5.2, 3.6))
        ax.plot(values)
        style.save(fig, "viz_handson_hours_default")


def _hours_dates():
    times, values = hours(PATH)
    with mpl.rc_context(MPL_DEFAULT):
        fig, ax = plt.subplots(figsize=(5.2, 3.6))
        ax.plot(times, values, linewidth=0.2)
        ax.set_xlabel("time")
        ax.set_ylabel(TEMP_LABEL)
        style.save(fig, "viz_handson_hours_dates")


def _temp_default():
    values = temps(PATH)
    with mpl.rc_context(MPL_DEFAULT):
        fig, ax = plt.subplots(figsize=(5.2, 3.6))
        ax.hist(values)
        style.save(fig, "viz_handson_temp_default")


def _temp_binwidths():
    """10 °C and 1 °C over the whole range, 0.05 °C from 0 to 2 °C."""
    values = temps(PATH)
    panels = [(6, (-20, 40), "10 °C per bin: 6 bins", style.BAD),
              (50, (-17, 33), "1 °C per bin: 50 bins", style.FG),
              (41, (-0.025, 2.025), "0.05 °C per bin, 0 to 2 °C", style.BAD)]
    fig, axes = plt.subplots(1, 3, figsize=(10.4, 3.3))
    for ax, (bins, span, title, color) in zip(axes, panels):
        ax.hist(values, bins=bins, range=span, color=style.ACCENT)
        ax.set_title(title, fontsize=12, fontweight="normal", color=color)
        ax.set_xlabel(TEMP_LABEL)
        ax.xaxis.grid(False)
    axes[0].set_ylabel("hours per bin")
    style.save(fig, "viz_handson_temp_binwidths")


def _temp_hist():
    values = temps(PATH)
    with mpl.rc_context(MPL_DEFAULT):
        fig, ax = plt.subplots(figsize=(5.2, 3.6))
        ax.hist(values, bins=50, range=(-17, 33))
        ax.set_xlabel(TEMP_LABEL)
        ax.set_ylabel("hours per 1 °C")
        style.save(fig, "viz_handson_temp_hist")


# ---------------------------------------------------------------------------
# The opening: the two figures shown before any code, full width
# ---------------------------------------------------------------------------

def _hours_view():
    """Every measured hour at its time, the coldest and the warmest marked."""
    times, values = hours(PATH)
    cold = values.index(min(values))
    warm = values.index(max(values))
    fig, ax = plt.subplots(figsize=(9, 3.8))
    ax.plot(times, values, linewidth=0.25, color=style.ACCENT)
    ax.set_ylabel(TEMP_LABEL)
    ax.xaxis.grid(False)
    arrow = {"arrowstyle": "->", "color": style.CYCLE[1]}
    ax.annotate(f"{values[cold]} °C, 7 Jan 2025", xy=(times[cold], values[cold]),
                xytext=(-150, -2), textcoords="offset points", va="center",
                color=style.CYCLE[1], arrowprops=arrow)
    ax.annotate(f"{values[warm]} °C, 18 Jun 2018", xy=(times[warm], values[warm]),
                xytext=(40, -4), textcoords="offset points", va="center",
                color=style.CYCLE[1], arrowprops=arrow)
    ax.set_ylim(-22, 38)
    style.save(fig, "viz_handson_hours_view")


def _temp_view():
    """The hours in bins of 1 °C, the mean as a line in the dip."""
    values = temps(PATH)
    m = mean(values)
    fig, ax = plt.subplots(figsize=(9, 3.8))
    ax.hist(values, bins=50, range=(-17, 33), color=style.ACCENT)
    ax.axvline(m, color=style.CYCLE[1], linewidth=1.6)
    ax.annotate(f"mean {m:.2f} °C", xy=(m, 3300), xytext=(10, 0),
                textcoords="offset points", color=style.CYCLE[1], va="center")
    ax.set(xlabel=TEMP_LABEL, ylabel="hours per 1 °C", xlim=(-17, 33))
    ax.xaxis.grid(False)
    style.save(fig, "viz_handson_temp_view")


# ---------------------------------------------------------------------------
# Hands-on Matplotlib
# ---------------------------------------------------------------------------

def _frost_bars():
    years = group(PATH, 0, 4)
    frost = []
    for year in years:
        count = 0
        for temp in years[year]:
            if temp < 0:
                count = count + 1
        frost.append(count)

    fig, ax = plt.subplots(figsize=(6, 3.2))
    ax.bar(range(2016, 2026), frost, color="#56B4E9", width=0.7)
    ax.set(xlabel="year", ylabel="hours below 0 °C", ylim=(0, 3000))

    ax.yaxis.grid(True, color="#b0bec5", linewidth=0.6)
    ax.xaxis.grid(False)
    ax.set_axisbelow(True)
    for side in ("top", "right", "left"):
        ax.spines[side].set_visible(False)
    style.save(fig, "viz_handson_frost_bars")


def _year_means():
    """The ten yearly means as points, the mean of all hours as a line."""
    names, means = _means(group(PATH, 0, 4))
    all_hours = mean(temps(PATH))

    fig, ax = plt.subplots(figsize=(5.2, 3.6))
    ax.axhline(all_hours, color="#D55E00", label="2016–2025: 7.16 °C")
    ax.plot(range(2016, 2026), means, "o", color="#56B4E9",
            label="one year")
    ax.set(xlabel="year", ylabel="mean temperature (°C)", ylim=(5, 9))
    ax.legend(frameon=False, loc="lower left")
    style.save(fig, "viz_handson_year_means")


def _month_annotated():
    """The monthly means with the warmest month marked and a finding."""
    names, means = _means(group(PATH, 5, 7))

    fig, ax = plt.subplots(figsize=(5.6, 3.6))
    ax.plot(names, means, "o-", color="#56B4E9")
    arrow = {"arrowstyle": "->", "color": "#D55E00"}
    ax.annotate("July, 18.5 °C", xy=("07", means[6]), xytext=("09", 19.5),
                color="#D55E00", arrowprops=arrow)
    ax.set(xlabel="month", ylabel="mean temperature (°C)", ylim=(-6, 22))
    ax.set_title("July is 22.4 °C warmer than January")
    style.save(fig, "viz_handson_month_annotated")


# ---------------------------------------------------------------------------
# Lecture 9: the D0 mass histogram as points with error bars
# ---------------------------------------------------------------------------

def _mass_errorbars():
    """Counts per 1 MeV/c² as points with error bars of sqrt(count)."""
    m = np.loadtxt(PATH.parent / "D0_KPi.csv", delimiter=",", skiprows=1, usecols=0)

    counts, edges = np.histogram(m, bins=110, range=(1810, 1920))
    centres = (edges[:-1] + edges[1:]) / 2

    fig, ax = plt.subplots(figsize=(5.6, 3.6))
    ax.errorbar(centres, counts, yerr=np.sqrt(counts), fmt="o", ms=3,
                color="#56B4E9")
    arrow = {"arrowstyle": "->", "color": "#D55E00"}
    ax.annotate("$D^0$", xy=(1870, 1650), xytext=(1885, 1900), color="#D55E00",
                arrowprops=arrow)
    ax.set(xlabel=r"$K^-\pi^+$ mass $M$ (MeV/$c^2$)",
           ylabel="candidates per 1 MeV/$c^2$", ylim=(0, 2100))
    ax.set_title("A peak at 1865 MeV/$c^2$")
    style.save(fig, "viz_handson_mass_errorbars")


FIGURES = {
    "viz_handson_hours_view": _hours_view,
    "viz_handson_temp_view": _temp_view,
    "viz_handson_figure_axes": _figure_axes,
    "viz_handson_hours_default": _hours_default,
    "viz_handson_hours_dates": _hours_dates,
    "viz_handson_temp_default": _temp_default,
    "viz_handson_temp_binwidths": _temp_binwidths,
    "viz_handson_temp_hist": _temp_hist,
    "viz_handson_frost_bars": _frost_bars,
    "viz_handson_year_means": _year_means,
    "viz_handson_month_annotated": _month_annotated,
    "viz_handson_mass_errorbars": _mass_errorbars,
}

if __name__ == "__main__":
    values = temps(PATH)
    print("hours", len(values), "mean", round(mean(values), 2),
          "min", min(values), "max", max(values))
    print("months", [(k, round(m, 2)) for k, m in zip(*_means(group(PATH, 5, 7)))])
    print("years", [(k, round(m, 2)) for k, m in zip(*_means(group(PATH, 0, 4)))])
