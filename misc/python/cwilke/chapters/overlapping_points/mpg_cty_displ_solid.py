"""mpg cty vs displ — solid opaque circles (Wilke fig 18.1, bad)."""

from __future__ import annotations

import matplotlib.pyplot as plt

from cwilke import data as D
from cwilke.theme import apply_base, open_axes, save, stamp_bad


DRV_COLORS = {"f": "#E69F00", "r": "#56B4E9", "4": "#202020"}
DRV_LABELS = {"f": "FWD", "r": "RWD", "4": "4WD"}


def render() -> None:
    apply_base()
    df = D.mpg()

    fig, ax = plt.subplots(figsize=(6.2, 4.4))
    for k in ("f", "r", "4"):
        sub = df[df["drv"] == k]
        ax.scatter(sub["displ"], sub["cty"],
                   s=55, facecolors=DRV_COLORS[k],
                   edgecolors="white", linewidths=0.6,
                   label=DRV_LABELS[k])
    ax.set_xlabel("displacement (l)")
    ax.set_ylabel("fuel economy (mpg)")
    ax.legend(title="drive train", loc="upper right", frameon=False)
    open_axes(ax)
    stamp_bad(fig)
    save(fig, "overlapping_points", "mpg_cty_displ_solid")


if __name__ == "__main__":
    render()
