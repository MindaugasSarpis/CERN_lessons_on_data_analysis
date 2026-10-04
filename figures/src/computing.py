"""Figures of Lecture 15: Computing Infrastructure & HPC.

Every number below was measured for the slides on one machine:
MacBook Pro 14-inch (2023), Apple M2 Pro, 12 cores (8 performance and
4 efficiency), 16 GB of memory, internal SSD, Python 3.13.9, NumPy 2.3.5.
The scripts are those of Seminar 15 (lectures/workbook/docs/data/
hpc_time_sum.py and hpc_sum_parallel.py); each time is the smallest of five
runs. To refresh the figures on another machine, rerun the scripts, change
the constants in the block MEASURED and run this file.

Run:  python figures/src/build.py --only computing
      (needs "computing" in FAMILIES of build.py), or directly:
      python figures/src/computing.py
"""
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle

import style

# ----------------------------------------------------------------- MEASURED
# hpc_time_sum.py: the sum of column M, 91 583 rows, in milliseconds
T_LOOP_MS = 1.53
T_NUMPY_MS = 0.018
T_POOL4_MS = 91.0

# hpc_sum_parallel.py --passes 1200: wall time in seconds per worker count
WORKERS = [1, 2, 4, 8, 12]
T_PAR = [1.964, 1.044, 0.586, 0.406, 0.408]

# 1 GB in memory, 2 GB on the SSD (not kept in the file cache), in GB/s
RATE_MEMORY_COPY = 10.2
RATE_SSD_READ = 4.4

CYAN = style.ACCENT
ORANGE = style.CYCLE[1]
GREEN = style.CYCLE[2]
PINK = style.CYCLE[3]
VIOLET = style.CYCLE[4]


def _amdahl(n, s):
    """Speed-up on n workers when the fraction s of the run stays serial."""
    return 1.0 / (s + (1.0 - s) / n)


def _serial_parts():
    """T(N) = t_s + t_p / N through the points N = 1 and N = 2."""
    t_p = 2.0 * (T_PAR[0] - T_PAR[1])
    t_s = T_PAR[0] - t_p
    return t_s, t_p


# ------------------------------------------------------------------ figures
def three_ways():
    """One sum, three ways: time on a log axis."""
    fig, ax = style.new_fig(6.4, 2.1)
    names = ["NumPy  M.sum()", "Python loop", "4 processes, the same loop"]
    times = [T_NUMPY_MS, T_LOOP_MS, T_POOL4_MS]
    colors = [GREEN, CYAN, ORANGE]
    y = np.arange(len(names))[::-1]
    ax.barh(y, [t - 0.004 for t in times], color=colors, height=0.58, left=0.004)
    for yi, t in zip(y, times):
        label = f"{t:.3f} ms" if t < 0.1 else (f"{t:.2f} ms" if t < 10 else f"{t:.0f} ms")
        ax.text(t * 1.3, yi, label, va="center", ha="left", fontsize=12,
                color=style.FG, fontweight="bold")
    ax.set_yticks(y)
    ax.set_yticklabels(names, fontsize=12, color=style.FG)
    ax.set_xscale("log")
    ax.set_xlim(0.004, 2000)
    ax.set_xticks([0.01, 0.1, 1, 10, 100, 1000])
    ax.set_xticklabels(["0.01", "0.1", "1", "10", "100", "1000"])
    ax.set_xlabel("time for the sum of 91 583 values, in ms")
    ax.grid(axis="y", visible=False)
    style.save(fig, "viz_computing_three_ways")


def amdahl():
    """Amdahl's law for five serial fractions."""
    fig, ax = style.new_fig(5.6, 4.0)
    n = np.arange(1, 129)
    ax.plot(n, n, color=style.DIM, lw=1.2, ls="--")
    ax.text(15, 24, "s = 0:  S = N", color=style.DIM, fontsize=10.5,
            rotation=41, ha="center", va="center")
    for s, color in [(0.01, GREEN), (0.05, CYAN), (0.10, ORANGE),
                     (0.25, PINK), (0.50, VIOLET)]:
        ax.plot(n, _amdahl(n, s), color=color)
        ax.text(140, _amdahl(128, s), f"s = {s * 100:.0f} %, limit {1 / s:.0f}",
                color=color, fontsize=10.5, va="center", ha="left")
    ax.set_xscale("log", base=2)
    ax.set_yscale("log", base=2)
    ax.set_xticks([1, 2, 4, 8, 16, 32, 64, 128])
    ax.set_xticklabels(["1", "2", "4", "8", "16", "32", "64", "128"])
    ax.set_yticks([1, 2, 4, 8, 16, 32, 64])
    ax.set_yticklabels(["1", "2", "4", "8", "16", "32", "64"])
    ax.set_xlim(1, 128)
    ax.set_ylim(1, 80)
    ax.set_xlabel("workers N")
    ax.set_ylabel("speed-up S(N)")
    style.save(fig, "viz_computing_amdahl")


