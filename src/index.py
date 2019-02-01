"""
    Dash app
"""

from dash.dependencies import Input, Output, State

from pages import get_pages
from dash_app import create_dash_app

import constants as c


# Create dash app with styles
APP = create_dash_app()
SERVER = APP.server

# Add pages with content, sidebar and callbacks
PAGES = get_pages(APP)


@APP.callback(Output('body', 'children'),
              [Input('url', 'pathname')])
#pylint: disable=unused-variable
def display_content(pathname):
    """Updates content based on current page"""

    if pathname in PAGES:
        return PAGES[pathname].get_body_html()
    return "404"


@APP.callback(Output('filters', 'children'),
              [Input('url', 'pathname')])
#pylint: disable=unused-variable
def display_filters(pathname):
    """ Updates content based on current page """

    if pathname in PAGES:
        return PAGES[pathname].get_filters()
    return "404"


@APP.callback(
    Output("filters-container", "is_open"),
    [Input("filters-button", "n_clicks")],
    [State("filters-container", "is_open")],
)
def toggle_filters(count, is_open):
    """ hides/opens the filter block """

    if count:
        return not is_open
    return is_open


if __name__ == '__main__':
    APP.run_server(debug=True)
