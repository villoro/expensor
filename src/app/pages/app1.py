"""
    Dash app
"""

import pandas as pd
import plotly.graph_objs as go
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from app.layout import PLOT_CONFIG

from dash_app import APP, CATEGORIES


def get_options(iterable):
    """
        Populates a dash dropdawn from an iterable
    """
    return [{"label": x, "value": x} for x in iterable]


sidebar = [
    #html.Div(dcc.Link('Go to App 1', href='/app1')),
    #html.Div(dcc.Link('Go to App 2', href='/app2')),
    dcc.Dropdown(id='category', options=get_options(CATEGORIES), multi=True),
    html.Div("text", id='aux2'),
]

content = [
    dcc.Graph(id="plot1", config=PLOT_CONFIG,
              figure={"data": [go.Bar(y=list("5945626454198514586548654158463"))]}),
]

@APP.callback(Output('aux2', 'children'), [Input("category", "value")])
def temp2(value):
    return value
