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
        dcc.Graph(id="plot_violin_year", config=uiu.PLOT_CONFIG),
        dcc.Graph(id="plot_violin_month", config=uiu.PLOT_CONFIG),
        uiu.get_dummy_div("violin_aux")
    ]

    sidebar = [("Categories", dcc.Dropdown(id="drop_violin_categ", multi=True))]


    @app.callback(Output("drop_violin_categ", "options"),
                  [Input("global_categories", "children"),
                   Input("violin_aux", "children")])
    #pylint: disable=unused-variable
    def update_categories(categories, aux):
        """
            Updates categories dropdown with the actual categories
        """

        return uiu.get_options(categories)


    @app.callback(Output("plot_violin_year", "figure"),
                  [Input("global_df_trans", "children"),
                   Input("drop_violin_categ", "value"),
                   Input("violin_aux", "children")])
    #pylint: disable=unused-variable
    def update_violin_y(df_trans, categories, aux):
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
                  [Input("global_df_trans", "children"),
                   Input("drop_violin_categ", "value"),
                   Input("violin_aux", "children")])
    #pylint: disable=unused-variable
    def update_violin_m(df_trans, categories, aux):
        """
            Updates the violin year plot

            Args:
                df_trans:   transactions dataframe
                categories: categories to use
        """

        df = u.uos.b64_to_df(df_trans)
        df = u.dfs.filter_data(df, categories)

        return plots.violin_plot(df, c.cols.MONTH)

    return {c.dash.KEY_BODY: content, c.dash.KEY_SIDEBAR: sidebar}
