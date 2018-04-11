"""
    Dash app
"""

from dash.dependencies import Input, Output

import utilities as u
from app.pages import app1, app2
from dash_app import APP


log = u.ulog.set_logger(__name__)


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
