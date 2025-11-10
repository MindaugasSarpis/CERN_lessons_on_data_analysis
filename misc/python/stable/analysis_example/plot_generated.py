#!/usr/bin/env python3
"""
Plot a histogram of Gaussian+Exponential mixture from CSV file.
Assumes CSV columns: id, x, label, component
"""
import csv
import numpy as np
import matplotlib.pyplot as plt
import argparse

def read_csv_values(filename):
    """Read 'x' and 'label' columns from the generated CSV."""
    xs_signal = []
    xs_bkg = []
    with open(filename, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            x = float(row["x"])
            if row["label"] == "signal":
                xs_signal.append(x)
            else:
                xs_bkg.append(x)
    return np.array(xs_signal), np.array(xs_bkg)

def main():
    parser = argparse.ArgumentParser(description="Plot Gaussian+Exponential mixture histogram from CSV.")
    parser.add_argument("filename", help="Input CSV file (from gen_mixture.py).")
    parser.add_argument("--bins", type=int, default=50, help="Number of histogram bins.")
    parser.add_argument("--out", type=str, help="Optional PNG filename to save the plot.")
    args = parser.parse_args()

    xs_signal, xs_bkg = read_csv_values(args.filename)
    xs_all = np.concatenate([xs_signal, xs_bkg])

    plt.figure(figsize=(8, 5))
    plt.hist(xs_bkg, bins=args.bins, alpha=0.5, label="Background (exp)", color="tab:blue")
    plt.hist(xs_signal, bins=args.bins, alpha=0.6, label="Signal (gauss)", color="tab:orange")
    plt.hist(xs_all, bins=args.bins, histtype="step", linewidth=2, color="black", label="Total")

    plt.xlabel("x")
    plt.ylabel("Events / bin")
    plt.title("Gaussian + Exponential Mixture")
    plt.legend()
    plt.grid(alpha=0.3)
    plt.tight_layout()

    if args.out:
        plt.savefig(args.out, dpi=150)
        print(f"Saved plot to {args.out}")
    else:
        plt.show()

if __name__ == "__main__":
    main()
