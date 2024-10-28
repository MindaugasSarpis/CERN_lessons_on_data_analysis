import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd
import numpy as np

# Sample data
df = pd.DataFrame({
    'Category': ['A', 'B', 'C', 'D'],
    'Values': [450, 250, 100, 200]
})

# Initialize the Dash app
app = dash.Dash(__name__)

# Layout of the dashboard
app.layout = html.Div(style={'backgroundColor': '#2c2c2c', 'padding': '20px', 'fontFamily': 'Arial, sans-serif'}, children=[
    html.H1('Super Cool Dashboard', style={'textAlign': 'center', 'color': '#00e6e6'}),
    
    html.Div(style={'display': 'flex', 'justifyContent': 'space-around'}, children=[
        # Pie chart
        html.Div(style={'width': '45%'}, children=[
            html.H3('Pie Chart', style={'textAlign': 'center', 'color': '#00e6e6'}),
            dcc.Graph(
                id='pie-chart',
                figure={
                    'data': [
                        go.Pie(
                            labels=df['Category'],
                            values=df['Values'],
                            hole=.3,
                            marker=dict(colors=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728'])
                        )
                    ],
                    'layout': go.Layout(
                        title='Distribution of Categories',
                        titlefont=dict(color='#00e6e6'),
                        paper_bgcolor='#2c2c2c',
                        plot_bgcolor='#2c2c2c',
                        font=dict(color='#00e6e6'),
                        showlegend=True,
                        legend=dict(font=dict(color='#00e6e6'))
                    )
                }
            )
        ]),
        
        # Line graph
        html.Div(style={'width': '45%'}, children=[
            html.H3('Line Graph', style={'textAlign': 'center', 'color': '#00e6e6'}),
            dcc.Graph(id='live-update-graph'),
            dcc.Interval(
                id='interval-component',
                interval=1*1000,  # in milliseconds
                n_intervals=0
            )
        ])
    ]),
    
    # List
    html.Div(style={'marginTop': '20px'}, children=[
        html.H3('Items List', style={'textAlign': 'center', 'color': '#00e6e6'}),
        html.Ul(style={'listStyleType': 'none', 'padding': '0', 'textAlign': 'center'}, children=[
            html.Li('Item 1', style={'padding': '10px', 'backgroundColor': '#1f77b4', 'margin': '5px', 'color': '#ffffff'}),
            html.Li('Item 1', style={'padding': '10px', 'backgroundColor': '#1f77b4', 'margin': '5px', 'color': '#ffffff'}),
            html.Li('Item 1', style={'padding': '10px', 'backgroundColor': '#1f77b4', 'margin': '5px', 'color': '#ffffff'}),
            html.Li('Item 1', style={'padding': '10px', 'backgroundColor': '#1f77b4', 'margin': '5px', 'color': '#ffffff'}),
            html.Li('Item 3', style={'padding': '10px', 'backgroundColor': '#2ca02c', 'margin': '5px', 'color': '#ffffff'}),
            html.Li('Item 2', style={'padding': '10px', 'backgroundColor': '#ff7f0e', 'margin': '5px', 'color': '#ffffff'}),
            html.Li('Item 2', style={'padding': '10px', 'backgroundColor': '#ff7f0e', 'margin': '5px', 'color': '#ffffff'}),
            html.Li('Item 2', style={'padding': '10px', 'backgroundColor': '#ff7f0e', 'margin': '5px', 'color': '#ffffff'}),
            html.Li('Item 2', style={'padding': '10px', 'backgroundColor': '#ff7f0e', 'margin': '5px', 'color': '#ffffff'}),
            html.Li('Item 2', style={'padding': '10px', 'backgroundColor': '#ff7f0e', 'margin': '5px', 'color': '#ffffff'}),
            html.Li('Item 2', style={'padding': '10px', 'backgroundColor': '#ff7f0e', 'margin': '5px', 'color': '#ffffff'}),
            html.Li('Item 4', style={'padding': '10px', 'backgroundColor': '#d62728', 'margin': '5px', 'color': '#ffffff'})
        ])
    ])
])

@app.callback(Output('live-update-graph', 'figure'),
              Input('interval-component', 'n_intervals'))
def update_graph_live(n):
    line_data = pd.DataFrame({
        'Time': pd.date_range(start='1/1/2020', periods=n+10),
        'Value': np.random.randint(1, 20, size=n+10)
    })
    
    fig = go.Figure(
        data=[
            go.Scatter(
                x=line_data['Time'],
                y=line_data['Value'],
                mode='lines+markers',
                line=dict(shape='spline', smoothing=1.3, color='#00e6e6'),
                marker=dict(color='#ff7f0e')
            )
        ],
        layout=go.Layout(
            title='Time Series Data',
            titlefont=dict(color='#00e6e6'),
            xaxis=dict(title='Time', titlefont=dict(color='#00e6e6'), tickfont=dict(color='#00e6e6')),
            yaxis=dict(title='Value', titlefont=dict(color='#00e6e6'), tickfont=dict(color='#00e6e6')),
            paper_bgcolor='#2c2c2c',
            plot_bgcolor='#2c2c2c',
            font=dict(color='#00e6e6')
        )
    )

    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
