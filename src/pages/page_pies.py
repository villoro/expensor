"""
    Dash app
"""

import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import utilities as u
import constants as c
import layout as lay
from plots import plots_pies as plots


class Page(lay.AppPage):
    """ Page Pies """

    link = c.dash.LINK_PIES

    def __init__(self, app):
        super().__init__([c.dash.INPUT_CATEGORIES])

        @app.callback(
            Output("drop_pie_{}".format(1), "value"),
            [Input("global_df", "children"), Input("pies_aux", "children")],
        )
        # pylint: disable=unused-variable,unused-argument
        def update_second_dropdown_value(df_trans, aux):
            """
                Sets the value of the second dropdown with year to the last year
            """

            df = u.uos.b64_to_df(df_trans)
            return max(df[c.cols.YEAR].unique().tolist())

        for num in range(2):

            @app.callback(
                Output("drop_pie_{}".format(num), "options"),
                [Input("global_df", "children"), Input("pies_aux", "children")],
            )
            # pylint: disable=unused-variable,unused-argument
            def update_dropdowns_years_options(df_in, aux):
                """
                    Updates the dropdowns with the years
                """

                df = u.uos.b64_to_df(df_in)
                return lay.get_options(df[c.cols.YEAR].unique().tolist())

            @app.callback(
                Output("plot_pie_{}_{}".format(num, c.names.INCOMES), "figure"),
                [
                    Input("global_df", "children"),
                    Input("input_categories", "value"),
                    Input("drop_pie_{}".format(num), "value"),
                    Input("pies_aux", "children"),
                ],
            )
            # pylint: disable=unused-variable,unused-argument
            def update_pie_incomes(df_in, categories, years, aux):
                """
                    Updates the incomes pie plot

                    Args:
                        df_in:      transactions dataframe
                        categories: categories to use
                        years:      years to include in pie
                """
                df = u.dfs.filter_data(u.uos.b64_to_df(df_in), categories)
                return plots.get_pie(df, c.names.INCOMES, years)

            @app.callback(
                Output("plot_pie_{}_{}".format(num, c.names.EXPENSES), "figure"),
                [
                    Input("global_df", "children"),
                    Input("input_categories", "value"),
                    Input("drop_pie_{}".format(num), "value"),
                    Input("pies_aux", "children"),
                ],
            )
            # pylint: disable=unused-variable,unused-argument
            def update_pie_expenses(df_in, categories, years, aux):
                """
                    Updates the expenses pie plot

                    Args:
                        df_in:      transactions dataframe
                        categories: categories to use
                        years:      years to include in pie
                """
                df = u.dfs.filter_data(u.uos.b64_to_df(df_in), categories)
                return plots.get_pie(df, c.names.EXPENSES, years)

    def get_body(self):
        body = []

        # Add plots and dropdowns
        # One row default with all data, the other with last year
        for num in range(2):

            body.append(
                lay.card(
                    [
                        html.Div(dcc.Dropdown(id="drop_pie_{}".format(num), multi=True)),
                        lay.two_columns(
                            [
                                dcc.Graph(
                                    id="plot_pie_{}_{}".format(num, c.names.INCOMES),
                                    config=c.dash.PLOT_CONFIG,
                                ),
                                dcc.Graph(
                                    id="plot_pie_{}_{}".format(num, c.names.EXPENSES),
                                    config=c.dash.PLOT_CONFIG,
                                ),
                            ]
                        ),
                    ]
                )
            )

        return body + [lay.get_dummy_div("pies_aux")]
