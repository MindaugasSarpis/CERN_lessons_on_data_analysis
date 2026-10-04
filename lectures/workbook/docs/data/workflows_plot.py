"""Plot the time of 10 swings against the length."""
import argparse

import matplotlib.pyplot as plt
import pandas as pd


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("table", help="cleaned CSV file")
    parser.add_argument("out", help="PNG file to write")
    parser.add_argument("--dpi", type=int, default=150,
                        help="dots per inch (default: 150)")
    args = parser.parse_args()

    table = pd.read_csv(args.table)
    fig, ax = plt.subplots(figsize=(4.8, 3.2))
    ax.plot(table["length_cm"], table["t10_s"], "o")
    ax.set_xlabel("length (cm)")
    ax.set_ylabel("time of 10 swings (s)")
    ax.grid(True, linewidth=0.5, alpha=0.5)
    fig.tight_layout()
    fig.savefig(args.out, dpi=args.dpi)
    print(f"{args.out}: {len(table)} points")


if __name__ == "__main__":
    main()
