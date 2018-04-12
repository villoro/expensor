"""
    Dash app
"""

from dash.dependencies import Input, Output

import utilities as u
from app.pages import app_evolution, app2
from dash_app import APP


log = u.ulog.set_logger(__name__)


@APP.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_content(pathname):
    """Updates content based on current page"""

    if (pathname == "/") or (pathname == '/evolution'):
        return app_evolution.CONTENT
    elif pathname == '/app2':
        return app2.CONTENT
    return '404'



if __name__ == '__main__':
    APP.run_server(debug=True)
