"""
    Dash app
"""

import dash_core_components as dcc
import dash_html_components as html

from static import styles


def get_layout():
    """
        Creates the dash layout
    """

    return html.Div([
        # Header
        html.Div([
            html.H1("ExpensORpy", id="title", style={"color": "white"})
        ], style=styles.STYLE_HEADER),

        # Sidebar
        html.Div(id="sidebar", style=styles.STYLE_SIDEBAR),

        # Header
        html.Div([
            html.H2("Filters")
        ], style=styles.STYLE_FILTER_DIV),

        # Body
        html.Div(id="page-content", style=styles.STYLE_BODY),

        # Others
        html.Link(rel='stylesheet', href='/static/styles.css'),
        dcc.Location(id='url', refresh=False),
    ])
