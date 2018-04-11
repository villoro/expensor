"""
    Dash app
"""
import os
from flask import send_from_directory
from dash import Dash
from dash.dependencies import Input, Output

import utilities as u
import constants as c
from app import layout


log = u.ulog.set_logger(__name__)

APP = Dash()
APP.config.supress_callback_exceptions = True
APP.css.config.serve_locally = True

DFG = u.uos.get_df(c.os.FILE_DATA_SAMPLE)
CATEGORIES = DFG[c.cols.CATEGORY].unique().tolist()

APP.layout = layout.get_layout(CATEGORIES)


@APP.callback(Output('df', 'children'), [Input("category", "value")])
def filter_data(categories):
    """
        Filters the dataframe that will be reused in all plots

        Args:
            categories
    """

    df = DFG.copy()

    if categories:
        if isinstance(categories, list):
            df = df[df[c.cols.CATEGORY].isin(categories)]
        else:
            df = df[df[c.cols.CATEGORY] == categories]

    return df.to_json()


@APP.server.route('/static/<path:path>')
def static_file(path):
    """Adds local css to dash """
    static_folder = os.path.join(os.getcwd(), 'static')
    return send_from_directory(static_folder, path)
