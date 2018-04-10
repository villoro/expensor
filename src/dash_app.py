"""
    Dash app
"""
import os
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

app = dash.Dash()
app.config.supress_callback_exceptions = True
app.css.config.serve_locally = True

app.layout = layout


@app.server.route('/static/<path:path>')
def static_file(path):
    static_folder = os.path.join(os.getcwd(), 'static')
    return send_from_directory(static_folder, path)


@app.callback(Output('sidebar', 'children'),
              [Input('url', 'pathname')])
def display_sidebar(pathname):

    if (pathname == "/") or (pathname == '/app1'):
        return app1.sidebar
    elif pathname == '/app2':
        return app2.sidebar
    else:
        return '404'


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_content(pathname):

    if (pathname == "/") or (pathname == '/app1'):
        return app1.content
    elif pathname == '/app2':
        return app2.content
    else:
        return '404'


if __name__ == '__main__':
    app.run_server(debug=True)
