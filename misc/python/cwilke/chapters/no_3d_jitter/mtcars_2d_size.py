"""Bubble-size encoding of mpg in a hp-vs-displ scatter (Wilke fig 26.6)."""

from __future__ import annotations

import numpy as np
import matplotlib.pyplot as plt

from cwilke.data import mtcars
from cwilke.theme import apply_base, open_axes, save


def render() -> None:
    apply_base()
    df = mtcars()
    colors = {4: "#0072B2", 6: "#CC79A7", 8: "#E69F00"}

    # Map mpg to marker size.
    mpg = df["mpg"].values
    # size in points^2: scale so 10 mpg -> 40, 30 mpg -> 300
    sizes = np.interp(mpg, (10, 35), (40, 380))

    fig, ax = plt.subplots(figsize=(6.6, 4.8))
    for cyl in (4, 6, 8):
        mask = df["cyl"] == cyl
        ax.scatter(df.loc[mask, "disp"], df.loc[mask, "hp"],
                   s=sizes[mask.values], c=colors[cyl],
                   edgecolors="white", linewidths=1.0,
                   alpha=0.85, label=f"{cyl} cyl")

    ax.set_xlabel("displacement (cu. in.)")
    ax.set_ylabel("power (hp)")

    # size legend
    for mpg_v, label in [(10, "10"), (20, "20"), (30, "30")]:
        s = np.interp(mpg_v, (10, 35), (40, 380))
        ax.scatter([], [], s=s, c="gray", alpha=0.6, edgecolors="white",
                   label=f"mpg = {label}")
    ax.legend(loc="upper right", labelspacing=1.1, fontsize=10,
              frameon=False)
    open_axes(ax)
    save(fig, "no_3d_jitter", "mtcars_2d_size")


if __name__ == "__main__":
    render()
