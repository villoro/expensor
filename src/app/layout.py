"""
    Dash app
"""

import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

from static.styles import style_header, style_sidebar, style_filters_container, style_body

PLOT_CONFIG = {
    "displaylogo": False,
    "modeBarButtonsToRemove": ["sendDataToCloud", "select2d", "lasso2d", "resetScale2d"]
}

layout = html.Div([
    # URL tracker
    html.Link(rel='stylesheet', href='/static/styles.css'),
    dcc.Location(id='url', refresh=False),

    # Header
    html.Div([
        html.H1("ExpensORpy")
    ], style=style_header),

    # Sidebar
    html.Div(id="sidebar", style=style_sidebar),

    # Header
    html.Div([
        html.H2("Filters")
    ], style=style_filters_container),

    # Body
    html.Div(id="page-content", style=style_body),
])
