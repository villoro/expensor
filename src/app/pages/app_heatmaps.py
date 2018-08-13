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


def get_content(app, dfg):
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
        dcc.Graph(id="plot_heat_distribution", config=uiu.PLOT_CONFIG),
    ]

    sidebar = [
        ("Categories", dcc.Dropdown(
            id="drop_heat_categ", multi=True,
            options=uiu.get_options(dfg[c.cols.CATEGORY].unique())
        ))
    ]


    @app.callback(Output("plot_heat_i", "figure"),
                  [Input("global_df", "children"),
                   Input("drop_heat_categ", "value"),
                   Input("heat_aux", "children")])
    #pylint: disable=unused-variable,unused-argument
    def update_heatmap_i(df_in, categories, aux):
        """
            Updates the incomes heatmap

            Args:
                df_in:      transactions dataframe
                categories: categories to use
        """
        df = u.dfs.filter_data(u.uos.b64_to_df(df_in), categories)
        return plots.get_heatmap(df, c.names.INCOMES)


    @app.callback(Output("plot_heat_e", "figure"),
                  [Input("global_df", "children"),
                   Input("drop_heat_categ", "value"),
                   Input("heat_aux", "children")])
    #pylint: disable=unused-variable,unused-argument
    def update_heatmap_e(df_in, categories, aux):
        """
            Updates the expenses heatmap

            Args:
                df_in:      transactions dataframe
                categories: categories to use
        """
        df = u.dfs.filter_data(u.uos.b64_to_df(df_in), categories)
        return plots.get_heatmap(df, c.names.EXPENSES)


    @app.callback(Output("plot_heat_distribution", "figure"),
                  [Input("global_df", "children"),
                   Input("drop_heat_categ", "value"),
                   Input("heat_aux", "children")])
    #pylint: disable=unused-variable,unused-argument
    def update_distplot(df_in, categories, aux):
        """
            Updates the distribution plot

            Args:
                df_in:      transactions dataframe
                categories: categories to use
        """
        df = u.dfs.filter_data(u.uos.b64_to_df(df_in), categories)
        return plots.dist_plot(df)

    return {
        c.dash.DUMMY_DIV: "heat_aux",
        c.dash.KEY_BODY: content,
        c.dash.KEY_SIDEBAR: sidebar
    }
