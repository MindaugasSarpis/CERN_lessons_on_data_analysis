#!/usr/bin/env python3
"""The warmest 30 days of each year in data/raw/weather.csv: the 720 hours
in a row with the highest mean temperature. The 120 hours marked -999 are
left out.

Usage, from the project folder:

    python scripts/warmest.py                    each year reads the file
    python scripts/warmest.py --read once        the file is read once
    python scripts/warmest.py --method numpy     the windows in NumPy
    python scripts/warmest.py --method running   a running sum
    python scripts/warmest.py --workers 4        four years at a time

At the end it prints the seconds spent reading, the seconds spent on the
windows, and the total.
"""
import argparse
import csv
import time
from multiprocessing import Pool

import numpy as np

PATH = "data/raw/weather.csv"
WINDOW = 720  # hours: 30 days
YEARS = range(2016, 2026)


def read_year(year):
    """Read the whole file, keep the rows of one year."""
    times, temps = [], []
    with open(PATH, newline="") as handle:
        for row in csv.DictReader(handle):
            if row["time"].startswith(str(year)) and row["temp_c"] != "-999":
                times.append(row["time"])
                temps.append(float(row["temp_c"]))
    return times, temps


def read_all():
    """Read the whole file once, sort the rows by year."""
    data = {year: ([], []) for year in YEARS}
    with open(PATH, newline="") as handle:
        for row in csv.DictReader(handle):
            if row["temp_c"] != "-999":
                times, temps = data[int(row["time"][:4])]
                times.append(row["time"])
                temps.append(float(row["temp_c"]))
    return data


def means_loop(temps):
    """Add up the 720 values of every window, one window after the other."""
    means = []
    for start in range(len(temps) - WINDOW + 1):
        total = 0.0
        for value in temps[start:start + WINDOW]:
            total += value
        means.append(total / WINDOW)
    return means


def means_running(temps):
    """Move the window by one hour: add the new value, drop the old one."""
    total = sum(temps[:WINDOW])
    means = [total / WINDOW]
    for start in range(1, len(temps) - WINDOW + 1):
        total += temps[start + WINDOW - 1] - temps[start - 1]
        means.append(total / WINDOW)
    return means


def means_numpy(temps):
    """All windows at once, from the cumulative sum."""
    c = np.cumsum(np.concatenate(([0.0], temps)))
    return (c[WINDOW:] - c[:-WINDOW]) / WINDOW


METHODS = {"loop": means_loop, "running": means_running,
           "numpy": means_numpy}


def warmest(job):
    """One year: read it (unless given), find its warmest window."""
    year, method, given = job
    t0 = time.perf_counter()
    times, temps = given if given else read_year(year)
    t1 = time.perf_counter()
    means = METHODS[method](temps)
    best = int(np.argmax(means))
    t2 = time.perf_counter()
    return year, times[best][:10], float(means[best]), t1 - t0, t2 - t1


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--method", default="loop", choices=METHODS)
    parser.add_argument("--read", default="each", choices=["each", "once"])
    parser.add_argument("--workers", type=int, default=1)
    args = parser.parse_args()

    start = time.perf_counter()
    if args.read == "once":
        data = read_all()
        jobs = [(year, args.method, data[year]) for year in YEARS]
    else:
        jobs = [(year, args.method, None) for year in YEARS]
    reading = time.perf_counter() - start

    if args.workers == 1:
        results = [warmest(job) for job in jobs]
    else:
        with Pool(args.workers) as pool:
            results = pool.map(warmest, jobs)
    total = time.perf_counter() - start

    for year, first_day, mean, _, _ in results:
        print(f"{year}  from {first_day}  {mean:.2f} °C")
    if args.workers == 1:
        reading += sum(r[3] for r in results)
        windows = sum(r[4] for r in results)
        print(f"read {reading:.2f} s  windows {windows:.2f} s  "
              f"total {total:.2f} s")
    else:
        print(f"workers {args.workers}  total {total:.2f} s")


if __name__ == "__main__":
    main()
