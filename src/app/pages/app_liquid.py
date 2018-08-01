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
        dcc.Graph(id="plot_liquid_months", config=uiu.PLOT_CONFIG),
    ]

    sidebar = [
        ("Rolling Average", dcc.Slider(
            id="slider_liq_rolling_avg",
            min=1, max=12, value=12,
            marks={i: str(i) if i > 1 else "None" for i in range(1, 13)},
        ))
    ]

    @app.callback(Output("plot_liquid_evo", "figure"),
                  [Input("global_df_liquid", "children"),
                   Input("global_df_liquid_list", "children"),
                   Input("liquid_aux", "children")])
    #pylint: disable=unused-variable,unused-argument
    def update_liquid(df_liq, df_liq_list, aux):
        """
            Updates the liquid distribution plot

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
                   Input("slider_liq_rolling_avg", "value"),
                   Input("liquid_aux", "children")])
    #pylint: disable=unused-variable,unused-argument
    def update_liquid_vs_expenses(df_liq, df_trans, avg_month, aux):
        """
            Updates the liquid vs expenses plot

            Args:
                df_liq:     dataframe with liquid info
                df_trans:   dataframe with transactions
                avg_month:  month to use in rolling average
        """

        return plots.plot_expenses_vs_liquid(
            df_liquid_in=u.uos.b64_to_df(df_liq),
            df_trans_in=u.uos.b64_to_df(df_trans),
            avg_month=avg_month
        )

    @app.callback(Output("plot_liquid_months", "figure"),
                  [Input("global_df_liquid", "children"),
                   Input("global_df_trans", "children"),
                   Input("slider_liq_rolling_avg", "value"),
                   Input("liquid_aux", "children")])
    #pylint: disable=unused-variable,unused-argument
    def update_liquid_months(df_liq, df_trans, avg_month, aux):
        """
            Updates the survival months plot

            Args:
                df_liq:     dataframe with liquid info
                df_trans:   dataframe with transactions
                avg_month:  month to use in rolling average
        """

        return plots.plot_months(
            df_liquid_in=u.uos.b64_to_df(df_liq),
            df_trans_in=u.uos.b64_to_df(df_trans),
            avg_month=avg_month
        )

    return {
        c.dash.DUMMY_DIV: "liquid_aux",
        c.dash.KEY_BODY: content,
        c.dash.KEY_SIDEBAR: sidebar
    }
