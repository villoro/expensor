"""
    Dash app
"""

import pandas as pd
import dash_core_components as dcc
from dash.dependencies import Input, Output
from app.layout import PLOT_CONFIG

from dash_app import DFG, APP
from plots import plots


CONTENT = [
    dcc.Graph(
        id="plot1", config=PLOT_CONFIG,
        figure=plots.plot_timeserie(DFG)
    ),
]


@APP.callback(Output("plot1", "figure"),
              [Input("df", "children"), Input("timewindow", "value")])
def update_timeserie_plot(df_input, timewindow):
    """
        Updates the timeserie plot

        Args:
        df_input:	dataframe to use
            timewindow:	timewindow to use for grouping
    """

    df = DFG if df_input is None else pd.read_json(df_input)

    return plots.plot_timeserie(df, timewindow)
