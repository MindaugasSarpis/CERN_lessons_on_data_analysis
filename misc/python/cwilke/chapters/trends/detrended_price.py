"""Raw vs. detrended series: two-panel example (Wilke fig 14.10 concept)."""

from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np

from cwilke.theme import MUTED, PRIMARY_BLUE, apply_base, open_axes, save


def render() -> None:
    apply_base()
    rng = np.random.default_rng(21)
    n = 400
    t = np.arange(n)

    trend = 100 + 0.0006 * (t ** 2)                  # quadratic up
    seasonal = 8 * np.sin(2 * np.pi * t / 90.0)       # period 90
    noise = rng.normal(0, 2.5, n)
    raw = trend + seasonal + noise
    detrended = raw - trend

    fig, axes = plt.subplots(1, 2, figsize=(10.4, 4.0))

    ax1 = axes[0]
    ax1.plot(t, raw, color=PRIMARY_BLUE, linewidth=1.2, label="raw")
    ax1.plot(t, trend, color=MUTED, linewidth=1.6,
             linestyle="--", label="trend")
    ax1.set_title("raw series")
    ax1.set_xlabel("day")
    ax1.set_ylabel("price")
    ax1.legend(loc="upper left")
    open_axes(ax1)

    ax2 = axes[1]
    ax2.axhline(0, color=MUTED, linewidth=1.0, linestyle="--")
    ax2.plot(t, detrended, color=PRIMARY_BLUE, linewidth=1.2)
    ax2.set_title("detrended (raw − trend)")
    ax2.set_xlabel("day")
    ax2.set_ylabel("residual")
    open_axes(ax2)

    fig.tight_layout()
    save(fig, "trends", "detrended_price")


if __name__ == "__main__":
    render()
