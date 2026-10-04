"""Clean the raw pendulum file: write a plain CSV table."""
import argparse

import pandas as pd


def clean(path):
    """Return the measurements in the raw file as a table."""
    raw = pd.read_csv(path, sep=";", decimal=",")
    rows = raw[raw["nr"].notna()]      # the mean line has no number
    table = rows[["length_cm", "t10_s"]]
    return table.astype({"length_cm": int})   # was text: "mean"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("raw", help="file as received")
    parser.add_argument("out", help="cleaned CSV file to write")
    args = parser.parse_args()

    table = clean(args.raw)
    table.to_csv(args.out, index=False, float_format="%.2f",
                 lineterminator="\n")
    print(f"{args.out}: {len(table)} rows")


if __name__ == "__main__":
    main()
