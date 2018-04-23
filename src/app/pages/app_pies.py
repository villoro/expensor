"""
    Dash app
"""

import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import utilities as u
import constants as c
from app import layout
from dash_app import DFG, CATEGORIES, APP
from plots import plots_pies as plots

YEARS = sorted(DFG[c.cols.YEAR].unique())

CONTENT = []

for num, default_years in enumerate([YEARS[-1], YEARS]):

    print("Start", "drop_pie_{}".format(num), "pie_{}_{}".format(num, c.names.INCOMES))
    CONTENT.append(
        layout.get_body_elem([
            dcc.Dropdown(
                id="drop_pie_{}".format(num),
                options=layout.get_options(YEARS),
                value=default_years,
                multi=True
            ),
            layout.get_row([
                layout.get_one_column(
                    dcc.Graph(
                        id="pie_{}_{}".format(num, c.names.INCOMES),
                        config=layout.PLOT_CONFIG,
                        figure=plots.get_pie(DFG, c.names.INCOMES, default_years)
                    ), n_rows=6
                ),
                layout.get_one_column(
                    dcc.Graph(
                        id="pie_{}_{}".format(num, c.names.EXPENSES),
                        config=layout.PLOT_CONFIG,
                        figure=plots.get_pie(DFG, c.names.EXPENSES, default_years)
                    ), n_rows=6
                )
            ])
        ]),
    )

SIDEBAR = layout.create_sidebar(
    CATEGORIES,
)
