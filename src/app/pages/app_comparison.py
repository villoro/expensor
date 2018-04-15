"""
    Dash app
"""

import dash_core_components as dcc
from dash.dependencies import Input, Output

import utilities as u
import constants as c
from app import layout
from dash_app import DFG, APP
from plots import plots


CONTENT = [
    layout.get_body_elem(
        dcc.Graph(
            id="plot_ts_grad_i", config=layout.PLOT_CONFIG,
            figure=plots.ts_gradient(DFG, c.names.INCOMES)
        )
    ),
    layout.get_body_elem(
        dcc.Graph(
            id="plot_ts_grad_e", config=layout.PLOT_CONFIG,
            figure=plots.ts_gradient(DFG, c.names.EXPENSES)
        )
    ),
]


@APP.callback(Output("plot_ts_grad_i", "figure"),
              [Input("category", "value"), Input("timewindow", "value")])
def update_ts_grad_i(categories, timewindow):
    """
        Updates the timeserie gradient plot

        Args:
            categories: categories to use
            timewindow: timewindow to use for grouping
    """

    if timewindow == "Y":
        return None

    df = u.dfs.filter_data(DFG, categories)

    return plots.ts_gradient(df, c.names.INCOMES, timewindow=timewindow)


@APP.callback(Output("plot_ts_grad_e", "figure"),
              [Input("category", "value"), Input("timewindow", "value")])
def update_ts_grad_e(categories, timewindow):
    """
        Updates the timeserie gradient plot

        Args:
            categories: categories to use
            timewindow: timewindow to use for grouping
    """

    if timewindow == "Y":
        return None

    df = u.dfs.filter_data(DFG, categories)

    return plots.ts_gradient(df, c.names.EXPENSES, timewindow=timewindow)