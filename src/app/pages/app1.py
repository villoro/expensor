"""
    Dash app
"""

import pandas as pd
import plotly.graph_objs as go
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from app.layout import PLOT_CONFIG

import constants as c
from dash_app import DFG, APP, CATEGORIES


def get_options(iterable):
    """
        Populates a dash dropdawn from an iterable
    """
    return [{"label": x, "value": x} for x in iterable]


sidebar = [
    html.Div(dcc.Link('Go to App 1', href='/app1')),
    html.Div(dcc.Link('Go to App 2', href='/app2')),
    dcc.Dropdown(id='category', options=get_options(CATEGORIES), multi=True),
]

content = [
    dcc.Graph(id="plot1", config=PLOT_CONFIG,
              figure={"data": [go.Bar(x=DFG[c.cols.DATE], y=DFG[c.cols.AMOUNT])]}),
]


@APP.callback(Output('plot1', 'figure'), [Input("df", "children")])
def update_plot(df_input):

    df = DFG if df_input is None else pd.read_json(df_input)
    
    return {"data": [go.Bar(x=df[c.cols.DATE], y=df[c.cols.AMOUNT])]}
