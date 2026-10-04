"""Fit a straight line to T^2 against L and compute g."""
import argparse
import json
import math

import pandas as pd
from scipy.optimize import curve_fit


def line(x, slope, intercept):
    return slope * x + intercept


def line_through_origin(x, slope):
    return slope * x


def g_from_slope(slope):
    """Return g in m/s^2 from the slope of T^2 against L in s^2/m."""
    return 4 * math.pi**2 / slope


def fit_g(length_m, period_s, through_origin=False):
    """Return g and its uncertainty, both in m/s^2."""
    model = line
    if through_origin:
        model = line_through_origin
    values, covariance = curve_fit(model, length_m, period_s**2)
    slope = values[0]
    slope_error = math.sqrt(covariance[0, 0])
    g = g_from_slope(slope)
    return g, g * slope_error / slope


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("table", help="cleaned CSV file")
    parser.add_argument("config", help="JSON file with the parameters")
    parser.add_argument("out", help="JSON file to write")
    args = parser.parse_args()

    table = pd.read_csv(args.table)
    with open(args.config) as f:
        config = json.load(f)

    g, g_error = fit_g(table["length_cm"] / 100,
                       table["t10_s"] / config["swings"],
                       config["through_origin"])
    result = {
        "g": round(g, 3),
        "g_error": round(g_error, 3),
        "points": len(table),
        "through_origin": config["through_origin"],
    }
    with open(args.out, "w", newline="\n") as f:
        json.dump(result, f, indent=2)
        f.write("\n")
    print(f"{args.out}: g = {g:.2f} +- {g_error:.2f} m/s^2")


if __name__ == "__main__":
    main()
