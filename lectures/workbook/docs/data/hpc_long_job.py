"""A longer job that reports its progress, one line per step."""
import argparse
import time

import numpy as np


def loop_sum(values, passes):
    total = 0.0
    for _ in range(passes):
        for v in values:
            total += v
    return total


def now():
    return time.strftime("%H:%M:%S")


parser = argparse.ArgumentParser()
parser.add_argument("--steps", type=int, default=60)
parser.add_argument("--path", default="data/raw/D0_KPi.csv")
args = parser.parse_args()

start = time.perf_counter()
M = np.loadtxt(args.path, delimiter=",", skiprows=1, usecols=0)
masses = M.tolist()
print(f"{now()}  read {len(masses)} rows from {args.path}")

for step in range(1, args.steps + 1):
    total = loop_sum(masses, 300)
    elapsed = time.perf_counter() - start
    print(f"{now()}  step {step:2d} of {args.steps}  {elapsed:5.1f} s")

mean = total / 300 / len(masses)
print(f"{now()}  done  mean of M = {mean:.4f}")
