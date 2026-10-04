"""Time one sum three ways: a Python loop, NumPy, four processes."""
import time
from multiprocessing import Pool

import numpy as np

PATH = "data/raw/D0_KPi.csv"


def loop_sum(values):
    total = 0.0
    for v in values:
        total += v
    return total


if __name__ == "__main__":
    start = time.perf_counter()
    M = np.loadtxt(PATH, delimiter=",", skiprows=1, usecols=0)
    elapsed = time.perf_counter() - start
    print(f"read   {elapsed * 1000:8.3f} ms  {len(M)} rows")
    masses = M.tolist()

    for attempt in range(5):
        start = time.perf_counter()
        total = loop_sum(masses)
        elapsed = time.perf_counter() - start
        print(f"loop   {elapsed * 1000:8.3f} ms  {total!r}")

    for attempt in range(5):
        start = time.perf_counter()
        total = M.sum()
        elapsed = time.perf_counter() - start
        print(f"numpy  {elapsed * 1000:8.3f} ms  {float(total)!r}")

    chunks = [masses[i::4] for i in range(4)]
    for attempt in range(5):
        start = time.perf_counter()
        with Pool(4) as pool:
            parts = pool.map(loop_sum, chunks)
        total = sum(parts)
        elapsed = time.perf_counter() - start
        print(f"pool   {elapsed * 1000:8.3f} ms  {total!r}")
