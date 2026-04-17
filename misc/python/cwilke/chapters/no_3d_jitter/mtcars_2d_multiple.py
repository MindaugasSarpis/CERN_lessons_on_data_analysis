"""mpg vs displ and mpg vs hp, two 2D panels (Wilke fig 26.5)."""

from __future__ import annotations

import matplotlib.pyplot as plt

from cwilke.data import mtcars
from cwilke.theme import apply_base, open_axes, save


def render() -> None:
    apply_base()
    df = mtcars()
    colors = {4: "#0072B2", 6: "#CC79A7", 8: "#E69F00"}

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8.0, 3.8))
    for cyl in (4, 6, 8):
        sub = df[df["cyl"] == cyl]
        ax1.scatter(sub["disp"], sub["mpg"],
                    color=colors[cyl], s=38, edgecolors="none",
                    label=f"{cyl} cyl")
        ax2.scatter(sub["hp"], sub["mpg"],
                    color=colors[cyl], s=38, edgecolors="none",
                    label=f"{cyl} cyl")
    ax1.set_xlabel("displacement (cu. in.)")
    ax1.set_ylabel("efficiency (mpg)")
    ax2.set_xlabel("power (hp)")
    ax2.set_ylabel("efficiency (mpg)")
    ax2.legend(title="cylinders", loc="upper right")
    ax1.text(0.02, 0.96, "a", transform=ax1.transAxes,
             fontsize=13, fontweight="bold", va="top")
    ax2.text(0.02, 0.96, "b", transform=ax2.transAxes,
             fontsize=13, fontweight="bold", va="top")
    open_axes(ax1)
    open_axes(ax2)
    fig.tight_layout()
    save(fig, "no_3d_jitter", "mtcars_2d_multiple")


if __name__ == "__main__":
    render()
