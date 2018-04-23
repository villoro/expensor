"""
    Dash app
"""

import dash_core_components as dcc
from dash.dependencies import Input, Output

import utilities as u
import constants as c
from app import layout
from dash_app import DFG, CATEGORIES, APP
from plots import plots_pies as plots

YEARS = sorted(DFG[c.cols.YEAR].unique())

CONTENT = []

for num, default_years in enumerate([YEARS[-1], None]):

    CONTENT.append(
        [
            dcc.Dropdown(
                id="drop_pie_{}".format(num),
                options=layout.get_options(YEARS),
                value=default_years,
                multi=True
            ),
            layout.get_row([
                layout.get_one_column(
                    dcc.Graph(
                        id="plot_pie_{}_{}".format(num, c.names.INCOMES),
                        config=layout.PLOT_CONFIG,
                        figure=plots.get_pie(DFG, c.names.INCOMES, default_years)
                    ), n_rows=6
                ),
                layout.get_one_column(
                    dcc.Graph(
                        id="plot_pie_{}_{}".format(num, c.names.EXPENSES),
                        config=layout.PLOT_CONFIG,
                        figure=plots.get_pie(DFG, c.names.EXPENSES, default_years)
                    ), n_rows=6
                )
            ])
        ],
    )

CONTENT = layout.create_body(CONTENT)

SIDEBAR = layout.create_sidebar(
    CATEGORIES,
)


for num in range(2):

    @APP.callback(Output("plot_pie_{}_{}".format(num, c.names.INCOMES), "figure"),
                  [Input("category", "value"),
                   Input("drop_pie_{}".format(num), "value")])
    def update_pie_incomes(categories, years):
        """
            Updates the incomes pie plot

            Args:
                categories: categories to use
                years:      years to include in pie
        """

        df = u.dfs.filter_data(DFG, categories)

        return plots.get_pie(df, c.names.INCOMES, years)


    @APP.callback(Output("plot_pie_{}_{}".format(num, c.names.EXPENSES), "figure"),
                  [Input("category", "value"),
                   Input("drop_pie_{}".format(num), "value")])
    def update_pie_expenses(categories, years):
        """
            Updates the expenses pie plot

            Args:
                categories: categories to use
                years:      years to include in pie
        """

        df = u.dfs.filter_data(DFG, categories)

        return plots.get_pie(df, c.names.EXPENSES, years)
