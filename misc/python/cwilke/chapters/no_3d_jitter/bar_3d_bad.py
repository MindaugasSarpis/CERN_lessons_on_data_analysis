"""Fake-3D bar chart to illustrate why 3D distorts perception (Wilke ch. 26)."""

from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np

from cwilke.theme import OKABE_ITO, apply_base, save, stamp_bad


def render() -> None:
    apply_base()

    categories = ["A", "B", "C", "D", "E"]
    values = [23, 17, 35, 29, 12]
    colors = [OKABE_ITO[1], OKABE_ITO[2], OKABE_ITO[3],
              OKABE_ITO[5], OKABE_ITO[6]]

    fig = plt.figure(figsize=(7.0, 4.4))
    ax = fig.add_subplot(111, projection="3d")

    xs = np.arange(len(categories))
    ys = np.zeros(len(categories))
    zs = np.zeros(len(categories))
    dx = np.full(len(categories), 0.6)
    dy = np.full(len(categories), 0.6)
    dz = np.array(values, dtype=float)

    ax.bar3d(xs, ys, zs, dx, dy, dz, color=colors,
             edgecolor="#2c3e50", linewidth=0.6, shade=True)

    # skewed viewing angle to emphasise the distortion
    ax.view_init(elev=25, azim=-55)

    ax.set_xticks(xs + 0.3)
    ax.set_xticklabels(categories)
    ax.set_yticks([])
    ax.set_zlabel("value")
    ax.set_ylabel("")
    ax.set_xlabel("category")
    ax.set_title("3D bars distort comparison")

    # lighten panes
    for pane in (ax.xaxis.pane, ax.yaxis.pane, ax.zaxis.pane):
        pane.set_edgecolor("#cfd8dc")
        pane.set_facecolor((1, 1, 1, 0.0))

    stamp_bad(fig)
    save(fig, "no_3d_jitter", "bar_3d_bad")


if __name__ == "__main__":
    render()
