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
MODE_WITH_CSV = {"CSV only"}
MODE_WITH_MODEL = {"Gaussian (μ, σ)", "Bimodal (2 Gaussians)"}
BIMODAL_MODE = "Bimodal (2 Gaussians)"
CSV_ANIMATION_DURATION_S = 10.0
ANIMATION_STATE = {"csv_signature": None}

# Colors
COLOR_CSV = "#2E86AB"  # Blue
COLOR_MODEL = "#A23B72"  # Purple


def _get_animation_state():
    doc = pn.state.curdoc
    if doc is None:
        return ANIMATION_STATE
    state = getattr(doc, "_grades_chart_animation_state", None)
    if state is None:
        state = {"csv_signature": None}
        setattr(doc, "_grades_chart_animation_state", state)
    return state




mode = pn.widgets.RadioButtonGroup(
    name="Mode",
    options=[
        "CSV only",
        "Gaussian (μ, σ)",
        "Bimodal (2 Gaussians)",
    ],
    value="CSV only",
)
csv_path = pn.widgets.TextInput(
    name="CSV path", placeholder="2025_grades_q2.csv (column: Įvertinimas/10.00)"
)
show_model_overlay = pn.widgets.Checkbox(
    name="Show Gaussian overlay", value=False
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

fit_button = pn.widgets.Button(
    name="Fit Gaussian to CSV", button_type="primary", width=200
)


def fit_gaussian_to_csv(event):
    """Fit Gaussian parameters to CSV data and update sliders."""
    try:
        series, _ = read_scores(csv_path.value)
        if series is None or series.empty:
            return

        # Calculate mean and std from the actual data points
        mean_val = float(series.mean())
        std_val = float(series.std())

        # Update the sliders
        mu.value = round(mean_val, 1)
        sigma.value = round(max(0.1, std_val), 1)  # Ensure sigma >= 0.1
        n_synth.value = len(series)

        # Enable overlay to show the fit
        show_model_overlay.value = True
    except Exception:
        pass


fit_button.on_click(fit_gaussian_to_csv)


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
        col_normalized = col.strip().casefold()
        if col_normalized in SCORE_COLUMNS:
            return col
        # Check if any score column name appears in this column
        for score_name in SCORE_COLUMNS:
            if score_name in col_normalized:
                return col
    return None


def read_scores(path_str):
    if not path_str:
        return None, "⚠️ Provide a CSV path"
    path = Path(path_str)
    if not path.exists():
        return None, f"⚠️ CSV '{path_str}' not found"

    try:
        df = pd.read_csv(path)
    except Exception as e:
        return None, f"⚠️ Failed to read CSV: {e}"

    column = pick_grade_column(df.columns)
    if not column:
        return None, f"⚠️ No grade column found (looking for: {', '.join(sorted(list(SCORE_COLUMNS)[:3]))}...)"

    series = pd.to_numeric(df[column], errors="coerce").dropna()
    series = series[(series >= 0) & (series <= 10)]
    if series.empty:
        return None, "⚠️ No valid grades in [0, 10] range"
    return series, ""


def load_csv_counts(csv_path_value):
    series, note = read_scores(csv_path_value)
    if series is None:
        return None, note, False, None
    return counts_in_fixed_bins(series), "", True, series.to_numpy()


def make_bar_trace(counts, name, offset, color):
    return go.Bar(
        x=CENTERS,
        y=counts,
        name=name,
        offsetgroup=offset,
        width=0.45,
        marker_color=color,
        marker_line_width=0,
    )


def format_stats(counts, title, color):
    if counts is None:
        return f"<div style='padding: 12px; border-left: 4px solid {color}; background: #f8f9fa;'><strong>{title}</strong>: no data</div>"
    total = float(np.sum(counts))
    if total <= 0:
        return f"<div style='padding: 12px; border-left: 4px solid {color}; background: #f8f9fa;'><strong>{title}</strong>: n=0 | mean=—</div>"
    mean = np.average(CENTERS, weights=counts)
    return f"<div style='padding: 12px; border-left: 4px solid {color}; background: #f8f9fa;'><strong style='font-size: 1.1em;'>{title}</strong><br>n = {total:.0f} students | mean = <strong>{mean:.2f}</strong></div>"


def build_figure(csv_counts_value, model_counts_value, ymax_value, animate_csv=False):
    fig = go.Figure()
    if csv_counts_value is not None:
        csv_display_counts = (
            np.zeros_like(csv_counts_value) if animate_csv else csv_counts_value
        )
        fig.add_trace(
            make_bar_trace(csv_display_counts, "CSV / Example", "csv", COLOR_CSV)
        )
    if model_counts_value is not None:
        # Show as line if overlaying with CSV, otherwise as bars
        if csv_counts_value is not None:
            fig.add_trace(
                go.Scatter(
                    x=CENTERS,
                    y=model_counts_value,
                    name="Model (Gaussian fit)",
                    mode="lines",
                    line=dict(color=COLOR_MODEL, width=4),
                    hovertemplate="Grade: %{x}<br>Students: %{y:.1f}<extra></extra>",
                )
            )
        else:
            fig.add_trace(
                make_bar_trace(model_counts_value, "Model", "model", COLOR_MODEL)
            )

    fig.update_layout(
        template="plotly_white",
        barmode="group",
        xaxis=dict(
            title=dict(text="Grade", font=dict(size=20, color="#333")),
            range=[0.5, 10.5],
            tickmode="array",
            tickvals=np.arange(1, 11, 1),
            tickfont=dict(size=20, color="#000", family="Arial, sans-serif"),
            ticktext=[f"<b>{i}</b>" for i in range(1, 11)],
        ),
        yaxis=dict(
            title=dict(text="Number of Students", font=dict(size=20, color="#333")),
            range=[0, int(ymax_value)],
            tickfont=dict(size=18),
        ),
        bargap=0.15,
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="left",
            x=0,
            font=dict(size=14),
        ),
        font=dict(family="system-ui, -apple-system, sans-serif", size=14, color="#333"),
        plot_bgcolor="white",
        paper_bgcolor="white",
        margin=dict(l=60, r=40, t=60, b=60),
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


@pn.depends(mode, csv_path, show_model_overlay, n_synth, mu, sigma, mu1, sigma1, mu2, sigma2, w1, ymax)
def view(
    mode_value,
    csv_path_value,
    show_overlay,
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
            csv_path_value
        )

    # Calculate model counts for model modes OR CSV mode with overlay enabled
    model_counts_value = None
    if mode_value in MODE_WITH_MODEL:
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
    elif mode_value in MODE_WITH_CSV and show_overlay:
        # Show Gaussian overlay in CSV mode
        model_counts_value = gaussian_bin_counts(mu_value, sigma_value, n_students)

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
        pn.pane.HTML(format_stats(csv_counts_value, "CSV / Example", COLOR_CSV)),
        pn.pane.HTML(format_stats(model_counts_value, "Model", COLOR_MODEL)),
        sizing_mode="stretch_width",
    )

    plot = pn.pane.Plotly(
        fig,
        config={"displaylogo": False, "responsive": True},
        sizing_mode="stretch_width",
        styles={"aspect-ratio": "16 / 9", "min-height": "320px"},
    )

    if should_animate_csv:
        animate_csv_bins(plot, csv_counts_value, csv_points)

    note_pane = (
        pn.pane.HTML(
            f"<div style='padding: 12px; background: #fff3cd; border-left: 4px solid #ffc107; margin-top: 10px; border-radius: 4px;'>{csv_note}</div>"
        )
        if csv_note
        else pn.Spacer(height=0)
    )

    return pn.Column(plot, stats_row, note_pane, sizing_mode="stretch_width")


