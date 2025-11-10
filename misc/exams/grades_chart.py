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
SCORE_COLUMNS = {
    name.casefold()
    for name in (
        "grade",
        "grades",
        "score",
        "scores",
        "mark",
        "marks",
        "įvertinimas",
        "ivertinimas",
    )
}
FALLBACK_GAUSSIAN = (7.0, 1.5)
MODE_WITH_CSV = {"CSV only", "CSV + Model overlay"}
MODE_WITH_MODEL = {"Gaussian (μ, σ)", "Bimodal (2 Gaussians)", "CSV + Model overlay"}
BIMODAL_MODE = "Bimodal (2 Gaussians)"
CSV_ANIMATION_DURATION_S = 10.0
ANIMATION_STATE = {"csv_signature": None}


def _get_animation_state():
    doc = pn.state.curdoc
    if doc is None:
        return ANIMATION_STATE
    state = getattr(doc, "_grades_chart_animation_state", None)
    if state is None:
        state = {"csv_signature": None}
        setattr(doc, "_grades_chart_animation_state", state)
    return state


def fallback_note(message: str) -> str:
    return f"⚠️ {message}. Showing Gaussian fallback."


mode = pn.widgets.RadioButtonGroup(
    name="Mode",
    options=[
        "CSV only",
        "Gaussian (μ, σ)",
        "Bimodal (2 Gaussians)",
        "CSV + Model overlay",
    ],
    value="CSV only",
)
csv_path = pn.widgets.TextInput(
    name="CSV path", placeholder="2025_grades_q1.csv (column: Įvertinimas/10.00)"
)
n_synth = pn.widgets.IntSlider(
    name="Number of students (model)", start=0, end=100, value=30
)

mu = pn.widgets.FloatSlider(name="μ (mean)", start=0.0, end=10.0, step=0.1, value=7.0)
sigma = pn.widgets.FloatSlider(name="σ (std)", start=0.1, end=3.0, step=0.1, value=1.5)

mu1 = pn.widgets.FloatSlider(name="μ₁", start=0.0, end=10.0, step=0.1, value=6.5)
sigma1 = pn.widgets.FloatSlider(name="σ₁", start=0.1, end=3.0, step=0.1, value=1.0)
mu2 = pn.widgets.FloatSlider(name="μ₂", start=0.0, end=10.0, step=0.1, value=8.5)
sigma2 = pn.widgets.FloatSlider(name="σ₂", start=0.1, end=3.0, step=0.1, value=1.0)
w1 = pn.widgets.FloatSlider(
    name="w₁ (weight of first Gaussian)", start=0.0, end=1.0, step=0.01, value=0.5
)

ymax = pn.widgets.IntSlider(
    name="Y-axis max (override)", start=0, end=100, step=1, value=0
)


def gaussian_bin_counts(mu_value, sigma_value, n_students):
    if n_students <= 0 or sigma_value <= 0:
        return np.zeros_like(CENTERS)
    inv_sigma = 1.0 / (sigma_value * sqrt(2.0))

    def cdf(x):
        return 0.5 * (1 + erf((x - mu_value) * inv_sigma))

    probs = np.array([cdf(b) - cdf(a) for a, b in zip(EDGES[:-1], EDGES[1:])])
    norm = max(cdf(10.0) - cdf(0.0), np.finfo(float).eps)
    return probs / norm * n_students


def bimodal_bin_counts(
    mu1_value, sigma1_value, mu2_value, sigma2_value, w1_value, n_students
):
    weight = float(np.clip(w1_value, 0.0, 1.0))
    first = gaussian_bin_counts(mu1_value, sigma1_value, n_students * weight)
    second = gaussian_bin_counts(mu2_value, sigma2_value, n_students * (1 - weight))
    return first + second


def model_counts(
    mode_value,
    n_students,
    mu_value,
    sigma_value,
    mu1_value,
    sigma1_value,
    mu2_value,
    sigma2_value,
    w1_value,
):
    if mode_value not in MODE_WITH_MODEL:
        return None
    if mode_value == BIMODAL_MODE:
        return bimodal_bin_counts(
            mu1_value, sigma1_value, mu2_value, sigma2_value, w1_value, n_students
        )
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
        return gaussian_fallback_counts(fallback_students), note, False, None
    return counts_in_fixed_bins(series), "", True, series.to_numpy()


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


def build_figure(csv_counts_value, model_counts_value, ymax_value, animate_csv=False):
    fig = go.Figure()
    if csv_counts_value is not None:
        csv_display_counts = (
            np.zeros_like(csv_counts_value) if animate_csv else csv_counts_value
        )
        fig.add_trace(make_bar_trace(csv_display_counts, "CSV / Example", "csv"))
    if model_counts_value is not None:
        fig.add_trace(make_bar_trace(model_counts_value, "Model", "model"))

    fig.update_layout(
        template="plotly_white",
        barmode="group",
        xaxis_title="Grade",
        yaxis_title="Students",
        xaxis=dict(
            range=[-0.25, 10.25], tickmode="array", tickvals=np.arange(0, 10.5, 0.5)
        ),
        yaxis=dict(range=[0, int(ymax_value)]),
        bargap=0.1,
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="left", x=0),
    )
    return fig


