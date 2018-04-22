"""
    Dash app
"""

from dash.dependencies import Input, Output

from app import pages
from dash_app import APP


def get_app_from_url(pathname):
    """
        Gets the app from the pathname
    """

    if pathname in pages.ALL_APPS:
        return pages.ALL_APPS[pathname]
    return None


@APP.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_content(pathname):
    """Updates content based on current page"""

    if pathname in pages.ALL_APPS:
        return pages.ALL_APPS[pathname].CONTENT
    return "404"


@APP.callback(Output('sidebar', 'children'),
              [Input('url', 'pathname')])
def display_sidebar(pathname):
    """Updates sidebar based on current page"""

    if pathname in pages.ALL_APPS:
        return pages.ALL_APPS[pathname].SIDEBAR
    return "404"



if __name__ == '__main__':
    APP.run_server(debug=True)
