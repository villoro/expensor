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

    sidebar = [("Categories", dcc.Dropdown(id="drop_pie_categ", multi=True))]

    @app.callback(Output("drop_pie_categ", "options"),
                  [Input("global_categories", "children"), Input("pies_aux", "children")])
    #pylint: disable=unused-variable,unused-argument
    def update_categories(df_categ, aux):
        """
            Updates categories dropdown with the actual categories
        """

        df = u.uos.b64_to_df(df_categ)

        return uiu.get_options(df[c.cols.NAME].unique())


    @app.callback(Output("drop_pie_{}".format(1), "value"),
                  [Input("global_df_trans", "children"), Input("pies_aux", "children")])
    #pylint: disable=unused-variable,unused-argument
    def update_second_dropdown_value(df_trans, aux):
        """
            Sets the value of the second dropdown with year to the last year
        """

        df = u.uos.b64_to_df(df_trans)
        return max(df[c.cols.YEAR].unique().tolist())


    content = []

    # Add plots and dropdowns
    for num in range(2):

        content.append(
            [
                dcc.Dropdown(
                    id="drop_pie_{}".format(num),
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

        @app.callback(Output("drop_pie_{}".format(num), "options"),
                      [Input("global_df_trans", "children"), Input("pies_aux", "children")])
        #pylint: disable=unused-variable,unused-argument
        def update_dropdowns_years_options(df_trans, aux):
            """
                Updates the dropdowns with the years
            """

            df = u.uos.b64_to_df(df_trans)
            return uiu.get_options(df[c.cols.YEAR].unique().tolist())


        @app.callback(Output("plot_pie_{}_{}".format(num, c.names.INCOMES), "figure"),
                      [Input("global_df_trans", "children"),
                       Input("drop_pie_categ", "value"),
                       Input("drop_pie_{}".format(num), "value"),
                       Input("pies_aux", "children")])
        #pylint: disable=unused-variable,unused-argument
        def update_pie_incomes(df_trans, categories, years, aux):
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
                       Input("drop_pie_{}".format(num), "value"),
                       Input("pies_aux", "children")])
        #pylint: disable=unused-variable,unused-argument
        def update_pie_expenses(df_trans, categories, years, aux):
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

    return {
        c.dash.DUMMY_DIV: "pies_aux",
        c.dash.KEY_BODY: content,
        c.dash.KEY_SIDEBAR: sidebar
    }
