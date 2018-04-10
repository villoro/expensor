"""
    Dash app
"""

import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from app.layout import PLOT_CONFIG


sidebar = [
    html.Div(dcc.Link('Go to App 1', href='/app1')),
    html.Div(dcc.Link('Go to App 2', href='/app2'))
]

content = [
    dcc.Graph(
        id="plot2", config=PLOT_CONFIG,
        figure={
            "data": [
                go.Bar(y=list("5423545632"))
            ]
        }
    ),
    dcc.Graph(
        id="plot3", config=PLOT_CONFIG,
        figure={
            "data": [
                go.Bar(y=list("515432514514513445631646387647845364356"))
            ]
        }
    ),
    dcc.Graph(
        id="plot4", config=PLOT_CONFIG,
        figure={
            "data": [
                go.Bar(y=list("12"))
            ]
        }
    )
]
