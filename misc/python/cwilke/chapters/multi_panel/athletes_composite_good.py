"""Athletes composite — consistent visual language (Wilke fig 21.8).

Female = orange, male = blue, throughout. Female always on the left of
every group. Single legend covers panels (b) and (c).
"""

from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np

from cwilke import data as D
from cwilke.theme import apply_base, hgrid, save


SEX_COLORS = {"f": "#D55E00", "m": "#0072B2"}


def _boxplot_by(ax, df, *, groupby, value, group_order, width=0.34):
    positions = np.arange(len(group_order))
    for i, sex in enumerate(("f", "m")):
        sub = df[df["sex"] == sex]
        data = [sub[sub[groupby] == g][value].dropna().values
                for g in group_order]
        bp = ax.boxplot(
            data,
            positions=positions + (i - 0.5) * (width + 0.04),
            widths=width,
            patch_artist=True,
            showfliers=False,
            medianprops={"color": "#2c3e50", "linewidth": 1.3},
        )
        color = SEX_COLORS[sex]
        for box in bp["boxes"]:
            box.set_facecolor(color)
            box.set_edgecolor(color)
            box.set_alpha(0.55)
        for w in bp["whiskers"] + bp["caps"]:
            w.set_color(color)
    ax.set_xticks(positions)
    ax.set_xticklabels(group_order)


def render() -> None:
    apply_base()
    df = D.aus_athletes()
    df = df[df["sport"].isin(["track (sprint)", "track (400m)",
                              "field", "swimming", "basketball",
                              "water polo"])].copy()
    df["sport"] = df["sport"].str.replace("track.*", "track", regex=True)

    fig = plt.figure(figsize=(10.0, 7.5))
    gs = fig.add_gridspec(2, 2, width_ratios=[0.9, 1.4],
                          height_ratios=[1, 1],
                          hspace=0.45, wspace=0.35)
    ax_a = fig.add_subplot(gs[0, 0])
    ax_b = fig.add_subplot(gs[0, 1])
    ax_c = fig.add_subplot(gs[1, :])

    counts = df["sex"].value_counts().reindex(["f", "m"])
    ax_a.bar(["female", "male"], counts.values,
             color=[SEX_COLORS["f"], SEX_COLORS["m"]],
             alpha=0.85, width=0.65)
    ax_a.set_ylabel("number")
    ax_a.set_ylim(0, 95)
    hgrid(ax_a)
    ax_a.set_title("a", loc="left", fontweight="bold", color="#455a64")

    for sex in ("f", "m"):
        sub = df[df["sex"] == sex]
        ax_b.scatter(sub["rcc"], sub["wcc"], s=36, color=SEX_COLORS[sex],
                     edgecolor="white", linewidth=0.6, alpha=0.85,
                     label="female" if sex == "f" else "male")
    ax_b.set_xlabel("RBC count")
    ax_b.set_ylabel("WBC count")
    ax_b.set_xlim(3.8, 6.4)
    ax_b.set_ylim(2.2, 11)
    hgrid(ax_b)
    ax_b.set_title("b", loc="left", fontweight="bold", color="#455a64")

    sports = sorted(df["sport"].unique())
    _boxplot_by(ax_c, df, groupby="sport", value="pcBfat",
                group_order=sports)
    ax_c.set_ylabel("% body fat")
    ax_c.set_xlabel("")
    hgrid(ax_c)
    ax_c.set_title("c", loc="left", fontweight="bold", color="#455a64")

    from matplotlib.patches import Patch
    legend_handles = [
        Patch(facecolor=SEX_COLORS["f"], label="female", alpha=0.7),
        Patch(facecolor=SEX_COLORS["m"], label="male", alpha=0.7),
    ]
    ax_c.legend(handles=legend_handles, loc="upper right", fontsize=9)

    fig.tight_layout()
    save(fig, "multi_panel", "athletes_composite_good")


if __name__ == "__main__":
    render()
