"""
    Dash app
"""

from dash import Dash
from dash_bootstrap_components.themes import BOOTSTRAP

import layout
import constants as c


def create_dash_app():
    """
        Creates the dash app and gets the related data
    """

    app = Dash("expensor", external_stylesheets=[BOOTSTRAP])
    app.config.supress_callback_exceptions = True

    app.title = c.names.TITLE
    app.layout = layout.get_layout()

    return app
