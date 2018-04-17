"""
    Dash app
"""
import os
from flask import send_from_directory
from dash import Dash

import utilities as u
import constants as c
from app import layout


APP = Dash()
APP.config.supress_callback_exceptions = True
APP.css.config.serve_locally = True

DFG = u.uos.get_df(c.os.FILE_DATA_SAMPLE)
CATEGORIES = DFG[c.cols.CATEGORY].unique().tolist()

APP.layout = layout.get_layout()


@APP.server.route('/static/<path:path>')
def static_file(path):
    """Adds local css to dash """
    static_folder = os.path.join(os.getcwd(), 'static')
    return send_from_directory(static_folder, path)
