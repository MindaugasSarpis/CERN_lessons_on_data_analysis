#!/usr/bin/env python3
"""Plot the pendulum example used in Lecture 2 and Seminar 1.

Reads `pendulum.csv` (the cleaned file: comma between values, decimal point)
and writes `pendulum_plot.png` next to it. The same picture is copied to the
slides' `public/figures/`, where the Markdown image slide shows it.

The values are example values, written for the exercise: the time of 10 swings
of a pendulum for nine lengths, close to T = 2*pi*sqrt(L/g).

Usage:  python pendulum_plot.py      (needs matplotlib)
"""
import csv
import shutil
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = Path(__file__).resolve().parent
SLIDES = HERE.parents[2] / "content" / "public" / "figures"


def main():
    with open(HERE / "pendulum.csv", newline="") as f:
        rows = list(csv.DictReader(f))
    length = [float(r["length_cm"]) for r in rows]
    t10 = [float(r["t10_s"]) for r in rows]

    fig, ax = plt.subplots(figsize=(4.8, 3.2), dpi=150)
    ax.plot(length, t10, "o", color="#1f6feb")
    ax.set_xlabel("length (cm)")
    ax.set_ylabel("time of 10 swings (s)")
    ax.set_xlim(0, 110)
    ax.set_ylim(0, 22)
    ax.grid(True, linewidth=0.5, alpha=0.5)
    fig.tight_layout()

    out = HERE / "pendulum_plot.png"
    # No timestamp in the file, so a rerun gives the same bytes.
    fig.savefig(out, metadata={"Software": None})
    shutil.copyfile(out, SLIDES / "pendulum_plot.png")


if __name__ == "__main__":
    main()
