"""
    Dash app
"""

from dash.dependencies import Input, Output

from app.pages import get_pages
from dash_app import create_dash_app


def get_dash_app():

    app, dfg, categories = create_dash_app()

    pages_json = get_pages(app, dfg, categories)


    @app.callback(Output('page-content', 'children'),
                  [Input('url', 'pathname')])
    def display_content(pathname):
        """Updates content based on current page"""

        if pathname in pages_json:
            return pages_json[pathname]["content"]
        return "404"


    @app.callback(Output('sidebar', 'children'),
                  [Input('url', 'pathname')])
    def display_sidebar(pathname):
        """Updates sidebar based on current page"""

        if pathname in pages_json:
            return pages_json[pathname]["sidebar"]
        return "404"

    return app


if __name__ == '__main__':
    get_dash_app().run_server(debug=True)
