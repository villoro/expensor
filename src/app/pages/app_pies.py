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

CONTENT = [
    layout.get_body_elem([
        dcc.Dropdown(
            id="drop-pie_1",
            options=layout.get_options(YEARS),
            value=YEARS[-1],
            multi=True
        ),
        layout.get_row([
            layout.get_one_column(
                dcc.Graph(
                    id="pie_1_i", config=layout.PLOT_CONFIG,
                    #figure=plots.plot_timeserie(DFG)
                ), n_rows=6
            ),
            layout.get_one_column(
                dcc.Graph(
                    id="pie_1_e", config=layout.PLOT_CONFIG,
                    #figure=plots.plot_timeserie(DFG)
                ), n_rows=6
            )
        ])
    ]),
    layout.get_body_elem([
        dcc.Dropdown(
            id="drop-pie_2",
            options=layout.get_options(YEARS),
            value=YEARS,
            multi=True
        ),
        layout.get_row([
            layout.get_one_column(
                dcc.Graph(
                    id="pie_2_i", config=layout.PLOT_CONFIG,
                    #figure=plots.plot_timeserie(DFG)
                ), n_rows=6
            ),
            layout.get_one_column(
                dcc.Graph(
                    id="pie_2_e", config=layout.PLOT_CONFIG,
                    #figure=plots.plot_timeserie(DFG)
                ), n_rows=6
            )
        ])
    ]),
]

SIDEBAR = layout.create_sidebar(
    CATEGORIES,
)
