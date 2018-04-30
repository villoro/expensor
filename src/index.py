"""
    Dash app
"""

from dash.dependencies import Input, Output

from app.pages import get_pages
from dash_app import create_dash_app

import constants as c

def get_dash_app():
    """
        Gets the dash app with all pages, callbacks and content
    """

    # Create dash app with styles
    app = create_dash_app()

    # Add pages with content, sidebar and callbacks
    pages_json = get_pages(app)

    @app.callback(Output('page-content', 'children'),
                  [Input('url', 'pathname')])
    #pylint: disable=unused-variable
    def display_content(pathname):
        """Updates content based on current page"""

        if pathname in pages_json:
            return pages_json[pathname][c.dash.KEY_BODY]
        return "404"


    @app.callback(Output('sidebar', 'children'),
                  [Input('url', 'pathname')])
    #pylint: disable=unused-variable
    def display_sidebar(pathname):
        """Updates sidebar based on current page"""

        if pathname in pages_json:
            return pages_json[pathname][c.dash.KEY_SIDEBAR]
        return "404"

    return app


if __name__ == '__main__':
    get_dash_app().run_server(debug=True)
