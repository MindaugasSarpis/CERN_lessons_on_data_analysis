"""Bachelor's degree trends with a *shared* y axis across panels (Wilke fig 21.4).

Same data as the bad variant, but every panel uses the same 0–24% y
range, revealing that the degree areas differ substantially in size.
"""

from __future__ import annotations

import matplotlib.pyplot as plt

from cwilke import data as D
from cwilke.theme import PRIMARY_BLUE, apply_base, hgrid, save


def render() -> None:
    apply_base()
    df = D.ba_degrees()
    order = (df.groupby("field")["perc"].mean()
             .sort_values(ascending=False).index.tolist())

    fig, axes = plt.subplots(3, 3, figsize=(10.0, 7.5),
                             sharey=True)

    for ax, field in zip(axes.ravel(), order):
        sub = df[df["field"] == field].sort_values("year")
        ax.plot(sub["year"], sub["perc"] * 100,
                color=PRIMARY_BLUE, linewidth=1.7)
        ax.set_ylim(0, 24)
        wrapped = field if len(field) < 30 else field.replace(", ", ",\n")
        ax.set_title(wrapped, fontsize=10, color="#455a64")
        ax.set_xticks([1970, 1990, 2010])
        hgrid(ax)

    fig.supylabel("proportion of degrees (%)", fontsize=11)
    fig.tight_layout()
    save(fig, "multi_panel", "ba_degrees_fixed_y")


if __name__ == "__main__":
    render()
