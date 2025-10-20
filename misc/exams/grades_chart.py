# misc/exams/grades_chart.py
import numpy as np
import pandas as pd
import panel as pn
import plotly.graph_objects as go
from pathlib import Path
from math import erf, sqrt

pn.extension("plotly")

EDGES = np.arange(0.0, 10.0 + 0.5, 0.5)
CENTERS = (EDGES[:-1] + EDGES[1:]) / 2.0
SCORE_COLUMNS = {name.casefold() for name in (
    "grade", "grades", "score", "scores", "mark", "marks",
    "įvertinimas", "ivertinimas",
)}
FALLBACK_GAUSSIAN = (7.0, 1.5)
MODE_WITH_CSV = {"CSV only", "CSV + Model overlay"}
MODE_WITH_MODEL = {"Gaussian (μ, σ)", "Bimodal (2 Gaussians)", "CSV + Model overlay"}
BIMODAL_MODE = "Bimodal (2 Gaussians)"


def fallback_note(message: str) -> str:
    return f"⚠️ {message}. Showing Gaussian fallback."

mode = pn.widgets.RadioButtonGroup(
    name="Mode",
    options=["CSV only", "Gaussian (μ, σ)", "Bimodal (2 Gaussians)", "CSV + Model overlay"],
    value="CSV only",
)
csv_path = pn.widgets.TextInput(name="CSV path", placeholder="2025_grades_q1.csv (column: Įvertinimas/10.00)")
n_synth = pn.widgets.IntSlider(name="Number of students (model)", start=0, end=50, value=30)

mu = pn.widgets.FloatSlider(name="μ (mean)", start=0.0, end=10.0, step=0.1, value=7.0)
sigma = pn.widgets.FloatSlider(name="σ (std)", start=0.1, end=3.0, step=0.1, value=1.5)

mu1 = pn.widgets.FloatSlider(name="μ₁", start=0.0, end=10.0, step=0.1, value=6.5)
sigma1 = pn.widgets.FloatSlider(name="σ₁", start=0.1, end=3.0, step=0.1, value=1.0)
mu2 = pn.widgets.FloatSlider(name="μ₂", start=0.0, end=10.0, step=0.1, value=8.5)
sigma2 = pn.widgets.FloatSlider(name="σ₂", start=0.1, end=3.0, step=0.1, value=1.0)
w1 = pn.widgets.FloatSlider(name="w₁ (weight of first Gaussian)", start=0.0, end=1.0, step=0.01, value=0.5)

ymax = pn.widgets.IntSlider(name="Y-axis max (scale)", start=5, end=200, step=5, value=50)


def gaussian_bin_counts(mu_value, sigma_value, n_students):
    if n_students <= 0 or sigma_value <= 0:
        return np.zeros_like(CENTERS)
    inv_sigma = 1.0 / (sigma_value * sqrt(2.0))

    def cdf(x):
        return 0.5 * (1 + erf((x - mu_value) * inv_sigma))

    probs = np.array([cdf(b) - cdf(a) for a, b in zip(EDGES[:-1], EDGES[1:])])
    norm = max(cdf(10.0) - cdf(0.0), np.finfo(float).eps)
    return probs / norm * n_students


def bimodal_bin_counts(mu1_value, sigma1_value, mu2_value, sigma2_value, w1_value, n_students):
    weight = float(np.clip(w1_value, 0.0, 1.0))
    first = gaussian_bin_counts(mu1_value, sigma1_value, n_students * weight)
    second = gaussian_bin_counts(mu2_value, sigma2_value, n_students * (1 - weight))
    return first + second


def model_counts(mode_value, n_students, mu_value, sigma_value, mu1_value, sigma1_value, mu2_value, sigma2_value, w1_value):
    if mode_value not in MODE_WITH_MODEL:
        return None
    if mode_value == BIMODAL_MODE:
        return bimodal_bin_counts(mu1_value, sigma1_value, mu2_value, sigma2_value, w1_value, n_students)
    return gaussian_bin_counts(mu_value, sigma_value, n_students)


def counts_in_fixed_bins(values):
    return np.histogram(values, bins=EDGES)[0]


def pick_grade_column(columns):
    for col in columns:
        if col.strip().casefold() in SCORE_COLUMNS:
            return col
    return None


