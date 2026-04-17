"""Life expectancy (Americas, 2007) rendered as BARS — Wilke fig 6.7.

This version is sorted correctly, but bars are a bad choice here: the values
(60–81 y) never come close to zero, so every bar is very long and of similar
length. The eye is drawn to the middle of the bars, not the ends, and the
real differences between countries are lost.
"""

from __future__ import annotations

import matplotlib.pyplot as plt

from cwilke import data as D
from cwilke.theme import PRIMARY_BLUE, apply_base, save, stamp_bad, vgrid


def render() -> None:
    apply_base()

    df = (
        D.gapminder()
        .query("year == 2007 and continent == 'Americas'")
        .sort_values("lifeExp")
    )
    if len(df) < 8:
        # fallback if the inline gapminder has too few Americas countries
        import numpy as np
        import pandas as pd
        rng = np.random.default_rng(42)
        countries = [
            "Haiti", "Bolivia", "Guatemala", "Honduras", "Paraguay",
            "El Salvador", "Peru", "Dominican Republic", "Jamaica",
            "Trinidad and Tobago", "Ecuador", "Brazil", "Colombia", "Venezuela",
            "Nicaragua", "Argentina", "Mexico", "Panama", "Uruguay",
            "Chile", "Cuba", "Costa Rica", "United States", "Puerto Rico",
            "Canada",
        ]
        values = [60.9, 65.6, 70.3, 70.2, 71.8, 71.9, 71.4, 72.9, 72.6,
                  69.8, 75.0, 72.4, 72.9, 73.7, 72.4, 75.3, 76.2, 75.5,
                  76.4, 78.6, 78.3, 78.8, 78.2, 78.7, 80.7]
        df = pd.DataFrame({"country": countries, "lifeExp": values})
        df = df.sort_values("lifeExp")

    fig, ax = plt.subplots(figsize=(6.4, 6.2))
    ax.barh(df["country"], df["lifeExp"],
            color=PRIMARY_BLUE, alpha=0.9, height=0.68,
            edgecolor="#2c3e50", linewidth=0.4)
    ax.set_xlabel("life expectancy (years)")
    ax.set_xlim(0, 85)
    ax.set_xticks([0, 20, 40, 60, 80])
    vgrid(ax)
    ax.tick_params(axis="y", length=0, labelsize=10)
    stamp_bad(fig)
    save(fig, "amounts", "lifeexp_bars_bad")


if __name__ == "__main__":
    render()
