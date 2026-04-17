"""Bachelor's degree trends with *free* y-axes per panel — bad practice.

Nine most-popular degree areas as small multiples. Each panel uses its
own y range, making it look like every area is equally popular. Wilke
marks this version as bad (fig 21.3).
"""

from __future__ import annotations

import matplotlib.pyplot as plt

from cwilke import data as D
from cwilke.theme import PRIMARY_BLUE, apply_base, hgrid, save, stamp_bad


def render() -> None:
    apply_base()
    df = D.ba_degrees()
    order = (df.groupby("field")["perc"].mean()
             .sort_values(ascending=False).index.tolist())

    fig, axes = plt.subplots(3, 3, figsize=(10.0, 7.5))

    for ax, field in zip(axes.ravel(), order):
        sub = df[df["field"] == field].sort_values("year")
        ax.plot(sub["year"], sub["perc"] * 100,
                color=PRIMARY_BLUE, linewidth=1.7)
        # Tight local y-range — this is the "bad" design choice
        lo, hi = sub["perc"].min() * 100, sub["perc"].max() * 100
        pad = (hi - lo) * 0.12 + 0.1
        ax.set_ylim(lo - pad, hi + pad)
        wrapped = field if len(field) < 30 else field.replace(", ", ",\n")
        ax.set_title(wrapped, fontsize=10, color="#455a64")
        ax.set_xticks([1970, 1990, 2010])
        hgrid(ax)

    fig.supylabel("proportion of degrees (%)", fontsize=11)
    stamp_bad(fig)
    fig.tight_layout()
    save(fig, "multi_panel", "ba_degrees_variable_y")


if __name__ == "__main__":
    render()
