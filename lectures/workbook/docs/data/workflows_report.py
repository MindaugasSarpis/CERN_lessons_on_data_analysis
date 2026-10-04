"""Write the report: the table, the plot and the value of g."""
import argparse
import json
from pathlib import Path

import pandas as pd


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("table", help="cleaned CSV file")
    parser.add_argument("fit", help="JSON file written by fit.py")
    parser.add_argument("figure", help="PNG file written by plot.py")
    parser.add_argument("out", help="Markdown file to write")
    args = parser.parse_args()

    table = pd.read_csv(args.table)
    with open(args.fit) as f:
        fit = json.load(f)
    figure = Path(args.figure).name    # it sits beside the report
    g = f"{fit['g']:.2f} ± {fit['g_error']:.2f} m/s²"

    lines = ["# Pendulum", "",
             f"Time of 10 swings for {len(table)} lengths.", "",
             "| length_cm | t10_s |",
             "|--:|--:|"]
    for row in table.itertuples():
        lines.append(f"| {row.length_cm} | {row.t10_s:.2f} |")
    lines += ["",
              f"![Time of 10 swings against length]({figure})", "",
              f"A straight-line fit of T² against L gives g = {g}."]

    with open(args.out, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(lines) + "\n")
    print(f"{args.out}: {len(lines)} lines")


if __name__ == "__main__":
    main()
