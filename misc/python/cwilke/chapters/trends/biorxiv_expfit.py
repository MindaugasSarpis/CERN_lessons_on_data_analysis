"""Monthly bioRxiv submissions with exponential fit (Wilke fig 14.8)."""

from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np

from cwilke import data as D
from cwilke.theme import PRIMARY_BLUE, apply_base, open_axes, save


def render() -> None:
    apply_base()
    df = D.biorxiv_growth()
    # fit log-linearly: log(count) = log(A) + b*(year - 2014)
    t = df["date_dec"].values - 2014
    logy = np.log(df["count"].values)
    b, logA = np.polyfit(t, logy, 1)[::-1]
    # polyfit returns [slope, intercept]; we want intercept as logA
    # actually polyfit(x, y, 1) returns [slope, intercept]
    slope, intercept = np.polyfit(t, logy, 1)
    A = np.exp(intercept)
    b = slope
    xs = np.linspace(t.min(), t.max(), 200)
    ys = A * np.exp(b * xs)

    fig, ax = plt.subplots(figsize=(6.4, 4.4))
    ax.plot(xs + 2014, ys, color="black", linewidth=1.2,
            linestyle="--", label="exponential fit")
    ax.plot(df["date_dec"], df["count"],
            color=PRIMARY_BLUE, linewidth=0.8)
    ax.scatter(df["date_dec"], df["count"], s=30,
               facecolors=PRIMARY_BLUE, edgecolors="white",
               linewidths=0.6, zorder=3, label="actual counts")
    ax.set_ylim(0, 1550)
    ax.set_ylabel("preprints / month")
    ax.legend(loc="upper left", frameon=False)
    open_axes(ax)
    save(fig, "trends", "biorxiv_expfit")


if __name__ == "__main__":
    render()
