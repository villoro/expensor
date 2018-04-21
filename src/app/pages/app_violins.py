"""
    Dash app
"""

import dash_core_components as dcc
from dash.dependencies import Input, Output

import utilities as u
import constants as c
from app import layout
from dash_app import DFG, CATEGORIES, APP
from plots import plots_violins as plots


CONTENT = [
    layout.get_body_elem(
        dcc.Graph(
            id="violin_year", config=layout.PLOT_CONFIG,
            figure=plots.violin_plot(DFG, c.cols.YEAR)
        )
    ),
    layout.get_body_elem(
        dcc.Graph(
            id="violin_month", config=layout.PLOT_CONFIG,
            figure=plots.violin_plot(DFG, c.cols.MONTH)
        )
    ),
]

SIDEBAR = layout.create_sidebar(
    CATEGORIES,
)

@APP.callback(Output("violin_year", "figure"),
              [Input("category", "value")])
def update_violin_y(categories):
    """
        Updates the violin year plot

        Args:
            categories: categories to use
    """

    df = u.dfs.filter_data(DFG, categories)

    return plots.violin_plot(df, c.cols.YEAR)


@APP.callback(Output("violin_month", "figure"),
              [Input("category", "value")])
def update_violin_m(categories):
    """
        Updates the violin year plot

        Args:
            categories: categories to use
    """

    df = u.dfs.filter_data(DFG, categories)

    return plots.violin_plot(df, c.cols.MONTH)
