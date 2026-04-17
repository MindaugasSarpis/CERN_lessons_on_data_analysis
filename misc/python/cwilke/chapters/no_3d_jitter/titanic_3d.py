"""3D stacked bar chart of Titanic passengers — bad (Wilke fig 26.2)."""

from __future__ import annotations

import numpy as np
import matplotlib.pyplot as plt

from cwilke.data import titanic_counts
from cwilke.theme import apply_base, save, stamp_bad


def render() -> None:
    apply_base()
    df = titanic_counts()

    classes = ["1st", "2nd", "3rd"]
    sexes = ["female", "male"]
    colors = {"female": "#E69F00", "male": "#56B4E9"}

    fig = plt.figure(figsize=(6.8, 5.0))
    ax = fig.add_subplot(111, projection="3d")

    for yi, sex in enumerate(sexes):
        xs, ys, zs, dxs, dys, dzs = [], [], [], [], [], []
        for xi, cls in enumerate(classes):
            cnt = int(df[(df["class"] == cls) & (df["sex"] == sex)]["count"].iloc[0])
            xs.append(xi)
            ys.append(yi)
            zs.append(0)
            dxs.append(0.55)
            dys.append(0.55)
            dzs.append(cnt)
        ax.bar3d(xs, ys, zs, dxs, dys, dzs,
                 color=colors[sex], edgecolor="#2c3e50",
                 linewidth=0.6, shade=True, label=sex)

    ax.view_init(elev=22, azim=-55)
    ax.set_xticks(np.arange(3) + 0.28)
    ax.set_xticklabels(classes)
    ax.set_yticks(np.arange(2) + 0.28)
    ax.set_yticklabels(sexes)
    ax.set_zlabel("passengers")
    ax.set_xlabel("class")
    ax.set_title("3D bars hide true heights")
    for pane in (ax.xaxis.pane, ax.yaxis.pane, ax.zaxis.pane):
        pane.set_edgecolor("#cfd8dc")
        pane.set_facecolor((1, 1, 1, 0))
    stamp_bad(fig)
    save(fig, "no_3d_jitter", "titanic_3d")


if __name__ == "__main__":
    render()
