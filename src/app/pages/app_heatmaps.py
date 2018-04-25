"""
    Dash app
"""

import dash_core_components as dcc
from dash.dependencies import Input, Output

import utilities as u
import constants as c
from app import ui_utils as uiu
from plots import plots_heatmaps as plots


LINK = c.dash.LINK_HEATMAPS


#pylint: disable=unused-argument
def get_content(app, dfg, categories):
    """
        Creates the page

        Args:
            app:        dash app
            dfg:        dataframe with all data
            categories: list of categories avaiables

        Returns:
            content:    body of the page
            sidebar:    content of the sidebar
    """

    content = [
        [
            uiu.get_one_column(
                dcc.Graph(
                    id="plot_heat_i", config=uiu.PLOT_CONFIG,
                    figure=plots.get_heatmap(dfg, c.names.INCOMES)
                ), n_rows=6),
            uiu.get_one_column(
                dcc.Graph(
                    id="plot_heat_e", config=uiu.PLOT_CONFIG,
                    figure=plots.get_heatmap(dfg, c.names.EXPENSES)
                ), n_rows=6
            )
        ],
        dcc.Graph(
            id="plot_heat_distribution", config=uiu.PLOT_CONFIG,
            figure=plots.dist_plot(dfg)
        )
    ]

    @app.callback(Output("plot_heat_i", "figure"),
                  [Input("category", "value")])
    #pylint: disable=unused-variable
    def update_heatmap_i(categories):
        """
            Updates the incomes heatmap

            Args:
                categories: categories to use
        """

        df = u.dfs.filter_data(dfg, categories)

        return plots.get_heatmap(df, c.names.INCOMES)


    @app.callback(Output("plot_heat_e", "figure"),
                  [Input("category", "value")])
    #pylint: disable=unused-variable
    def update_heatmap_e(categories):
        """
            Updates the expenses heatmap

            Args:
                categories: categories to use
        """

        df = u.dfs.filter_data(dfg, categories)

        return plots.get_heatmap(df, c.names.EXPENSES)


    @app.callback(Output("plot_heat_distribution", "figure"),
                  [Input("category", "value")])
    #pylint: disable=unused-variable
    def update_distplot(categories):
        """
            Updates the distribution plot

            Args:
                categories: categories to use
        """

        return plots.dist_plot(u.dfs.filter_data(dfg, categories))

    return content, None
