"""Lincoln daily temperatures: raw scatter + smoothed curve (Wilke fig 14.2)."""

from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np

from cwilke import data as D
from cwilke.theme import BAD, MUTED, apply_base, open_axes, save


def _running_mean(y: np.ndarray, window: int = 31) -> np.ndarray:
    """Centered running mean with edge-truncated windows."""
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

    fig, ax = plt.subplots(figsize=(7.0, 4.2))
    ax.scatter(x, y, s=16, color=MUTED, alpha=0.6,
               edgecolors="none", label="daily mean")
    ax.plot(x, smooth, color=BAD, linewidth=2.2, label="smoothed")
    ax.set_xlabel("day of the year")
    ax.set_ylabel("mean temperature (°F)")
    ax.legend(loc="lower center", ncol=2)
    open_axes(ax)
    save(fig, "trends", "lincoln_temps_raw_smooth")


if __name__ == "__main__":
    render()
