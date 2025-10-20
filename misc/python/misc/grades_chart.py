# grades_panel_simple.py — Deterministic Gaussian/Bimodal bar chart (Panel + Plotly)
import numpy as np
import pandas as pd
import panel as pn
import plotly.graph_objects as go
from pathlib import Path

pn.extension("plotly")

# ---- Fixed buckets: 0, 0.5, ..., 10 ----
EDGES = np.arange(0.0, 10.0 + 0.5, 0.5)
CENTERS = (EDGES[:-1] + EDGES[1:]) / 2.0

# ---- Widgets ----
mode = pn.widgets.RadioButtonGroup(
    name="Mode",
    options=["CSV only", "Gaussian (μ, σ)", "Bimodal (2 Gaussians)", "CSV + Model overlay"],
    value="CSV only",
)

csv_path = pn.widgets.TextInput(name="CSV path", placeholder="grades.csv (column: grade)")
n_synth = pn.widgets.IntSlider(name="Number of students (model)", start=0, end=50, value=30)

# Gaussian sliders
mu    = pn.widgets.FloatSlider(name="μ (mean)", start=0.0, end=10.0, step=0.1, value=7.0)
sigma = pn.widgets.FloatSlider(name="σ (std)",  start=0.1, end=3.0,  step=0.1, value=1.5)

# Bimodal sliders
mu1    = pn.widgets.FloatSlider(name="μ₁", start=0.0, end=10.0, step=0.1, value=6.5)
sigma1 = pn.widgets.FloatSlider(name="σ₁", start=0.1, end=3.0,  step=0.1, value=1.0)
mu2    = pn.widgets.FloatSlider(name="μ₂", start=0.0, end=10.0, step=0.1, value=8.5)
sigma2 = pn.widgets.FloatSlider(name="σ₂", start=0.1, end=3.0,  step=0.1, value=1.0)
w1     = pn.widgets.FloatSlider(name="w₁ (weight of first Gaussian)", start=0.0, end=1.0, step=0.01, value=0.5)

# Plot scale (Y axis max)
ymax = pn.widgets.IntSlider(name="Y-axis max (scale)", start=5, end=200, step=5, value=50)

# ---- Helpers ----
def read_csv_series(path: str):
    if not path:
        return None
    p = Path(path)
    if not p.exists():
        return None
    try:
        df = pd.read_csv(p)
        for c in df.columns:
            if c.strip().lower() in {"grade", "grades", "score", "scores", "mark", "marks"}:
                s = pd.to_numeric(df[c], errors="coerce").dropna()
                return s[(s >= 0) & (s <= 10)]
        return None
    except Exception:
        return None

# deterministic Gaussian counts (no randomness)
def gaussian_bin_counts(mu, sigma, n_students):
    """Expected number of students in each 0.5-wide bin, truncated to [0,10]."""
    if n_students <= 0:
        return np.zeros_like(CENTERS)
    from math import erf, sqrt
    def cdf(x):
        return 0.5 * (1 + erf((x - mu) / (sigma * np.sqrt(2))))
    probs = np.array([cdf(b) - cdf(a) for a, b in zip(EDGES[:-1], EDGES[1:])])
    # truncate normalization for [0,10]
    norm = cdf(10) - cdf(0)
    probs = probs / norm
    return probs * n_students

def bimodal_bin_counts(mu1, s1, mu2, s2, w1, n_students):
    if n_students <= 0:
        return np.zeros_like(CENTERS)
    g1 = gaussian_bin_counts(mu1, s1, n_students * w1)
    g2 = gaussian_bin_counts(mu2, s2, n_students * (1 - w1))
    return g1 + g2

def counts_in_fixed_bins(values):
    counts, _ = np.histogram(values, bins=EDGES)
    return counts

def make_bar_trace(counts, name, offsetgroup):
    return go.Bar(x=CENTERS, y=counts, name=name, offsetgroup=offsetgroup, width=0.45)

# ---- Reactive view ----
@pn.depends(mode, csv_path, n_synth, mu, sigma, mu1, sigma1, mu2, sigma2, w1, ymax)
def view(mode, csv_path, n_synth, mu, sigma, mu1, sigma1, mu2, sigma2, w1, ymax):
    csv_series = read_csv_series(csv_path)
    fallback_msg = ""
    csv_counts = None
    if mode in ["CSV only", "CSV + Model overlay"]:
        if csv_series is None or csv_series.empty:
            fallback_msg = "⚠️ CSV not found — showing example Gaussian fallback."
            csv_counts = gaussian_bin_counts(7.0, 1.5, max(1, n_synth))
        else:
            csv_counts = counts_in_fixed_bins(csv_series)

    # Model data
    model_counts = None
    if mode in ["Gaussian (μ, σ)", "CSV + Model overlay"]:
        model_counts = gaussian_bin_counts(mu, sigma, n_synth)
    elif mode == "Bimodal (2 Gaussians)":
        model_counts = bimodal_bin_counts(mu1, sigma1, mu2, sigma2, w1, n_synth)

    # Figure
    fig = go.Figure()
    if csv_counts is not None:
        fig.add_trace(make_bar_trace(csv_counts, "CSV / Example", "csv"))
    if model_counts is not None:
        fig.add_trace(make_bar_trace(model_counts, "Model", "model"))

    fig.update_layout(
        template="plotly_white",
        barmode="group",
        xaxis_title="Grade (0.5 steps)",
        yaxis_title="Students",
        xaxis=dict(range=[-0.25, 10.25], tickmode="array", tickvals=np.arange(0, 10.5, 0.5)),
        yaxis=dict(range=[0, int(ymax)]),
        bargap=0.1,
        title="Grades — Bar Chart (Analytical Gaussian)",
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="left", x=0),
    )

    def stats(arr, title):
        arr = np.asarray(arr)
        if arr.size == 0:
            return f"**{title}**: no data"
        total = arr.sum()
        mean = np.average(CENTERS, weights=arr) if total > 0 else float("nan")
        return f"**{title}** n={total:.0f} | mean≈{mean:.2f}"

    left = stats(csv_counts if csv_counts is not None else np.array([]), "CSV / Example")
    right = stats(model_counts if model_counts is not None else np.array([]), "Model")

    return pn.Column(
        pn.pane.Plotly(fig, config={"displaylogo": False, "responsive": True}),
        pn.Row(pn.pane.Markdown(left), pn.pane.Markdown(right)),
        pn.pane.HTML(f"<i>{fallback_msg}</i>") if fallback_msg else pn.Spacer(height=0),
        sizing_mode="stretch_width",
    )

# ---- Layout ----
template = pn.template.FastListTemplate(
    title="Grades — Analytical Gaussian Bar Chart (0..10, step 0.5)",
    sidebar=[
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
        mu, sigma,
        pn.pane.Markdown("**Bimodal**"),
        mu1, sigma1, mu2, sigma2, w1,
    ],
    main=[view],
    sidebar_width=300,
)
template.servable()
