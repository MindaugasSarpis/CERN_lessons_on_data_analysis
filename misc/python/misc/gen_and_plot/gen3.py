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
parser.add_argument("--output", type=str, default="data.csv", help="Output CSV file name")
args = parser.parse_args()

# --- Generate data ---
gaussian_signal = np.random.normal(args.mean, args.sigma, args.n_signal)
exponential_background = np.random.exponential(scale=2.0, size=args.n_background)

# --- Save to CSV ---
with open(args.output, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["x", "label"])
    writer.writerows([[x, "signal"] for x in gaussian_signal])
    writer.writerows([[x, "background"] for x in exponential_background])

print(f"Data saved to {args.output}")

# --- Read back from CSV ---
signal, background = [], []
with open(args.output) as f:
    reader = csv.DictReader(f)
    for row in reader:
        x = float(row["x"])
        if row["label"] == "signal":
            signal.append(x)
        else:
            background.append(x)

# --- Plot ---
plt.hist(background, bins=50, alpha=0.5, label="Background (exp)", color="tab:blue")
plt.hist(signal, bins=50, alpha=0.5, label="Signal (gauss)", color="tab:orange")
plt.hist(signal + background, bins=50, histtype="step", linewidth=2, color="black", label="Total")

plt.xlabel("x")
plt.ylabel("Entries")
plt.legend()
plt.show()

