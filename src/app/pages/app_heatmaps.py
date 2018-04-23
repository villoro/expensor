"""
    Dash app
"""

import dash_core_components as dcc
from dash.dependencies import Input, Output

import utilities as u
import constants as c
from app import layout
from dash_app import DFG, CATEGORIES, APP
from plots import plots_heatmaps as plots


CONTENT = layout.create_body([
    [
        layout.get_one_column(
            dcc.Graph(
                id="plot_heat_i", config=layout.PLOT_CONFIG,
                figure=plots.get_heatmap(DFG, c.names.INCOMES)
            ), n_rows=6),
        layout.get_one_column(
            dcc.Graph(
                id="plot_heat_e", config=layout.PLOT_CONFIG,
                figure=plots.get_heatmap(DFG, c.names.EXPENSES)
            ), n_rows=6
        )
    ],
    dcc.Graph(
        id="plot_heat_distribution", config=layout.PLOT_CONFIG,
        figure=plots.dist_plot(DFG)
    )
])

SIDEBAR = layout.create_sidebar(
    CATEGORIES,
)

@APP.callback(Output("plot_heat_i", "figure"),
              [Input("category", "value")])
def update_heatmap_i(categories):
    """
        Updates the incomes heatmap

        Args:
            categories: categories to use
    """

    df = u.dfs.filter_data(DFG, categories)

    return plots.get_heatmap(df, c.names.INCOMES)


@APP.callback(Output("plot_heat_e", "figure"),
              [Input("category", "value")])
def update_heatmap_e(categories):
    """
        Updates the expenses heatmap

        Args:
            categories: categories to use
    """

    df = u.dfs.filter_data(DFG, categories)

    return plots.get_heatmap(df, c.names.EXPENSES)


@APP.callback(Output("plot_heat_distribution", "figure"),
              [Input("category", "value")])
def update_distplot(categories):
    """
        Updates the distribution plot

        Args:
            categories: categories to use
    """

    return plots.dist_plot(u.dfs.filter_data(DFG, categories))
