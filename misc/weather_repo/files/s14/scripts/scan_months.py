#!/usr/bin/env python3
"""Check every month of 2016 to 2025 the way month_check.py checks one:
z = (the month - the mean of the same month in the other nine years) / sd.

Usage, from the project folder (macOS: python3, Windows: python):

    python3 scripts/scan_months.py            sd of the same month
    python3 scripts/scan_months.py --pooled   sd of all twelve months
"""
import argparse

import pandas as pd

parser = argparse.ArgumentParser()
parser.add_argument("--pooled", action="store_true")
args = parser.parse_args()

hours = pd.read_csv("data/raw/weather.csv", na_values=[-999],
                    parse_dates=["time"], index_col="time")
months = hours["temp_c"].resample("D").mean().resample("MS").mean()

rows = []
for when, value in months.items():
    rest = months[months.index.year != when.year]
    ref = rest[rest.index.month == when.month]
    if args.pooled:
        dev = rest - rest.groupby(rest.index.month).transform("mean")
        sd = dev.std(ddof=12)
    else:
        sd = ref.std()
    rows.append((when, value, (value - ref.mean()) / sd))

beyond = [r for r in rows if abs(r[2]) > 2]
print(f"months checked {len(rows)}   beyond 2 sd {len(beyond)}")
for when, value, z in sorted(rows, key=lambda r: -abs(r[2]))[:5]:
    print(f"{when:%Y-%m}  mean {value:6.2f} °C  z {z:+.2f}")
