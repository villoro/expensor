"""
    Dash app
"""
import os
import pandas as pd
from flask import send_from_directory
from dash import Dash
from dash.dependencies import Input, Output

import utilities as u
from app.layout import layout


log = u.ulog.set_logger(__name__)

APP = Dash()
APP.config.supress_callback_exceptions = True
APP.css.config.serve_locally = True

APP.layout = layout

DFG = pd.read_excel("../data/data.xlsx", "Expenses_raw")
CATEGORIES = DFG["Type"].unique().tolist()


@APP.callback(Output('df', 'children'), [Input("category", "value")])
def filter_data(values):
    df = DFG.copy()

    if values:
        if isinstance(values, list):
            df = df[df["Type"].isin(values)]
        else:
            df = df[df["Type"] == values]

    return df.to_json()


@APP.server.route('/static/<path:path>')
def static_file(path):
    """Adds local css to dash """
    static_folder = os.path.join(os.getcwd(), 'static')
    return send_from_directory(static_folder, path)
