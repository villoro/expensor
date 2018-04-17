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
    # layout.get_body_elem(
    #     [
    #         layout.get_one_column()
    #     ]
    # ),
]

SIDEBAR = layout.create_sidebar(
    CATEGORIES,
)
