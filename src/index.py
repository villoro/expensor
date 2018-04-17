"""
    Dash app
"""

from dash.dependencies import Input, Output

import constants as c
import utilities as u
from app import pages
from dash_app import APP


log = u.ulog.set_logger(__name__)


@APP.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_content(pathname):
    """Updates content based on current page"""

    if (pathname == "/") or (pathname == c.dash.LINK_EVOLUTION):
        return pages.app_evolution.CONTENT
    elif pathname == c.dash.LINK_COMPARISON:
        return pages.app_comparison.CONTENT
    elif pathname == c.dash.LINK_HEATMAPS:
        return pages.app_heatmaps.CONTENT
    return '404'


@APP.callback(Output('sidebar', 'children'),
              [Input('url', 'pathname')])
def display_sidebar(pathname):
    """Updates sidebar based on current page"""

    if (pathname == "/") or (pathname == c.dash.LINK_EVOLUTION):
        return pages.app_evolution.SIDEBAR
    elif pathname == c.dash.LINK_COMPARISON:
        return pages.app_comparison.SIDEBAR
    elif pathname == c.dash.LINK_HEATMAPS:
        return pages.app_heatmaps.SIDEBAR
    return '404'



if __name__ == '__main__':
    APP.run_server(debug=True)
