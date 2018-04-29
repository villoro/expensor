"""
    Dash app
"""

import dash_core_components as dcc
from dash.dependencies import Input, Output

import utilities as u
import constants as c
from app import ui_utils as uiu
from plots import plots_violins as plots


LINK = c.dash.LINK_VIOLINS


def get_content(app, df_trans_input):
    """
        Creates the page

        Args:
            app:            dash app
            df_trans_input: dataframe with transactions

        Returns:
            dict with content:
                body:       body of the page
    """

    content = [
        dcc.Graph(
            id="plot_violin_year", config=uiu.PLOT_CONFIG,
            figure=plots.violin_plot(df_trans_input, c.cols.YEAR)
        ),
        dcc.Graph(
            id="plot_violin_month", config=uiu.PLOT_CONFIG,
            figure=plots.violin_plot(df_trans_input, c.cols.MONTH)
        )
    ]


    @app.callback(Output("plot_violin_year", "figure"),
                  [Input("global_df_trans", "children"), Input("category", "value")])
    #pylint: disable=unused-variable
    def update_violin_y(df_trans, categories):
        """
            Updates the violin year plot

            Args:
                df_trans:   transactions dataframe
                categories: categories to use
        """

        df = u.uos.b64_to_df(df_trans)
        df = u.dfs.filter_data(df, categories)

        return plots.violin_plot(df, c.cols.YEAR)


    @app.callback(Output("plot_violin_month", "figure"),
                  [Input("global_df_trans", "children"), Input("category", "value")])
    #pylint: disable=unused-variable
    def update_violin_m(df_trans, categories):
        """
            Updates the violin year plot

            Args:
                df_trans:   transactions dataframe
                categories: categories to use
        """

        df = u.uos.b64_to_df(df_trans)
        df = u.dfs.filter_data(df, categories)

        return plots.violin_plot(df, c.cols.MONTH)

    return {c.dash.KEY_BODY: content}
