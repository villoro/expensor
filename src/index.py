"""
    Dash app
"""

from dash.dependencies import Input, Output

from pages import get_pages
from dash_app import create_dash_app


# Create dash app with styles
APP = create_dash_app()
SERVER = APP.server

# Add pages with content, sidebar and callbacks
PAGES = get_pages(APP)


@APP.callback(Output("body", "children"), [Input("url", "pathname")])
# pylint: disable=unused-variable
def display_content(pathname):
    """Updates content based on current page"""

    if pathname in PAGES:
        return PAGES[pathname].get_body_html()
    return "404"


@APP.callback(Output("filters", "children"), [Input("url", "pathname")])
# pylint: disable=unused-variable
def display_filters(pathname):
    """ Updates content based on current page """

    if pathname in PAGES:
        return PAGES[pathname].get_filters()
    return "404"


@APP.callback(Output("filters-container", "is_open"), [Input("filters-button", "n_clicks")])
def toggle_filters(count):
    """ hides/opens the filter block """

    # Toggle between show and hide
    return count % 2 == 1 if count is not None else False


if __name__ == "__main__":
    APP.run_server(debug=True)
