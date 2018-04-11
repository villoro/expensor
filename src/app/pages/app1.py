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
from dash_app import DFG, APP
from plots import plots
from app import layout


content = [
    dcc.Graph(id="plot1", config=PLOT_CONFIG,
    		  figure=plots.plot_timeserie(DFG)),
]


@APP.callback(Output("plot1", "figure"),
              [Input("df", "children"), Input("timewindow", "value")])
def update_plot(df_input, timewindow):

    df = DFG if df_input is None else pd.read_json(df_input)
    
    return plots.plot_timeserie(df, timewindow)
