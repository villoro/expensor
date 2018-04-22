"""
    Dash app
"""

from dash.dependencies import Input, Output

import constants as c
from app import pages
from dash_app import APP


def get_app_from_url(pathname):
    """
        Gets the app from the pathname
    """

    if (pathname == "/") or (pathname == c.dash.LINK_EVOLUTION):
        return pages.app_evolution

    elif pathname == c.dash.LINK_COMPARISON:
        return pages.app_comparison

    elif pathname == c.dash.LINK_HEATMAPS:
        return pages.app_heatmaps

    elif pathname == c.dash.LINK_VIOLINS:
        return pages.app_violins

    elif pathname == c.dash.LINK_PIES:
        return pages.app_pies

    return None


@APP.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_content(pathname):
    """Updates content based on current page"""

    m_app = get_app_from_url(pathname)

    if m_app is not None:
        return m_app.CONTENT

    return "404"


@APP.callback(Output('sidebar', 'children'),
              [Input('url', 'pathname')])
def display_sidebar(pathname):
    """Updates sidebar based on current page"""

    m_app = get_app_from_url(pathname)

    if m_app is not None:
        return m_app.SIDEBAR

    return "404"



if __name__ == '__main__':
    APP.run_server(debug=True)
