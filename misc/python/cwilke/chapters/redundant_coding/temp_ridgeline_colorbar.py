"""Monthly temperature ridgelines with inline colour-bar x-axis (Wilke fig 20.12)."""

from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import gaussian_kde

from cwilke import data as D
from cwilke.theme import apply_base, save


MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]


def render() -> None:
    apply_base()

    df = D.lincoln_temps()

    tmin = df["mean_temp_F"].min() - 4
    tmax = df["mean_temp_F"].max() + 4
    grid_x = np.linspace(tmin, tmax, 400)

    # Use the YlOrRd ("heat"-style) colormap; temp → colour
    cmap = plt.get_cmap("YlOrRd")

    fig = plt.figure(figsize=(7.6, 5.0))
    gs = fig.add_gridspec(2, 1, height_ratios=(16, 1),
                          hspace=0.15, left=0.09, right=0.98,
                          top=0.96, bottom=0.10)
    ax = fig.add_subplot(gs[0])

    scale = 3.3
    for i, month in enumerate(reversed(MONTHS)):
        vals = df.loc[df["month"] == month, "mean_temp_F"].values
        if len(vals) < 5:
            continue
        kde = gaussian_kde(vals, bw_method=0.35)
        dens = kde(grid_x)
        dens_scaled = dens / dens.max() * scale
        base = i

        # colour each segment by its temperature
        for j in range(len(grid_x) - 1):
            c = cmap((grid_x[j] - tmin) / (tmax - tmin))
            ax.fill_between(grid_x[j:j + 2], base,
                            base + dens_scaled[j:j + 2],
                            color=c, linewidth=0)
        ax.plot(grid_x, base + dens_scaled, color="black", linewidth=0.6)

    ax.set_yticks(range(len(MONTHS)))
    ax.set_yticklabels(list(reversed(MONTHS)))
    ax.set_xlim(tmin, tmax)
    ax.set_ylim(-0.5, len(MONTHS) + 2.2)
    ax.set_xticks([])
    for spine in ("top", "right", "bottom"):
        ax.spines[spine].set_visible(False)
    ax.tick_params(axis="y", length=0)

    # Inline colour bar serving as x-axis
    cax = fig.add_subplot(gs[1])
    gradient = np.linspace(0, 1, 512).reshape(1, -1)
    cax.imshow(gradient, aspect="auto", cmap=cmap,
               extent=(tmin, tmax, 0, 1))
    for temp in (0, 25, 50, 75):
        cax.text(temp, 0.5, str(temp), ha="center", va="center",
                 fontsize=10, color="#2c3e50", fontweight="bold",
                 bbox=dict(facecolor="white", edgecolor="none",
                           pad=1.5, alpha=0.85))
    cax.set_xlim(tmin, tmax)
    cax.set_yticks([])
    for spine in cax.spines.values():
        spine.set_visible(False)
    cax.set_xlabel("mean temperature (°F)", fontsize=11)

    save(fig, "redundant_coding", "temp_ridgeline_colorbar")


if __name__ == "__main__":
    render()