def read_scores(path_str):
    if not path_str:
        return None, fallback_note("Provide a CSV path")
    path = Path(path_str)
    if not path.exists():
        return None, fallback_note(f"CSV '{path_str}' not found")

    try:
        df = pd.read_csv(path)
    except Exception:
        return None, fallback_note(f"Failed to read '{path_str}'")

    column = pick_grade_column(df.columns)
    if not column:
        return None, fallback_note(f"Could not find a grade column in '{path_str}'")

    series = pd.to_numeric(df[column], errors="coerce").dropna()
    series = series[(series >= 0) & (series <= 10)]
    if series.empty:
        return None, fallback_note("Grade column contained no values in [0, 10]")
    return series, ""


def gaussian_fallback_counts(fallback_students):
    mu, sigma = FALLBACK_GAUSSIAN
    return gaussian_bin_counts(mu, sigma, max(1, fallback_students))


def load_csv_counts(csv_path_value, fallback_students):
    series, note = read_scores(csv_path_value)
    if series is None:
        return gaussian_fallback_counts(fallback_students), note
    return counts_in_fixed_bins(series), ""


def make_bar_trace(counts, name, offset):
    return go.Bar(x=CENTERS, y=counts, name=name, offsetgroup=offset, width=0.45)


def format_stats(counts, title):
    if counts is None:
        return f"**{title}**: no data"
    total = float(np.sum(counts))
    if total <= 0:
        return f"**{title}** n=0 | mean≈—"
    mean = np.average(CENTERS, weights=counts)
    return f"**{title}** n={total:.0f} | mean≈{mean:.2f}"


def build_figure(csv_counts_value, model_counts_value, ymax_value):
    fig = go.Figure()
    if csv_counts_value is not None:
        fig.add_trace(make_bar_trace(csv_counts_value, "CSV / Example", "csv"))
    if model_counts_value is not None:
        fig.add_trace(make_bar_trace(model_counts_value, "Model", "model"))

    fig.update_layout(
        template="plotly_white",
        barmode="group",
        xaxis_title="Grade",
        yaxis_title="Students",
        xaxis=dict(range=[-0.25, 10.25], tickmode="array", tickvals=np.arange(0, 10.5, 0.5)),
        yaxis=dict(range=[0, int(ymax_value)]),
        bargap=0.1,
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="left", x=0),
    )
    return fig


@pn.depends(mode, csv_path, n_synth, mu, sigma, mu1, sigma1, mu2, sigma2, w1, ymax)
def view(mode_value, csv_path_value, n_students, mu_value, sigma_value, mu1_value, sigma1_value, mu2_value, sigma2_value, w1_value, ymax_value):
    csv_counts_value, csv_note = (None, "")
    if mode_value in MODE_WITH_CSV:
        csv_counts_value, csv_note = load_csv_counts(csv_path_value, n_students)

    model_counts_value = model_counts(
        mode_value,
        n_students,
        mu_value,
        sigma_value,
        mu1_value,
        sigma1_value,
        mu2_value,
        sigma2_value,
        w1_value,
    )

    fig = build_figure(csv_counts_value, model_counts_value, ymax_value)
    stats_row = pn.Row(
        pn.pane.Markdown(format_stats(csv_counts_value, "CSV / Example")),
        pn.pane.Markdown(format_stats(model_counts_value, "Model")),
    )

    plot = pn.pane.Plotly(
        fig,
        config={"displaylogo": False, "responsive": True},
        sizing_mode="stretch_width",
        styles={"aspect-ratio": "16 / 9", "min-height": "320px"},
    )

    note_pane = pn.pane.HTML(csv_note) if csv_note else pn.Spacer(height=0)

    return pn.Column(plot, stats_row, note_pane, sizing_mode="stretch_width")


sidebar = [
    pn.pane.Markdown("### Controls"),
    mode,
    pn.layout.Divider(),
    pn.pane.Markdown("### CSV"),
    csv_path,
    pn.layout.Divider(),
    pn.pane.Markdown("### Model (students & shape)"),
    n_synth,
    ymax,
    pn.pane.Markdown("**Gaussian**"),
    mu,
    sigma,
    pn.pane.Markdown("**Bimodal**"),
    mu1,
    sigma1,
    mu2,
    sigma2,
    w1,
]

template = pn.template.FastListTemplate(
    title="",
    sidebar=sidebar,
    main=[view],
    sidebar_width=300,
    main_max_width="100%",
)
template.servable()
