"""8th Bundestag pie — a case where pies work (Wilke fig 10.1).

Three categories, one near-50/50 split, emphasises the coalition
majority. Stacked or side-by-side bars would obscure the fact that
SPD+FDP collectively exceed CDU/CSU.
"""

from __future__ import annotations

import matplotlib.pyplot as plt

from cwilke import data as D
from cwilke.theme import apply_base, save


def render() -> None:
    apply_base()
    df = D.bundestag_1976()

    fig, ax = plt.subplots(figsize=(5.6, 5.0))
    wedges, texts, autotexts = ax.pie(
        df["seats"], labels=df["party"],
        colors=df["color"].tolist(),
        autopct=lambda p: f"{int(round(p * sum(df['seats']) / 100))}",
        startangle=90, counterclock=False,
        wedgeprops=dict(edgecolor="white", linewidth=1.5),
        textprops=dict(fontsize=12),
    )
    for at, color in zip(autotexts, df["color"]):
        # White numbers on dark wedges, black on yellow.
        at.set_color("white" if color != "#F0E442" else "black")
        at.set_fontsize(12)
    ax.set_aspect("equal")
    fig.tight_layout()
    save(fig, "proportions", "bundestag_pie_good")


if __name__ == "__main__":
    render()
