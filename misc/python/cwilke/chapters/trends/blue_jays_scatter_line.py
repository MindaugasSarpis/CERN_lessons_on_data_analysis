"""Blue jays — head length vs body mass with per-sex linear fits
(Wilke fig 14.7)."""

from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np

from cwilke import data as D
from cwilke.theme import apply_base, grid, save


def render() -> None:
    apply_base()
    df = D.blue_jays()
    colors = {"F": "#D55E00", "M": "#0072B2"}
    labels = {"F": "female birds", "M": "male birds"}

    fig, ax = plt.subplots(figsize=(6.0, 4.4))
    for s in ("F", "M"):
        sub = df[df["sex"] == s]
        ax.scatter(sub["body_mass_g"], sub["head_length_mm"],
                   s=34, facecolors=colors[s], edgecolors="white",
                   linewidths=0.6, label=labels[s])
        # least-squares line
        x = sub["body_mass_g"].values
        y = sub["head_length_mm"].values
        m, b = np.polyfit(x, y, 1)
        xs = np.linspace(df["body_mass_g"].min(), df["body_mass_g"].max(), 40)
        ax.plot(xs, m * xs + b, color=colors[s], linewidth=1.6)
    ax.set_xlabel("body mass (g)")
    ax.set_ylabel("head length (mm)")
    ax.legend(loc="lower right", frameon=False)
    grid(ax)
    save(fig, "trends", "blue_jays_scatter_line")


if __name__ == "__main__":
    render()