def scaling():
    """Measured speed-up of the 1200-pass sum against Amdahl's prediction."""
    t_s, t_p = _serial_parts()
    s = t_s / (t_s + t_p)
    fig, ax = style.new_fig(5.2, 3.9)
    n = np.linspace(1, 12.5, 200)
    ax.plot(n, n, color=style.DIM, lw=1.2, ls="--", label="S = N")
    ax.plot(n, _amdahl(n, s), color=CYAN,
            label=f"Amdahl, s = {s * 100:.1f} %")
    speed = [T_PAR[0] / t for t in T_PAR]
    ax.plot(WORKERS, speed, "o", color=ORANGE, ms=9, label="measured", zorder=5)
    for w, sp in zip(WORKERS, speed):
        offset = (-34, -16) if w == WORKERS[-1] else (9, -14)
        ax.annotate(f"{sp:.2f}", (w, sp), textcoords="offset points",
                    xytext=offset, fontsize=10.5, color=ORANGE)
    ax.axvline(8, color=style.DIM, lw=1, ls=":")
    ax.text(8.15, 0.55, "8 performance cores", color=style.DIM, fontsize=9.5,
            ha="left", va="bottom")
    ax.set_xlim(0.5, 12.8)
    ax.set_ylim(0, 9)
    ax.set_xticks([1, 2, 4, 6, 8, 10, 12])
    ax.set_xlabel("worker processes N")
    ax.set_ylabel("speed-up T(1) / T(N)")
    ax.legend(loc="upper left")
    style.save(fig, "viz_computing_scaling")


def move_1tb():
    """Time to move one terabyte at five rates."""
    fig, ax = style.new_fig(6.4, 2.7)
    tb = 1e12
    rows = [
        ("memory to memory, 10 GB/s", tb / (RATE_MEMORY_COPY * 1e9), GREEN),
        ("SSD to memory, 4.4 GB/s", tb / (RATE_SSD_READ * 1e9), CYAN),
        ("network, 10 Gbit/s", tb * 8 / 10e9, ORANGE),
        ("network, 1 Gbit/s", tb * 8 / 1e9, PINK),
        ("network, 100 Mbit/s", tb * 8 / 100e6, VIOLET),
    ]

    def human(sec):
        if sec < 120:
            return f"{sec:.0f} s"
        if sec < 7200:
            return f"{sec / 60:.0f} min"
        return f"{sec / 3600:.0f} h"

    y = np.arange(len(rows))[::-1]
    for yi, (name, sec, color) in zip(y, rows):
        ax.barh(yi, sec - 10, color=color, height=0.6, left=10)
        ax.text(sec * 1.2, yi, human(sec), va="center", ha="left",
                fontsize=12, color=style.FG, fontweight="bold")
    ax.set_yticks(y)
    ax.set_yticklabels([r[0] for r in rows], fontsize=11.5, color=style.FG)
    ax.set_xscale("log")
    ax.set_xlim(10, 1.2e6)
    ax.set_xticks([60, 600, 3600, 36000, 86400 * 7])
    ax.set_xticklabels(["1 min", "10 min", "1 h", "10 h", "1 week"])
    ax.set_xlabel("time to move 1 TB")
    ax.grid(axis="y", visible=False)
    style.save(fig, "viz_computing_move_1tb")


def backfill():
    """A node of 8 cores: a short job starts in the gap, a long one waits."""
    fig, ax = style.new_fig(6.6, 3.1)

    def box(x, y, w, h, color, text, alpha=0.85, ls="-", fill=True):
        ax.add_patch(Rectangle((x, y), w, h, facecolor=color if fill else "none",
                               edgecolor=color, alpha=alpha, lw=1.8, ls=ls))
        ax.text(x + w / 2, y + h / 2, text, ha="center", va="center",
                fontsize=10.5, color="#0b0e14" if fill else color,
                fontweight="bold")

    box(0, 0, 2, 4, CYAN, "A  running\n4 cores, 2 h left")
    box(2, 0, 3, 8, ORANGE, "B  first in the queue\n8 cores, 3 h\nstarts when A ends")
    box(0, 4, 2, 4, GREEN, "C  4 cores, 2 h\nstarts now")
    box(5, 0, 4, 4, PINK, "D  4 cores, 4 h\nwaits until B ends", fill=False, ls="--")
    ax.axvline(0, color=style.FG, lw=1.2)
    ax.text(0.05, 8.35, "now", color=style.FG, fontsize=10.5, ha="left")
    ax.set_xlim(-0.2, 9.4)
    ax.set_ylim(0, 9.2)
    ax.set_xticks(range(0, 10))
    ax.set_yticks([0, 2, 4, 6, 8])
    ax.set_xlabel("hours from now")
    ax.set_ylabel("cores of the node")
    style.save(fig, "viz_computing_backfill")


FIGURES = {
    "three_ways": three_ways,
    "amdahl": amdahl,
    "scaling": scaling,
    "move_1tb": move_1tb,
    "backfill": backfill,
}

if __name__ == "__main__":
    style.use()
    for _name, _fn in FIGURES.items():
        _fn()
