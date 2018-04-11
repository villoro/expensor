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
from plots import plots
from app import layout


def get_options(iterable):
    """
        Populates a dash dropdawn from an iterable
    """
    return [{"label": x, "value": x} for x in iterable]


sidebar = [
    layout.get_sidebar_elem(
        "Sections",
        [
            html.Div(dcc.Link("App 1", href="/app1")),
            html.Div(dcc.Link("App 2", href="/app2"))
        ]
    ),
    layout.get_sidebar_elem(
        "Categories",
        dcc.Dropdown(id="category", options=get_options(CATEGORIES), multi=True)
    ),
    layout.get_sidebar_elem(
        "Group by",
        dcc.RadioItems(id="timewindow", value="M",
                       options=[{"label": "Day", "value": "D"},
                                {"label": "Month", "value": "M"},
                                {"label": "Year", "value": "Y"}])
    ),
]

content = [
    dcc.Graph(id="plot1", config=PLOT_CONFIG),
]


@APP.callback(Output("plot1", "figure"),
              [Input("df", "children"), Input("timewindow", "value")])
def update_plot(df_input, timewindow):

    df = DFG if df_input is None else pd.read_json(df_input)
    
    return plots.plot_timeserie(df, timewindow)
