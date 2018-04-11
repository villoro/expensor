"""
    Dash app
"""

import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from app.layout import PLOT_CONFIG


content = [
    dcc.Graph(
        id="plot2", config=PLOT_CONFIG,
        figure={
            "data": [
                go.Bar(y=list("5945626454198514515616548486548654158463"))
            ]
        }
    ),
    dcc.Graph(
        id="plot3", config=PLOT_CONFIG,
        figure={
            "data": [
                go.Bar(y=list("515432514514513445631618597158719746387647845364356"))
            ]
        }
    ),
]