@pn.depends(mode, show_model_overlay)
def sidebar_content(mode_value, show_overlay):
    """Generate sidebar content based on selected mode."""
    items = [
        pn.pane.Markdown(
            "## Grade Distribution",
            styles={
                "font-size": "1.4em",
                "font-weight": "600",
                "margin-bottom": "20px",
                "color": "#2c3e50",
            },
        ),
        mode,
        pn.Spacer(height=15),
    ]

    # CSV section - show if mode uses CSV
    if mode_value in MODE_WITH_CSV:
        items.extend([
            pn.pane.Markdown("### CSV Data", styles={"color": COLOR_CSV, "font-weight": "600"}),
            csv_path,
            pn.Spacer(height=10),
            show_model_overlay,
            pn.Spacer(height=10),
            fit_button,
            pn.pane.Markdown(
                "_Calculates μ and σ from CSV data_",
                styles={"font-size": "0.85em", "color": "#666", "margin-top": "4px"},
            ),
            pn.Spacer(height=15),
        ])

        # Show Gaussian parameters if overlay is enabled
        if show_overlay:
            items.extend([
                pn.pane.Markdown("### Gaussian Overlay", styles={"color": COLOR_MODEL, "font-weight": "600"}),
                n_synth,
                mu,
                sigma,
                pn.Spacer(height=15),
            ])

    # Model parameters - show if mode uses model
    if mode_value in MODE_WITH_MODEL:
        items.extend([
            pn.pane.Markdown("### Model Parameters", styles={"color": COLOR_MODEL, "font-weight": "600"}),
            n_synth,
            pn.Spacer(height=10),
        ])

        # Gaussian parameters
        if mode_value == "Gaussian (μ, σ)":
            items.extend([
                pn.pane.Markdown("**Gaussian Distribution**"),
                mu,
                sigma,
                pn.Spacer(height=10),
            ])

        # Bimodal parameters
        if mode_value == BIMODAL_MODE:
            items.extend([
                pn.pane.Markdown("**Bimodal Distribution**"),
                mu1,
                sigma1,
                mu2,
                sigma2,
                w1,
                pn.Spacer(height=10),
            ])

    # Display options
    items.extend([
        pn.Spacer(height=5),
        pn.pane.Markdown("### Display Options", styles={"font-weight": "600"}),
        ymax,
        pn.pane.Markdown(
            "_Override Y-axis max (0 = auto)_",
            styles={"font-size": "0.85em", "color": "#666", "margin-top": "4px"},
        ),
    ])

    return pn.Column(*items)

template = pn.template.FastListTemplate(
    title="Grade Analysis Dashboard",
    sidebar=[sidebar_content],
    main=[view],
    sidebar_width=320,
    main_max_width="100%",
    header_background="#2c3e50",
)
template.servable()
