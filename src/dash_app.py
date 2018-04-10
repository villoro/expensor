"""
    Dash app
"""
import os
import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
from flask import send_from_directory
from dash.dependencies import Input, Output

import constants as c
import utilities as u
from app.layout import layout
from app.pages import app1, app2


log = u.ulog.set_logger(__name__)

APP = dash.Dash()
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


@APP.callback(Output('sidebar', 'children'),
              [Input('url', 'pathname')])
def display_sidebar(pathname):
    """Updates sidebar based on current page"""

    if (pathname == "/") or (pathname == '/app1'):
        return app1.sidebar
    elif pathname == '/app2':
        return app2.sidebar
    else:
        return '404'


@APP.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_content(pathname):
    """Updates content based on current page"""

    if (pathname == "/") or (pathname == '/app1'):
        return app1.content
    elif pathname == '/app2':
        return app2.content
    else:
        return '404'


if __name__ == '__main__':
    APP.run_server(debug=True)
