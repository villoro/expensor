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

def get_content(app, dfg, categories):
    content = uiu.create_body([
        dcc.Graph(
            id="plot_comp_i", config=uiu.PLOT_CONFIG,
            figure=plots.ts_gradient(dfg, c.names.INCOMES)
        ),
        dcc.Graph(
            id="plot_comp_e", config=uiu.PLOT_CONFIG,
            figure=plots.ts_gradient(dfg, c.names.EXPENSES)
        ),
    ])

    sidebar = uiu.create_sidebar(categories)


    @app.callback(Output("plot_comp_i", "figure"), [Input("category", "value")])
    def update_ts_grad_i(categories):
        """
            Updates the timeserie gradient plot

            Args:
                categories: categories to use
        """

        df = u.dfs.filter_data(dfg, categories)

        return plots.ts_gradient(df, c.names.INCOMES)


    @app.callback(Output("plot_comp_e", "figure"), [Input("category", "value")])
    def update_ts_grad_e(categories):
        """
            Updates the timeserie gradient plot

            Args:
                categories: categories to use
        """

        df = u.dfs.filter_data(dfg, categories)

        return plots.ts_gradient(df, c.names.EXPENSES)

    return content, sidebar
