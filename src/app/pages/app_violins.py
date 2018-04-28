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


def get_content(app, mdata):
    """
        Creates the page

        Args:
            app:        dash app
            mdata:      data helper class, used for retriving dataframes

        Returns:
            dict with content:
                body:       body of the page
                sidebar:    content of the sidebar
    """

    # Retreive transactions dataframe from data helper
    dfg = mdata.df_trans

    content = [
        dcc.Graph(
            id="plot_violin_year", config=uiu.PLOT_CONFIG,
            figure=plots.violin_plot(dfg, c.cols.YEAR)
        ),
        dcc.Graph(
            id="plot_violin_month", config=uiu.PLOT_CONFIG,
            figure=plots.violin_plot(dfg, c.cols.MONTH)
        )
    ]

    @app.callback(Output("plot_violin_year", "figure"),
                  [Input("category", "value")])
    #pylint: disable=unused-variable
    def update_violin_y(categories):
        """
            Updates the violin year plot

            Args:
                categories: categories to use
        """

        df = u.dfs.filter_data(dfg, categories)

        return plots.violin_plot(df, c.cols.YEAR)


    @app.callback(Output("plot_violin_month", "figure"),
                  [Input("category", "value")])
    #pylint: disable=unused-variable
    def update_violin_m(categories):
        """
            Updates the violin year plot

            Args:
                categories: categories to use
        """

        df = u.dfs.filter_data(dfg, categories)

        return plots.violin_plot(df, c.cols.MONTH)

    return {"body": content}
