"""mpg cty vs displ — too much jitter distorts the data (Wilke fig 18.4, bad)."""

from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np

from cwilke import data as D
from cwilke.theme import apply_base, open_axes, save, stamp_bad


DRV_COLORS = {"f": "#E69F00", "r": "#56B4E9", "4": "#202020"}
DRV_LABELS = {"f": "FWD", "r": "RWD", "4": "4WD"}


def render() -> None:
    apply_base()
    df = D.mpg()
    rng = np.random.default_rng(42)
    x_amp = 0.10 * (df["displ"].max() - df["displ"].min())
    y_amp = 0.10 * (df["cty"].max() - df["cty"].min())

    fig, ax = plt.subplots(figsize=(6.2, 4.4))
    for k in ("f", "r", "4"):
        sub = df[df["drv"] == k]
        jx = sub["displ"] + rng.normal(0, x_amp, len(sub))
        jy = sub["cty"] + rng.normal(0, y_amp, len(sub))
        ax.scatter(jx, jy, s=55, facecolors=DRV_COLORS[k] + "80",
                   edgecolors=DRV_COLORS[k], linewidths=0.7,
                   label=DRV_LABELS[k])
    ax.set_xlabel("displacement (l)")
    ax.set_ylabel("fuel economy (mpg)")
    ax.legend(title="drive train", loc="upper right", frameon=False)
    open_axes(ax)
    stamp_bad(fig)
    save(fig, "overlapping_points", "mpg_cty_displ_jitter_extreme")


if __name__ == "__main__":
    render()
