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
        dcc.Graph(id="plot_liquid_year", config=uiu.PLOT_CONFIG),
    ]

    @app.callback(Output("plot_liquid_year", "figure"),
                  [Input("global_df_liquid", "children"),
                   Input("global_df_liquid_list", "children"),
                   Input("liquid_aux", "children")])
    #pylint: disable=unused-variable,unused-argument
    def update_liquid(df_liq_in, df_liq_list_in, aux):
        """
            Updates the incomes heatmap

            Args:
                df_liq_in:          dataframe with liquid info
                df_liq_list_in:     dataframe with types of liquids
        """

        return plots.liquid_plot(
            df_liq_in=u.uos.b64_to_df(df_liq_in),
            df_list=u.uos.b64_to_df(df_liq_list_in)
        )

    return {c.dash.DUMMY_DIV: "liquid_aux", c.dash.KEY_BODY: content}
