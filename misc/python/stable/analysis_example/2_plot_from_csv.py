#!/usr/bin/env python3
import argparse
import numpy as np
import matplotlib.pyplot as plt
import csv

# --- Command-line arguments ---
parser = argparse.ArgumentParser(description="Generate Gaussian + exponential data and plot from CSV")
parser.add_argument("--mean", type=float, default=5.0, help="Mean of Gaussian signal")
parser.add_argument("--sigma", type=float, default=1.0, help="Sigma of Gaussian signal")
parser.add_argument("--n-signal", type=int, default=10000, help="Number of signal points")
parser.add_argument("--n-background", type=int, default=100000, help="Number of background points")
parser.add_argument("--output", type=str, default="sample.csv", help="Output CSV file name")
args = parser.parse_args()

# --- Read back from CSV ---
data = []
with open(args.output) as f:
    reader = csv.DictReader(f)
    for row in reader:
        x = float(row["data"])
        data.append(x)

# --- Plot ---
plt.hist(data, bins=50, alpha=0.5, label="Data", color="tab:blue")

plt.xlabel("x")
plt.ylabel("Entries")
plt.legend()
plt.show()

