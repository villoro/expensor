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

def get_content(app, dfg, categories):
    """
        Creates the page

        Args:
            app:        dash app
            dfg:        dataframe with all data
            categories: list of categories avaiables

        Returns:
            content:    body of the page
            sidebar:    content of the sidebar
    """

    years = sorted(dfg[c.cols.YEAR].unique())

    content = []

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
                            figure=plots.get_pie(dfg, c.names.INCOMES, default_years)
                        ), n_rows=6
                    ),
                    uiu.get_one_column(
                        dcc.Graph(
                            id="plot_pie_{}_{}".format(num, c.names.EXPENSES),
                            config=uiu.PLOT_CONFIG,
                            figure=plots.get_pie(dfg, c.names.EXPENSES, default_years)
                        ), n_rows=6
                    )
                ])
            ],
        )

    content = uiu.create_body(content)

    sidebar = uiu.create_sidebar(
        categories,
    )


    for num in range(2):

        @app.callback(Output("plot_pie_{}_{}".format(num, c.names.INCOMES), "figure"),
                      [Input("category", "value"),
                       Input("drop_pie_{}".format(num), "value")])
        def update_pie_incomes(categories, years):
            """
                Updates the incomes pie plot

                Args:
                    categories: categories to use
                    years:      years to include in pie
            """

            df = u.dfs.filter_data(dfg, categories)

            return plots.get_pie(df, c.names.INCOMES, years)


        @app.callback(Output("plot_pie_{}_{}".format(num, c.names.EXPENSES), "figure"),
                      [Input("category", "value"),
                       Input("drop_pie_{}".format(num), "value")])
        def update_pie_expenses(categories, years):
            """
                Updates the expenses pie plot

                Args:
                    categories: categories to use
                    years:      years to include in pie
            """

            df = u.dfs.filter_data(dfg, categories)

            return plots.get_pie(df, c.names.EXPENSES, years)

    return content, sidebar