def animate_csv_bins(
    plot_pane, target_counts, data_points, duration_s=CSV_ANIMATION_DURATION_S
):
    """
    Animate CSV bins by revealing one data point at a time within the given duration.
    """
    if pn.state.curdoc is None:
        return

    counts = np.array(target_counts, dtype=float)
    if counts.size == 0:
        return

    values = np.array(data_points if data_points is not None else [])
    if values.size == 0:
        return

    figure = plot_pane.object
    if not figure.data:
        return

    csv_trace = None
    for trace in figure.data:
        if getattr(trace, "name", "") == "CSV / Example":
            csv_trace = trace
            break
    if csv_trace is None:
        csv_trace = figure.data[0]

    previous_callback = getattr(plot_pane, "_csv_animation_callback", None)
    if previous_callback is not None:
        previous_callback.stop()

    current_counts = np.zeros_like(counts, dtype=float)
    csv_trace.y = current_counts
    plot_pane.param.trigger("object")

    bin_indices = np.searchsorted(EDGES, values, side="right") - 1
    bin_indices = np.clip(bin_indices, 0, counts.size - 1)
    total_points = bin_indices.size
    period_ms = max(int(duration_s * 1000 / max(total_points, 1)), 10)
    state = {"index": 0}
    callback_holder = {"cb": None}

    def advance():
        idx = state["index"]
        if idx >= total_points:
            csv_trace.y = counts
            plot_pane.param.trigger("object")
            if callback_holder["cb"] is not None:
                callback_holder["cb"].stop()
            return

        bin_idx = bin_indices[idx]
        current_counts[bin_idx] += 1
        state["index"] += 1
        csv_trace.y = current_counts.copy()
        plot_pane.param.trigger("object")

    callback_holder["cb"] = pn.state.add_periodic_callback(advance, period=period_ms)
    plot_pane._csv_animation_callback = callback_holder["cb"]
    advance()


@pn.depends(mode, csv_path, n_synth, mu, sigma, mu1, sigma1, mu2, sigma2, w1, ymax)
def view(
    mode_value,
    csv_path_value,
    n_students,
    mu_value,
    sigma_value,
    mu1_value,
    sigma1_value,
    mu2_value,
    sigma2_value,
    w1_value,
    ymax_value,
):
    csv_counts_value, csv_note, csv_has_real_data, csv_points = (None, "", False, None)
    if mode_value in MODE_WITH_CSV:
        csv_counts_value, csv_note, csv_has_real_data, csv_points = load_csv_counts(
            csv_path_value, n_students
        )

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

    animation_state = _get_animation_state()
    should_animate_csv = False
    if csv_has_real_data and csv_counts_value is not None:
        counts_tuple = tuple(np.asarray(csv_counts_value, dtype=float))
        csv_signature = (csv_path_value or "", counts_tuple)
        should_animate_csv = csv_signature != animation_state.get("csv_signature")
        animation_state["csv_signature"] = csv_signature
    else:
        animation_state["csv_signature"] = None

    csv_max = (
        float(np.max(csv_counts_value))
        if csv_counts_value is not None and np.size(csv_counts_value) > 0
        else 0.0
    )
    model_max = (
        float(np.max(model_counts_value))
        if model_counts_value is not None and np.size(model_counts_value) > 0
        else 0.0
    )
    auto_ymax = max(5, int(np.ceil(max(csv_max, model_max) + 1)))
    final_ymax = ymax_value if ymax_value > 0 else auto_ymax

    fig = build_figure(
        csv_counts_value, model_counts_value, final_ymax, animate_csv=should_animate_csv
    )
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

    if should_animate_csv:
        animate_csv_bins(plot, csv_counts_value, csv_points)

    note_pane = pn.pane.HTML(csv_note) if csv_note else pn.Spacer(height=0)

    return pn.Column(plot, stats_row, note_pane, sizing_mode="stretch_width")


sidebar = [
    pn.pane.Markdown(
        "### Controls",
        styles={
            "border-bottom": "1px solid #e0e0e0",
            "padding-bottom": "6px",
            "margin-bottom": "12px",
        },
    ),
    mode,
    pn.layout.Divider(),
    pn.pane.Markdown("### CSV"),
    csv_path,
    pn.layout.Divider(),
    pn.pane.Markdown("### Model (students & shape)"),
    n_synth,
    ymax,
    pn.pane.Markdown(
        "_Set >0 to override auto scale (max bin + 1)._",
        styles={"font-size": "0.85em", "color": "#555"},
    ),
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
