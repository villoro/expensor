"""
    Dash app
"""

import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

from static import styles

PLOT_CONFIG = {
    "displaylogo": False,
    "modeBarButtonsToRemove": ["sendDataToCloud", "select2d", "lasso2d", "resetScale2d"]
}

layout = html.Div([
    # Header
    html.Div([
        html.H1("ExpensORpy", id="title")
    ], style=styles.style_header),

    # Sidebar
    html.Div(id="sidebar", style=styles.style_sidebar),

    # Header
    html.Div([
        html.H2("Filters")
    ], style=styles.style_filters_container),

    # Body
    html.Div(id="page-content", style=styles.style_body),

    # Others
    html.Link(rel='stylesheet', href='/static/styles.css'),
    dcc.Location(id='url', refresh=False),
    html.Div(id='df', style={'display': 'none'})
])


def get_sidebar_elem(title, children):
    """
        Creates an element for the sidebar

        Args:
            title:      name to display
            children:   what to include in the element

        Return:
            html div with the element
    """

    return html.Div([html.H6(title + ":"), children], style=styles.style_sidebar_elem)