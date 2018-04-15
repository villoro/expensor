"""
    Dash app
"""

import dash_core_components as dcc
from dash.dependencies import Input, Output

import utilities as u
import constants as c
from app import layout
from dash_app import DFG, CATEGORIES, APP
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

SIDEBAR = layout.create_sidebar(CATEGORIES)


@APP.callback(Output("plot_ts_grad_i", "figure"), [Input("category", "value")])
def update_ts_grad_i(categories):
    """
        Updates the timeserie gradient plot

        Args:
            categories: categories to use
    """

    df = u.dfs.filter_data(DFG, categories)

    return plots.ts_gradient(df, c.names.INCOMES)


@APP.callback(Output("plot_ts_grad_e", "figure"), [Input("category", "value")])
def update_ts_grad_e(categories):
    """
        Updates the timeserie gradient plot

        Args:
            categories: categories to use
    """

    df = u.dfs.filter_data(DFG, categories)

    return plots.ts_gradient(df, c.names.EXPENSES)