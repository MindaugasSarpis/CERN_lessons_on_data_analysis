"""3D bars of Virginia mortality (Wilke fig 26.7) — bad."""

from __future__ import annotations

import numpy as np
import matplotlib.pyplot as plt

from cwilke.data import va_deaths
from cwilke.theme import apply_base, save, stamp_bad


def render() -> None:
    apply_base()
    df = va_deaths()

    ages = list(df["age"].cat.categories)
    groups = ["Rural Female", "Rural Male", "Urban Female", "Urban Male"]

    fig = plt.figure(figsize=(6.4, 5.0))
    ax = fig.add_subplot(111, projection="3d")

    for yi, grp in enumerate(groups):
        xs = np.arange(len(ages))
        ys = np.full(len(ages), yi)
        zs = np.zeros(len(ages))
        dx = np.full(len(ages), 0.55)
        dy = np.full(len(ages), 0.55)
        dz = np.array([
            float(df[(df["age"] == age) & (df["group"] == grp)]["rate"].iloc[0])
            for age in ages
        ])
        ax.bar3d(xs, ys, zs, dx, dy, dz,
                 color="#56B4E9", edgecolor="#1f4e79",
                 linewidth=0.5, shade=True)

    ax.view_init(elev=22, azim=-65)
    ax.set_xticks(np.arange(len(ages)) + 0.28)
    ax.set_xticklabels(ages, fontsize=9)
    ax.set_yticks(np.arange(len(groups)) + 0.28)
    ax.set_yticklabels(groups, fontsize=9)
    ax.set_zlabel("deaths / 1000")
    ax.set_title("Virginia mortality, 1940 (3D — bad)")
    for pane in (ax.xaxis.pane, ax.yaxis.pane, ax.zaxis.pane):
        pane.set_edgecolor("#cfd8dc")
        pane.set_facecolor((1, 1, 1, 0))
    stamp_bad(fig)
    save(fig, "no_3d_jitter", "va_deaths_3d")


if __name__ == "__main__":
    render()
