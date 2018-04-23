"""
    Dash app
"""

import dash_core_components as dcc
from dash.dependencies import Input, Output

import utilities as u
import constants as c
from app import ui_utils as uiu
from dash_app import DFG, CATEGORIES, APP
from plots import plots_violins as plots


CONTENT = uiu.create_body([
    dcc.Graph(
        id="plot_violin_year", config=uiu.PLOT_CONFIG,
        figure=plots.violin_plot(DFG, c.cols.YEAR)
    ),
    dcc.Graph(
        id="plot_violin_month", config=uiu.PLOT_CONFIG,
        figure=plots.violin_plot(DFG, c.cols.MONTH)
    )
])

SIDEBAR = uiu.create_sidebar(
    CATEGORIES,
)

@APP.callback(Output("plot_violin_year", "figure"),
              [Input("category", "value")])
def update_violin_y(categories):
    """
        Updates the violin year plot

        Args:
            categories: categories to use
    """

    df = u.dfs.filter_data(DFG, categories)

    return plots.violin_plot(df, c.cols.YEAR)


@APP.callback(Output("plot_violin_month", "figure"),
              [Input("category", "value")])
def update_violin_m(categories):
    """
        Updates the violin year plot

        Args:
            categories: categories to use
    """

    df = u.dfs.filter_data(DFG, categories)

    return plots.violin_plot(df, c.cols.MONTH)
