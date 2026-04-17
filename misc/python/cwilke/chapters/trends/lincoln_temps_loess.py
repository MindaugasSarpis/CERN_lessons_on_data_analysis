"""Lincoln temperatures: smooth curve with SE band (Wilke fig 14.3)."""

from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np

from cwilke import data as D
from cwilke.theme import BAD, apply_base, open_axes, save


def _running_mean(y: np.ndarray, window: int = 31) -> np.ndarray:
    n = len(y)
    out = np.empty(n)
    half = window // 2
    for i in range(n):
        lo = max(0, i - half)
        hi = min(n, i + half + 1)
        out[i] = y[lo:hi].mean()
    return out


def render() -> None:
    apply_base()
    df = D.lincoln_temps()
    x = df["day"].values
    y = df["mean_temp_F"].values
    smooth = _running_mean(y, window=31)
    resid = y - smooth
    se = 2.0 * resid.std()

    fig, ax = plt.subplots(figsize=(7.0, 4.2))
    ax.fill_between(x, smooth - se, smooth + se,
                    color=BAD, alpha=0.18, linewidth=0,
                    label="±2 SD")
    ax.plot(x, smooth, color=BAD, linewidth=2.6, label="smoothed")
    ax.set_xlabel("day of the year")
    ax.set_ylabel("mean temperature (°F)")
    ax.legend(loc="lower center", ncol=2)
    open_axes(ax)
    save(fig, "trends", "lincoln_temps_loess")


if __name__ == "__main__":
    render()
