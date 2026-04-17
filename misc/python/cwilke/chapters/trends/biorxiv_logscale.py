"""Monthly bioRxiv submissions on a log y-axis (Wilke fig 14.9)."""

from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np

from cwilke import data as D
from cwilke.theme import PRIMARY_BLUE, apply_base, open_axes, save


def render() -> None:
    apply_base()
    df = D.biorxiv_growth()
    t = df["date_dec"].values - 2014
    slope, intercept = np.polyfit(t, np.log(df["count"].values), 1)
    A = np.exp(intercept)
    b = slope
    xs = np.linspace(t.min(), t.max(), 200)
    ys = A * np.exp(b * xs)

    fig, ax = plt.subplots(figsize=(6.4, 4.4))
    ax.plot(xs + 2014, ys, color="black", linewidth=1.0,
            label="linear fit, log-transformed data")
    ax.plot(df["date_dec"], df["count"],
            color=PRIMARY_BLUE, linewidth=0.8)
    ax.scatter(df["date_dec"], df["count"], s=30,
               facecolors=PRIMARY_BLUE, edgecolors="white",
               linewidths=0.6, zorder=3, label="actual counts")
    ax.set_yscale("log")
    ax.set_ylim(30, 1800)
    ax.set_yticks([50, 100, 500, 1000])
    ax.set_yticklabels(["50", "100", "500", "1000"])
    ax.set_ylabel("preprints / month")
    ax.legend(loc="upper left", frameon=False)
    open_axes(ax)
    save(fig, "trends", "biorxiv_logscale")


if __name__ == "__main__":
    render()
