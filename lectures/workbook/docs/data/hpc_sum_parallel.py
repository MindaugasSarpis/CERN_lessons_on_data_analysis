"""Add up the mass column many times over, split over processes."""
import argparse
import time
from multiprocessing import Pool

import numpy as np

PATH = "data/raw/D0_KPi.csv"


def sum_passes(passes):
    M = np.loadtxt(PATH, delimiter=",", skiprows=1, usecols=0)
    masses = M.tolist()
    total = 0.0
    for _ in range(passes):
        for m in masses:
            total += m
    return total


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--workers", type=int, default=4)
    parser.add_argument("--passes", type=int, default=1200)
    args = parser.parse_args()

    start = time.perf_counter()
    share = args.passes // args.workers
    with Pool(args.workers) as pool:
        parts = pool.map(sum_passes, [share] * args.workers)
    elapsed = time.perf_counter() - start
    print(f"workers {args.workers:2d}  passes {share * args.workers}"
          f"  time {elapsed:6.3f} s  sum {sum(parts)!r}")
