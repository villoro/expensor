"""
    Dash app
"""

import dash_core_components as dcc
from dash.dependencies import Input, Output

import utilities as u
import constants as c
from app import layout
from dash_app import DFG, CATEGORIES, APP
from plots import plots_heatmaps as plots


CONTENT = [
    layout.get_body_elem([
        layout.get_one_column(
            dcc.Graph(
                id="heatmap_i", config=layout.PLOT_CONFIG,
                figure=plots.get_heatmap(DFG, c.names.INCOMES)
            ), n_rows=6),
        layout.get_one_column(
            dcc.Graph(
                id="heatmap_e", config=layout.PLOT_CONFIG,
                figure=plots.get_heatmap(DFG, c.names.EXPENSES)
            ), n_rows=6
        )]
    ),
    layout.get_body_elem(
        dcc.Graph(
            id="dist_plot", config=layout.PLOT_CONFIG,
            figure=plots.dist_plot(DFG)
        )
    ),
]

SIDEBAR = layout.create_sidebar(
    CATEGORIES,
)
