"""
    Dash app
"""

import dash_core_components as dcc
from dash.dependencies import Input, Output

import utilities as u
import constants as c
from app import ui_utils as uiu
from plots import plots_comparison as plots


LINK = c.dash.LINK_COMPARISON


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
        dcc.Graph(id="plot_comp_i", config=uiu.PLOT_CONFIG),
        dcc.Graph(id="plot_comp_e", config=uiu.PLOT_CONFIG),
        uiu.get_dummy_div("comp_aux")
    ]

    sidebar = [("Categories", dcc.Dropdown(id="drop_comp_categ", multi=True))]


    @app.callback(Output("drop_comp_categ", "options"),
                  [Input("global_categories", "children"),
                   Input("comp_aux", "children")])
    #pylint: disable=unused-variable
    def update_categories(categories, aux):
        """
            Updates categories dropdown with the actual categories
        """

        return uiu.get_options(categories)


    @app.callback(Output("plot_comp_i", "figure"),
                  [Input("global_df_trans", "children"),
                   Input("drop_comp_categ", "value"),
                   Input("comp_aux", "children")])
    #pylint: disable=unused-variable
    def update_ts_grad_i(df_trans, categories, aux):
        """
            Updates the timeserie gradient plot

            Args:
                df_trans:   transactions dataframe
                categories: categories to use
        """

        df = u.uos.b64_to_df(df_trans)
        df = u.dfs.filter_data(df, categories)

        return plots.ts_gradient(df, c.names.INCOMES)


    @app.callback(Output("plot_comp_e", "figure"),
                  [Input("global_df_trans", "children"),
                   Input("drop_comp_categ", "value"),
                   Input("comp_aux", "children")])
    #pylint: disable=unused-variable
    def update_ts_grad_e(df_trans, categories, aux):
        """
            Updates the timeserie gradient plot

            Args:
                df_trans:   transactions dataframe
                categories: categories to use
        """

        df = u.uos.b64_to_df(df_trans)
        df = u.dfs.filter_data(df, categories)

        return plots.ts_gradient(df, c.names.EXPENSES)

    return {c.dash.KEY_BODY: content, c.dash.KEY_SIDEBAR: sidebar}
