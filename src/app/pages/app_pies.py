"""
    Dash app
"""

import dash_core_components as dcc
from dash.dependencies import Input, Output

import utilities as u
import constants as c
from app import ui_utils as uiu
from plots import plots_pies as plots


LINK = c.dash.LINK_PIES


def get_content(app):
    """
        Creates the page

        Args:
            app:            dash app

        Returns:
            dict with content:
                body:       body of the page
    """

    years = [2017, 2018] # TODO: fix that!

    sidebar = [("Categories", dcc.Dropdown(id="drop_pie_categ", multi=True))]


    @app.callback(Output("drop_pie_categ", "options"),
                  [Input("global_categories", "children"), Input("pies_aux", "children")])
    #pylint: disable=unused-variable
    def update_categories(categories, aux):
        """
            Updates categories dropdown with the actual categories
        """

        return uiu.get_options(categories)

    content = [uiu.get_dummy_div("pies_aux")]

    for num, default_years in enumerate([years[-1], None]):

        content.append(
            [
                dcc.Dropdown(
                    id="drop_pie_{}".format(num),
                    options=uiu.get_options(years),
                    value=default_years,
                    multi=True
                ),
                uiu.get_row([
                    uiu.get_one_column(
                        dcc.Graph(
                            id="plot_pie_{}_{}".format(num, c.names.INCOMES),
                            config=uiu.PLOT_CONFIG,
                        ), n_rows=6
                    ),
                    uiu.get_one_column(
                        dcc.Graph(
                            id="plot_pie_{}_{}".format(num, c.names.EXPENSES),
                            config=uiu.PLOT_CONFIG,
                        ), n_rows=6
                    )
                ])
            ],
        )

    for num in range(2):

        @app.callback(Output("plot_pie_{}_{}".format(num, c.names.INCOMES), "figure"),
                      [Input("global_df_trans", "children"),
                       Input("drop_pie_categ", "value"),
                       Input("drop_pie_{}".format(num), "value")])
        #pylint: disable=unused-variable
        def update_pie_incomes(df_trans, categories, years):
            """
                Updates the incomes pie plot

                Args:
                    df_trans:   transactions dataframe
                    categories: categories to use
                    years:      years to include in pie
            """

            df = u.uos.b64_to_df(df_trans)
            df = u.dfs.filter_data(df, categories)

            return plots.get_pie(df, c.names.INCOMES, years)


        @app.callback(Output("plot_pie_{}_{}".format(num, c.names.EXPENSES), "figure"),
                      [Input("global_df_trans", "children"),
                       Input("drop_pie_categ", "value"),
                       Input("drop_pie_{}".format(num), "value")])
        #pylint: disable=unused-variable
        def update_pie_expenses(df_trans, categories, years):
            """
                Updates the expenses pie plot

                Args:
                    df_trans:   transactions dataframe
                    categories: categories to use
                    years:      years to include in pie
            """

            df = u.uos.b64_to_df(df_trans)
            df = u.dfs.filter_data(df, categories)

            return plots.get_pie(df, c.names.EXPENSES, years)

    return {c.dash.KEY_BODY: content, c.dash.KEY_SIDEBAR: sidebar}
