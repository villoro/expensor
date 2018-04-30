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


def get_content(app):
    """
        Creates the page

        Args:
            app:            dash app

        Returns:
            dict with content:
                body:       body of the page
    """

    content = [
        [
            uiu.get_one_column(
                dcc.Graph(id="plot_heat_i", config=uiu.PLOT_CONFIG), n_rows=6
            ),
            uiu.get_one_column(
                dcc.Graph(id="plot_heat_e", config=uiu.PLOT_CONFIG), n_rows=6
            )
        ],
        dcc.Graph(id="plot_heat_distribution", config=uiu.PLOT_CONFIG)
    ]

    @app.callback(Output("plot_heat_i", "figure"),
                  [Input("global_df_trans", "children"), Input("category", "value")])
    #pylint: disable=unused-variable
    def update_heatmap_i(df_trans, categories):
        """
            Updates the incomes heatmap

            Args:
                df_trans:   transactions dataframe
                categories: categories to use
        """

        df = u.uos.b64_to_df(df_trans)
        df = u.dfs.filter_data(df, categories)

        return plots.get_heatmap(df, c.names.INCOMES)


    @app.callback(Output("plot_heat_e", "figure"),
                  [Input("global_df_trans", "children"), Input("category", "value")])
    #pylint: disable=unused-variable
    def update_heatmap_e(df_trans, categories):
        """
            Updates the expenses heatmap

            Args:
                df_trans:   transactions dataframe
                categories: categories to use
        """

        df = u.uos.b64_to_df(df_trans)
        df = u.dfs.filter_data(df, categories)

        return plots.get_heatmap(df, c.names.EXPENSES)


    @app.callback(Output("plot_heat_distribution", "figure"),
                  [Input("global_df_trans", "children"), Input("category", "value")])
    #pylint: disable=unused-variable
    def update_distplot(df_trans, categories):
        """
            Updates the distribution plot

            Args:
                df_trans:   transactions dataframe
                categories: categories to use
        """

        df = u.uos.b64_to_df(df_trans)
        df = u.dfs.filter_data(df, categories)

        return plots.dist_plot(df)

    return {c.dash.KEY_BODY: content}
