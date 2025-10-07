#!/usr/bin/env python3
import argparse
import numpy as np
import matplotlib.pyplot as plt

# --- Command-line arguments ---
parser = argparse.ArgumentParser(description="Plot Gaussian + exponential mixture")
parser.add_argument("--mean", type=float, default=5.0, help="Mean of Gaussian signal")
parser.add_argument("--sigma", type=float, default=1.0, help="Sigma of Gaussian signal")
parser.add_argument("--n-signal", type=int, default=10000, help="Number of signal points")
parser.add_argument("--n-background", type=int, default=100000, help="Number of background points")
args = parser.parse_args()

# --- Generate data ---
gaussian_signal = np.random.normal(args.mean, args.sigma, args.n_signal)
exponential_background = np.random.exponential(scale=2.0, size=args.n_background)
all_data = np.concatenate([gaussian_signal, exponential_background])

# --- Plot ---
plt.hist(exponential_background, bins=50, alpha=0.5, label="Background (exp)", color="tab:blue")
plt.hist(gaussian_signal, bins=50, alpha=0.5, label="Signal (gauss)", color="tab:orange")
plt.hist(all_data, bins=50, histtype="step", linewidth=2, color="black", label="Total")

plt.xlabel("x")
plt.ylabel("Entries")
plt.legend()
plt.show()

