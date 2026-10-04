"""Figures of Lecture 07: Python for Data & NumPy.

Schematics of how a list and an array lie in memory, of indexing, masks,
broadcasting and `axis`; the measured loop-against-array timings; and the
counts of `np.histogram` on the mass column of the course's data file.

The timings are measurements, so they are constants here (a figure build must
be deterministic). To measure them again on another computer:

    python figures/src/arrays.py

prints the same table from 51 repetitions of each task (median).
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyArrowPatch, Rectangle

import style

DATA = style.ROOT / "lectures" / "workbook" / "docs" / "data" / "D0_KPi.csv"

MONO = "DejaVu Sans Mono"
AMBER, GREEN, PINK, VIOLET = style.CYCLE[1], style.CYCLE[2], style.CYCLE[3], style.CYCLE[4]
CELL = "#131926"       # face of an ordinary cell
GHOST = "#0f141e"      # face of a cell that broadcasting repeats

# Measured on an Apple M2 Pro, Python 3.13.9, NumPy 2.3.5, 4 October 2026,
# with `python figures/src/arrays.py`. Median of 51 runs (15 for reading the
# file), in milliseconds, on the 91 583 rows of D0_KPi.csv:
# (task, Python loop, NumPy).
TIMINGS_MS = [
    ("read the file, 4 columns", 61.4, 18.2),
    ("sum of M", 1.59, 0.0299),
    ("mean and std of M", 6.66, 0.141),
    ("count TAU != -100", 3.68, 0.0565),
    ("M / 1000", 2.64, 0.0379),
]


def _ms(v: float) -> str:
    """Two significant digits, as on the slide: 61, 1.6, 0.030."""
    if v >= 10:
        return f"{v:.0f}"
    if v >= 1:
        return f"{v:.1f}"
    return f"{v:.2g}" if v >= 0.1 else f"{v:.3f}"


def _cell(ax, x, y, text="", w=1.0, h=1.0, fc=CELL, ec=style.DIM, tc=style.FG,
          size=11, mono=True, lw=1.0, ls="-", weight="normal"):
    ax.add_patch(Rectangle((x, y), w, h, facecolor=fc, edgecolor=ec, linewidth=lw, linestyle=ls))
    if text != "":
        ax.text(x + w / 2, y + h / 2, text, ha="center", va="center", color=tc,
                fontsize=size, family=MONO if mono else None, weight=weight)


def _arrow(ax, p, q, color=style.DIM, lw=1.2, style_="-|>", scale=10):
    ax.add_patch(FancyArrowPatch(p, q, arrowstyle=style_, mutation_scale=scale,
                                 color=color, linewidth=lw, shrinkA=0, shrinkB=0))


def _blank(w, h, xlim, ylim):
    fig, ax = plt.subplots(figsize=(w, h))
    ax.set(xlim=xlim, ylim=ylim)
    ax.set_aspect("equal")
    ax.axis("off")
    return fig, ax


def _list_vs_array():
    values = ["1880.649", "1860.6599", "1913.8755", "1888.7571"]
    fig, ax = _blank(10, 3.6, (0, 20), (0.4, 7.6))

    # --- left: a list --------------------------------------------------
    ax.text(0.2, 7.1, "list", color=AMBER, fontsize=14, weight="bold", va="center")
    ax.text(1.5, 7.1, "four references to four separate objects", color=style.DIM, fontsize=10.5, va="center")
    rw = 2.2                                   # width of one reference slot
    for i in range(4):
        _cell(ax, 0.2 + rw * i, 5.3, "reference", w=rw, h=0.85, ec=AMBER, size=9)
    ax.text(9.2, 5.72, "8 bytes", color=style.DIM, fontsize=9, va="center", ha="left")
    # float objects, staggered so that no arrow crosses a box
    ow = (0.7, 0.85, 1.5)                      # type, count, value
    spots = [(0.2, 3.3), (2.25, 1.6), (4.25, 3.3), (6.45, 1.6)]
    for i, (x, y) in enumerate(spots):
        _cell(ax, x, y, "type", w=ow[0], h=0.8, size=7.5, tc=style.DIM)
        _cell(ax, x + ow[0], y, "count", w=ow[1], h=0.8, size=7.5, tc=style.DIM)
        _cell(ax, x + ow[0] + ow[1], y, values[i], w=ow[2], h=0.8, size=8.5, ec=AMBER)
        cx = 0.2 + rw * i + rw / 2
        _arrow(ax, (cx, 5.3), (cx, y + 0.8), color=AMBER)
    ax.text(0.2, 0.8, "8 + 24 = 32 bytes per number", color=style.FG, fontsize=10, va="center")

    ax.plot([10.0, 10.0], [0.5, 7.5], color=style.GRID, linewidth=1)

    # --- right: an array -----------------------------------------------
    ax.text(10.6, 7.1, "array", color=style.ACCENT, fontsize=14, weight="bold", va="center")
    ax.text(12.4, 7.1, "one block of memory, one type", color=style.DIM, fontsize=10.5, va="center")
    _cell(ax, 10.6, 5.3, "dtype float64 · shape (4,)", w=5.6, h=0.85, size=9.5, tc=style.DIM)
    ax.text(16.45, 5.72, "stored once", color=style.DIM, fontsize=9.5, va="center")
    for i in range(4):
        _cell(ax, 10.6 + 2.2 * i, 3.3, values[i], w=2.2, h=0.85, ec=style.ACCENT, size=9.5)
    _arrow(ax, (11.7, 5.3), (11.7, 4.15), color=style.ACCENT)
    ax.text(10.6, 2.7, "the values themselves, side by side", color=style.DIM, fontsize=9.5, va="center")
    ax.text(10.6, 0.8, "8 bytes per number", color=style.FG, fontsize=10, va="center")
    style.save(fig, "viz_arrays_list_vs_array")


def _timing():
    labels = [t[0] for t in TIMINGS_MS][::-1]
    loop = np.array([t[1] for t in TIMINGS_MS][::-1])
    arr = np.array([t[2] for t in TIMINGS_MS][::-1])
    y = np.arange(len(labels))

    fig, ax = plt.subplots(figsize=(8.6, 3.7))
    ax.barh(y + 0.19, loop, height=0.36, color=AMBER, label="Python loop over a list")
    ax.barh(y - 0.19, arr, height=0.36, color=style.ACCENT, label="NumPy array")
    for yi, (a, b) in enumerate(zip(loop, arr)):
        ax.text(a * 1.15, yi + 0.19, f"{_ms(a)} ms", va="center", color=style.FG, fontsize=9.5)
        ax.text(b * 1.15, yi - 0.19, f"{_ms(b)} ms", va="center", color=style.FG, fontsize=9.5)
        ax.text(430, yi, f"{a / b:.0f}×" if a / b >= 10 else f"{a / b:.1f}×", va="center",
                ha="right", color=GREEN, fontsize=12, weight="bold")
    ax.set_xscale("log")
    ax.set_xlim(0.01, 500)
    ax.set_yticks(y, labels, family=MONO, fontsize=10, color=style.FG)
    ax.set_xlabel("time for 91 583 rows (ms, each step of the axis is a factor 10)")
    ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda v, _: f"{v:g}"))
    ax.yaxis.grid(False)
    ax.tick_params(axis="y", length=0)
    ax.legend(loc="lower center", bbox_to_anchor=(0.45, 1.0), ncols=2)
    style.save(fig, "viz_arrays_timing")


def _indexing():
    panels = [
        ("data[1, 2]", "one value", lambda r, c: (r, c) == (1, 2)),
        ("data[0]", "one row", lambda r, c: r == 0),
        ("data[:, 0]", "one column", lambda r, c: c == 0),
        ("data[1:3, :2]", "a block", lambda r, c: 1 <= r < 3 and c < 2),
    ]
    rows, cols = 5, 4
    fig, axes = plt.subplots(1, 4, figsize=(10, 3.3))
    for k, (ax, (code, what, hit)) in enumerate(zip(axes, panels)):
        ax.set(xlim=(-1.3, cols + 0.2), ylim=(-0.9, rows + 2.2))
        ax.set_aspect("equal")
        ax.axis("off")
        for r in range(rows):
            ax.text(-0.4, rows - r - 0.5, str(r), ha="center", va="center", color=style.DIM, fontsize=10, family=MONO)
            for c in range(cols):
                on = hit(r, c)
                _cell(ax, c, rows - r - 1, fc=style.ACCENT if on else CELL, ec=style.DIM, lw=1.0)
        for c in range(cols):
            ax.text(c + 0.5, rows + 0.35, str(c), ha="center", va="center", color=style.DIM, fontsize=10, family=MONO)
        ax.text(cols / 2, rows + 1.75, code, ha="center", va="center", color=style.FG, fontsize=13, family=MONO, weight="bold")
        ax.text(cols / 2, -0.25, what, ha="center", va="top", color=style.FG, fontsize=10.5)
        if k == 0:
            ax.text(cols / 2, rows + 0.95, "column", ha="center", va="center", color=style.DIM, fontsize=9.5)
            ax.text(-1.05, rows / 2, "row", ha="center", va="center", color=style.DIM, fontsize=9.5, rotation=90)
    style.save(fig, "viz_arrays_indexing")


def _mask():
    tau = ["0.41", "0.19", "-100", "0.57", "0.29", "-100"]
    mass = ["1880.6", "1860.7", "1913.9", "1888.8", "1862.5", "1845.2"]
    keep = [t != "-100" for t in tau]
    w, h = 1.9, 0.85
    x0 = 4.6
    fig, ax = _blank(8.6, 3.6, (0.2, 19.4), (0.6, 7.8))

    def label(y, text):
        ax.text(x0 - 0.3, y + h / 2, text, ha="right", va="center", color=style.FG, fontsize=10.5, family=MONO)

    label(6.6, "mass")
    label(5.6, "tau")
    label(4.4, "mask = tau != -100")
    label(2.2, "tau[mask]")
    label(1.2, "mass[mask]")
    for i, k in enumerate(keep):
        _cell(ax, x0 + w * i, 6.6, mass[i], w=w, h=h, size=10.5, tc=style.FG if k else style.DIM)
        _cell(ax, x0 + w * i, 5.6, tau[i], w=w, h=h, size=10.5, tc=style.FG if k else style.BAD)
        _cell(ax, x0 + w * i, 4.4, "True" if k else "False", w=w, h=h, size=10.5,
              fc="#12352b" if k else "#3a1c1c", tc=GREEN if k else style.BAD)
    j = 0
    for i, k in enumerate(keep):
        if not k:
            continue
        _arrow(ax, (x0 + w * i + w / 2, 4.4), (x0 + w * j + w / 2, 3.1), color=GREEN)
        _cell(ax, x0 + w * j, 2.2, tau[i], w=w, h=h, ec=style.ACCENT, size=10.5)
        _cell(ax, x0 + w * j, 1.2, mass[i], w=w, h=h, ec=style.ACCENT, size=10.5)
        j += 1
    ax.text(x0 + w * 4 + 0.4, 2.2 + h / 2, "4 values", color=style.DIM, fontsize=10.5, va="center")
    ax.text(x0 + w * 4 + 0.4, 1.2 + h / 2, "of the same 4 rows", color=style.DIM, fontsize=10.5, va="center")
    style.save(fig, "viz_arrays_mask")


def _grid(ax, x, y, values, ec=style.ACCENT, fc=CELL, tc=style.FG, ls="-", w=1.3, h=0.9, size=11):
    """values: list of rows. (x, y) is the top-left corner."""
    for r, line in enumerate(values):
        for c, v in enumerate(line):
            _cell(ax, x + w * c, y - h * (r + 1), str(v), w=w, h=h, ec=ec, fc=fc, tc=tc, ls=ls, size=size)


def _broadcasting():
    A = [[1, 2, 3], [4, 5, 6]]
    fig, ax = _blank(10, 3.4, (0, 20), (1.2, 8.0))
    w, h = 1.3, 0.9

    def line(ytop, b_real, b_ghost, result, shape_b, note):
        _grid(ax, 0.3, ytop, A)
        ax.text(0.3 + 1.5 * w, ytop - 2 * h - 0.45, "(2, 3)", ha="center", color=style.DIM, fontsize=10.5, family=MONO)
        ax.text(4.75, ytop - h, "+", ha="center", va="center", color=style.FG, fontsize=18)
        for (r, c, v) in b_ghost:
            _cell(ax, 5.3 + w * c, ytop - h * (r + 1), str(v), w=w, h=h, ec=style.DIM, fc=GHOST,
                  tc=style.DIM, ls=(0, (3, 2)), size=11)
        for (r, c, v) in b_real:
            _cell(ax, 5.3 + w * c, ytop - h * (r + 1), str(v), w=w, h=h, ec=AMBER, size=11)
        ax.text(5.3 + 1.5 * w, ytop - 2 * h - 0.45, shape_b, ha="center", color=style.DIM, fontsize=10.5, family=MONO)
        ax.text(9.75, ytop - h, "=", ha="center", va="center", color=style.FG, fontsize=18)
        _grid(ax, 10.3, ytop, result, ec=GREEN)
        ax.text(10.3 + 1.5 * w, ytop - 2 * h - 0.45, "(2, 3)", ha="center", color=style.DIM, fontsize=10.5, family=MONO)
        ax.text(14.8, ytop - h, note, va="center", color=style.FG, fontsize=10.5, linespacing=1.5)

    line(7.8,
         [(0, 0, 10), (0, 1, 20), (0, 2, 30)],
         [(1, 0, 10), (1, 1, 20), (1, 2, 30)],
         [[11, 22, 33], [14, 25, 36]],
         "(3,) → (2, 3)", "the row is used\nfor every row")
    line(4.3,
         [(0, 0, 100), (1, 0, 200)],
         [(0, 1, 100), (0, 2, 100), (1, 1, 200), (1, 2, 200)],
         [[101, 102, 103], [204, 205, 206]],
         "(2, 1) → (2, 3)", "the column is used\nfor every column")
    style.save(fig, "viz_arrays_broadcasting")


def _axis():
    A = [[1, 2, 3], [4, 5, 6]]
    w, h = 1.3, 0.9
    fig, ax = _blank(7.2, 2.75, (0, 14.4), (1.0, 6.5))
    x0, ytop = 3.4, 5.6
    _grid(ax, x0, ytop, A)
    ax.text(x0 - 0.3, ytop - h, "A", ha="right", va="center", color=style.FG, fontsize=13, family=MONO, weight="bold")
    # axis 0: down the rows, one result per column
    for c in range(3):
        _arrow(ax, (x0 + w * c + w / 2, ytop - 2 * h - 0.1), (x0 + w * c + w / 2, ytop - 2 * h - 0.95), color=AMBER)
    _grid(ax, x0, ytop - 2 * h - 1.05, [[5, 7, 9]], ec=AMBER)
    ax.text(x0 - 0.3, ytop - 3 * h - 0.6, "A.sum(axis=0)", ha="right", va="center", color=AMBER, fontsize=10.5, family=MONO)
    ax.text(x0 + 1.5 * w, ytop - 3 * h - 1.55, "one number per column", ha="center", color=style.DIM, fontsize=10)
    # axis 1: along each row, one result per row
    for r in range(2):
        _arrow(ax, (x0 + 3 * w + 0.1, ytop - h * r - h / 2), (x0 + 3 * w + 0.95, ytop - h * r - h / 2), color=GREEN)
    _grid(ax, x0 + 3 * w + 1.05, ytop, [[6], [15]], ec=GREEN)
    ax.text(x0 + 4 * w + 1.3, ytop - h, "A.sum(axis=1)", va="center", color=GREEN, fontsize=10.5, family=MONO)
    ax.text(x0 + 4 * w + 1.3, ytop - h - 0.7, "one number per row", va="center", color=style.DIM, fontsize=10)
    ax.text(x0 + 1.5 * w, ytop + 0.45, "A.sum()  is 21", ha="center", color=style.FG, fontsize=10.5, family=MONO)
    style.save(fig, "viz_arrays_axis")


def _histogram():
    M = np.loadtxt(DATA, delimiter=",", skiprows=1, usecols=0)
    counts, edges = np.histogram(M, bins=20, range=(1815, 1915))
    i = counts.argmax()

    fig, ax = plt.subplots(figsize=(5.6, 3.2))
    colours = [style.ACCENT] * len(counts)
    colours[i] = AMBER
    ax.bar(edges[:-1], counts, width=np.diff(edges), align="edge", color=colours,
           edgecolor="#0b0e14", linewidth=1.0)
    ax.text(edges[i] + 2.5, counts[i] + 200, f"counts[{i}] = {counts[i]}", ha="center",
            color=AMBER, fontsize=10.5, family=MONO)
    ax.annotate("", xy=(edges[2], 4500), xytext=(edges[3], 4500),
                arrowprops=dict(arrowstyle="<->", color=style.FG, linewidth=1.0))
    ax.text(edges[2] + 2.5, 4950, "5 MeV", ha="center", color=style.FG, fontsize=10)
    ax.text(edges[0] + 2, -2300, "edges[0]", ha="center", color=style.DIM, fontsize=9.5, family=MONO)
    ax.text(edges[-1] - 2, -2300, "edges[20]", ha="center", color=style.DIM, fontsize=9.5, family=MONO)
    ax.set_xticks(edges[::4])
    ax.set_xlim(1811, 1919)
    ax.set_ylim(0, 10000)
    ax.set_xlabel("M (MeV/c²)", labelpad=2)
    ax.set_ylabel("rows in the bin")
    ax.xaxis.grid(False)
    style.save(fig, "viz_arrays_histogram")


FIGURES = {
    "list_vs_array": _list_vs_array,
    "timing": _timing,
    "indexing": _indexing,
    "mask": _mask,
    "broadcasting": _broadcasting,
    "axis": _axis,
    "histogram": _histogram,
}


def measure() -> None:
    """Print the loop-against-array timings on this computer."""
    import csv
    import math
    import statistics
    import sys
    import time

    def median_ms(fn, n=51):
        times = []
        for _ in range(n):
            t0 = time.perf_counter()
            fn()
            times.append(time.perf_counter() - t0)
        return statistics.median(times) * 1000

    def read_lists():
        M, PT, TAU, IPCHI2 = [], [], [], []
        with open(DATA, newline="", encoding="utf-8") as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                M.append(float(row[0]))
                PT.append(float(row[1]))
                TAU.append(float(row[2]))
                IPCHI2.append(float(row[3]))
        return M, TAU

    def read_array():
        return np.loadtxt(DATA, delimiter=",", skiprows=1)

    M_list, TAU_list = read_lists()
    data = read_array()
    M, TAU = data[:, 0], data[:, 2]

    def loop_sum():
        total = 0.0
        for m in M_list:
            total += m
        return total

    def loop_mean_std():
        total = 0.0
        for m in M_list:
            total += m
        mean = total / len(M_list)
        squares = 0.0
        for m in M_list:
            squares += (m - mean) ** 2
        return mean, math.sqrt(squares / len(M_list))

    def loop_count():
        n = 0
        for t in TAU_list:
            if t != -100:
                n += 1
        return n

    tasks = [
        ("read the file, 4 columns", lambda: median_ms(read_lists, 15), lambda: median_ms(read_array, 15)),
        ("sum of M", lambda: median_ms(loop_sum), lambda: median_ms(M.sum)),
        ("mean and std of M", lambda: median_ms(loop_mean_std), lambda: median_ms(lambda: (M.mean(), M.std()))),
        ("count TAU != -100", lambda: median_ms(loop_count), lambda: median_ms(lambda: (TAU != -100).sum())),
        ("M / 1000", lambda: median_ms(lambda: [m / 1000 for m in M_list]), lambda: median_ms(lambda: M / 1000)),
    ]
    print(f"Python {sys.version.split()[0]}, NumPy {np.__version__}, {len(M_list)} rows")
    print(f"{'task':26s} {'loop ms':>9s} {'NumPy ms':>9s} {'factor':>7s}")
    for name, loop, arr in tasks:
        a, b = loop(), arr()
        print(f"{name:26s} {a:9.3g} {b:9.3g} {a / b:7.1f}")


if __name__ == "__main__":
    measure()
