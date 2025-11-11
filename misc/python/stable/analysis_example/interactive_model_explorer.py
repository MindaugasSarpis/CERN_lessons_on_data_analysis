#!/usr/bin/env python3
import numpy as np
import plotly.graph_objects as go
from dash import Dash, dcc, html, Input, Output

# Model functions
def gaussian(x, amp, mean, sigma):
    if sigma == 0:
        return np.zeros_like(x)
    return amp * np.exp(-0.5 * ((x - mean) / sigma)**2)

def exponential(x, norm, scale):
    if scale == 0:
        return np.zeros_like(x)
    return norm * np.exp(-x / scale)

# Setup
x = np.linspace(0, 10, 500)

# Initialize the Dash app
app = Dash(__name__)

# Define the layout
app.layout = html.Div([
    html.Div([
        dcc.Graph(id='model-plot', style={'width': '70%', 'display': 'inline-block'}),

        html.Div([
            html.Label('Amplitude', style={'marginTop': '20px'}),
            dcc.Slider(
                id='amplitude-slider',
                min=0, max=200, step=1, value=100,
                marks={i: str(i) for i in range(0, 201, 50)},
                tooltip={"placement": "bottom", "always_visible": True},
                updatemode='drag'
            ),

            html.Label('Mean', style={'marginTop': '20px'}),
            dcc.Slider(
                id='mean-slider',
                min=0, max=8, step=0.1, value=5.0,
                marks={i: str(i) for i in range(0, 9)},
                tooltip={"placement": "bottom", "always_visible": True},
                updatemode='drag'
            ),

            html.Label('Width (σ)', style={'marginTop': '20px'}),
            dcc.Slider(
                id='sigma-slider',
                min=0, max=2.5, step=0.1, value=1.0,
                marks={float(i): f'{i:.1f}' for i in [0, 0.5, 1.0, 1.5, 2.0, 2.5]},
                tooltip={"placement": "bottom", "always_visible": True},
                updatemode='drag'
            ),

            html.Label('Exp Norm', style={'marginTop': '20px'}),
            dcc.Slider(
                id='exp-norm-slider',
                min=0, max=150, step=1, value=50,
                marks={i: str(i) for i in range(0, 151, 50)},
                tooltip={"placement": "bottom", "always_visible": True},
                updatemode='drag'
            ),

            html.Label('Exp Scale', style={'marginTop': '20px'}),
            dcc.Slider(
                id='exp-scale-slider',
                min=0, max=5.0, step=0.1, value=2.0,
                marks={float(i): f'{i:.1f}' for i in [0, 1.0, 2.0, 3.0, 4.0, 5.0]},
                tooltip={"placement": "bottom", "always_visible": True},
                updatemode='drag'
            ),
        ], style={'width': '25%', 'display': 'inline-block', 'verticalAlign': 'top', 'padding': '20px'})
    ])
])

# Define the callback to update the plot
@app.callback(
    Output('model-plot', 'figure'),
    [Input('amplitude-slider', 'value'),
     Input('mean-slider', 'value'),
     Input('sigma-slider', 'value'),
     Input('exp-norm-slider', 'value'),
     Input('exp-scale-slider', 'value')]
)
def update_plot(amp, mean, sigma, exp_norm, exp_scale):
    # Calculate curves
    gauss = gaussian(x, amp, mean, sigma)
    exp = exponential(x, exp_norm, exp_scale)
    total = gauss + exp

    # Create figure
    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=x, y=total,
        name='Total',
        line=dict(color='red', width=3)
    ))

    fig.add_trace(go.Scatter(
        x=x, y=gauss,
        name='Gaussian',
        line=dict(color='green', dash='dash')
    ))

    fig.add_trace(go.Scatter(
        x=x, y=exp,
        name='Exponential',
        line=dict(color='purple', dash='dash')
    ))

    fig.update_layout(
        height=600,
        xaxis_title="x",
        yaxis_title="Counts",
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        margin=dict(t=50, r=50, l=50, b=50)
    )

    return fig

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
