"""
    Dash app
"""

import dash_core_components as dcc
from dash.dependencies import Input, Output

import utilities as u
import constants as c
from app import ui_utils as uiu
from plots import plots_liquid as plots


LINK = c.dash.LINK_LIQUID


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
        dcc.Graph(id="plot_liquid_evo", config=uiu.PLOT_CONFIG),
        dcc.Graph(id="plot_liquid_vs_expenses", config=uiu.PLOT_CONFIG),
    ]

    @app.callback(Output("plot_liquid_evo", "figure"),
                  [Input("global_df_liquid", "children"),
                   Input("global_df_liquid_list", "children"),
                   Input("liquid_aux", "children")])
    #pylint: disable=unused-variable,unused-argument
    def update_liquid(df_liq, df_liq_list, aux):
        """
            Updates the incomes heatmap

            Args:
                df_liq:         dataframe with liquid info
                df_liq_list:    dataframe with types of liquids
        """

        return plots.liquid_plot(
            df_liq_in=u.uos.b64_to_df(df_liq),
            df_list=u.uos.b64_to_df(df_liq_list)
        )

    @app.callback(Output("plot_liquid_vs_expenses", "figure"),
                  [Input("global_df_liquid", "children"),
                   Input("global_df_trans", "children"),
                   Input("liquid_aux", "children")])
    #pylint: disable=unused-variable,unused-argument
    def update_liquid(df_liq, df_trans, aux):
        """
            Updates the incomes heatmap

            Args:
                df_liq:     dataframe with liquid info
                df_trans:   dataframe with transactions
        """

        return plots.plot_expenses_vs_liquid(
            df_liquid_in=u.uos.b64_to_df(df_liq),
            df_trans_in=u.uos.b64_to_df(df_trans)
        )

    return {c.dash.DUMMY_DIV: "liquid_aux", c.dash.KEY_BODY: content}
