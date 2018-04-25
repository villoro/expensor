"""
    Dash app
"""
import os
from flask import send_from_directory
from dash import Dash

from app import layout


def create_dash_app():
    """
        Creates the dash app and gets the related data
    """

    app = Dash()
    app.config.supress_callback_exceptions = True
    app.css.config.serve_locally = True

    app.layout = layout.get_layout()


    @app.server.route('/static/<path:path>')
    #pylint: disable=unused-variable
    def static_file(path):
        """Adds local css to dash """
        static_folder = os.path.join(os.getcwd(), 'static')
        return send_from_directory(static_folder, path)

    return app
