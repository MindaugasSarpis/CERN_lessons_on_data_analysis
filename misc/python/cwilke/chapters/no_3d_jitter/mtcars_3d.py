"""Four 3D scatter views of mtcars (displ, hp, mpg) (Wilke fig 26.3)."""

from __future__ import annotations

import matplotlib.pyplot as plt

from cwilke.data import mtcars
from cwilke.theme import apply_base, save, stamp_bad


def _panel(fig, pos, theta, phi, df, colors, title, *, axes=True):
    ax = fig.add_subplot(pos, projection="3d")
    for cyl in (4, 6, 8):
        sub = df[df["cyl"] == cyl]
        ax.scatter(sub["disp"], sub["hp"], sub["mpg"],
                   color=colors[cyl], s=30, edgecolors="none",
                   label=f"{cyl} cyl")
    ax.view_init(elev=phi, azim=theta)
    if axes:
        ax.set_xlabel("displ.", fontsize=9)
        ax.set_ylabel("power", fontsize=9)
        ax.set_zlabel("mpg", fontsize=9)
        for pane in (ax.xaxis.pane, ax.yaxis.pane, ax.zaxis.pane):
            pane.set_edgecolor("#cfd8dc")
            pane.set_facecolor((1, 1, 1, 0))
    else:
        ax.set_axis_off()
    ax.set_title(title, fontsize=10)
    return ax


def render(axes: bool = True, name: str = "mtcars_3d") -> None:
    apply_base()
    df = mtcars()
    colors = {4: "#0072B2", 6: "#CC79A7", 8: "#E69F00"}

    fig = plt.figure(figsize=(8.2, 7.2))
    _panel(fig, 221, 30, 20, df, colors, "(a) theta=30, phi=20", axes=axes)
    _panel(fig, 222, -30, 20, df, colors, "(b) theta=-30, phi=20", axes=axes)
    _panel(fig, 223, 30, 40, df, colors, "(c) theta=30, phi=40", axes=axes)
    _panel(fig, 224, -30, 40, df, colors, "(d) theta=-30, phi=40", axes=axes)

    handles = [plt.Line2D([0], [0], marker="o", linestyle="",
                          color=colors[c], label=f"{c} cyl")
               for c in (4, 6, 8)]
    fig.legend(handles=handles, loc="upper center", ncol=3, frameon=False,
               bbox_to_anchor=(0.5, 1.02))
    fig.subplots_adjust(wspace=0.02, hspace=0.12)
    stamp_bad(fig)
    save(fig, "no_3d_jitter", name)


if __name__ == "__main__":
    render()
