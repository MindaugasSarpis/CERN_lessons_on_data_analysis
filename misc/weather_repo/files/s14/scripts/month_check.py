#!/usr/bin/env python3
"""Is one month unusually warm or cold? Compare it with the same month of
the other years in data/raw/weather.csv.

The month itself stays hidden until --unblind is given, so the rule can be
written down before its value is seen.

Usage, from the project folder (macOS: python3, Windows: python):

    python3 scripts/month_check.py 2025 10              the other years only
    python3 scripts/month_check.py 2025 10 --unblind    and the month itself

Options for the checks of the method:

    --first YEAR   leave the years before YEAR out of the reference
    --minmax       a day's mean is (min + max) / 2, not the mean of 24 hours
    --pooled       the spread of all twelve months, not of this month only
"""
import argparse

import pandas as pd

parser = argparse.ArgumentParser()
parser.add_argument("year", type=int)
parser.add_argument("month", type=int)
parser.add_argument("--unblind", action="store_true")
parser.add_argument("--first", type=int, default=2016)
parser.add_argument("--minmax", action="store_true")
parser.add_argument("--pooled", action="store_true")
args = parser.parse_args()

hours = pd.read_csv("data/raw/weather.csv", na_values=[-999],
                    parse_dates=["time"], index_col="time")
temp = hours["temp_c"]
if args.minmax:
    days = (temp.resample("D").min() + temp.resample("D").max()) / 2
else:
    days = temp.resample("D").mean()
months = days.resample("MS").mean()
months = months[months.index.year >= args.first]

same = months[months.index.month == args.month]
ref = same[same.index.year != args.year]
first, last = ref.index.year.min(), ref.index.year.max()
print(f"{first} to {last}:", " ".join(f"{v:.2f}" for v in ref))

mean = ref.mean()
if args.pooled:
    # each month minus the mean of its own month over all years
    rest = months[months.index.year != args.year]
    dev = rest - rest.groupby(rest.index.month).transform("mean")
    sd = dev.std(ddof=12)
else:
    sd = ref.std()
print(f"reference  {len(ref)} years  mean {mean:.2f} °C  sd {sd:.2f} °C")

if args.unblind:
    value = same[same.index.year == args.year].iloc[0]
    z = (value - mean) / sd
    print(f"{args.year}-{args.month:02d}    mean {value:.2f} °C  z {z:+.2f}")
else:
    print(f"{args.year}-{args.month:02d}    hidden: run again with --unblind")
