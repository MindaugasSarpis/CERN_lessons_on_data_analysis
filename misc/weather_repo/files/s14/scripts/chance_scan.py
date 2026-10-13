#!/usr/bin/env python3
"""How many months beyond 2 sd does chance alone give in ten years?

Draws ten years of twelve monthly means from one normal distribution, in
which no month is unusual, scans them as scan_months.py does, and repeats
that for many decades.

Usage, from the project folder (macOS: python3, Windows: python):

    python3 scripts/chance_scan.py
"""
import numpy as np

rng = np.random.default_rng(2026)
decades = 2000
counts = []
largest = []
for _ in range(decades):
    months = rng.normal(0, 1, size=(10, 12))  # 10 years, 12 months
    z = np.empty_like(months)
    for y in range(10):
        ref = np.delete(months, y, axis=0)    # the other nine years
        z[y] = (months[y] - ref.mean(axis=0)) / ref.std(axis=0, ddof=1)
    counts.append(np.sum(np.abs(z) > 2))
    largest.append(np.abs(z).max())

counts = np.array(counts)
largest = np.array(largest)
print(f"decades of pure chance  {decades}")
print(f"months beyond 2 sd, on average  {counts.mean():.1f} of 120")
print(f"decades with at least one       {np.mean(counts > 0):.1%}")
print(f"largest z of a decade, median    {np.median(largest):.1f}")
