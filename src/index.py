"""
    Dash app
"""

from dash.dependencies import Input, Output

import constants as c
import utilities as u
from app.layout import layout
from app.pages import app1, app2
from dash_app import APP


log = u.ulog.set_logger(__name__)


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
