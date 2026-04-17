"""Monthly mean temperature as a heatmap (Wilke fig 2.4).

Swap the position/colour roles from the line plot: now temperature is
colour, month is x, location is y.
"""

from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np

from cwilke import data as D
from cwilke.theme import apply_base, save


def render() -> None:
    apply_base()
    df = D.ncdc_normals_4locs()

    month_names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
                   "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    df["month"] = df["month"].astype("category")

    monthly = (df.groupby(["location", "month"], observed=True)["temperature"]
               .mean().reset_index())

    # Order rows coldest to warmest overall
    loc_order = (monthly.groupby("location")["temperature"].mean()
                 .sort_values().index.tolist())

    grid_vals = np.zeros((len(loc_order), len(month_names)))
    for i, loc in enumerate(loc_order):
        for j, m in enumerate(month_names):
            val = monthly[(monthly["location"] == loc)
                          & (monthly["month"] == m)]["temperature"]
            grid_vals[i, j] = val.iloc[0] if len(val) else np.nan

    fig, ax = plt.subplots(figsize=(9.0, 2.6))
    im = ax.imshow(grid_vals, aspect="auto", cmap="inferno",
                   vmin=20, vmax=95)
    ax.set_xticks(np.arange(len(month_names)))
    ax.set_xticklabels(month_names)
    ax.set_yticks(np.arange(len(loc_order)))
    ax.set_yticklabels(loc_order)
    ax.set_xlabel("month")
    for sp in ("top", "right", "bottom", "left"):
        ax.spines[sp].set_visible(False)
    ax.tick_params(axis="both", length=0)

    cbar = fig.colorbar(im, ax=ax, fraction=0.04, pad=0.02)
    cbar.set_label("temperature (°F)", fontsize=10)
    cbar.ax.tick_params(labelsize=9)

    fig.tight_layout()
    save(fig, "aesthetic_mapping", "temp_normals_heatmap")


if __name__ == "__main__":
    render()
