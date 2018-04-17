"""
    Dash app
"""

import dash_core_components as dcc
from dash.dependencies import Input, Output

import utilities as u
import constants as c
from app import layout
from dash_app import DFG, CATEGORIES, APP
from plots import plots


CONTENT = [
    layout.get_body_elem(
        []
    ),
]

SIDEBAR = layout.create_sidebar(
    CATEGORIES,
)
