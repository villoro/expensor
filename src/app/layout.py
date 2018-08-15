"""
    Dash app
"""

import dash_core_components as dcc
import dash_html_components as html

import constants as c
from utilities.uos import df_to_b64


def get_layout(df):
    """
        Creates the dash layout

        Args:
            dfs:   dict of excel bytes
    """

    return html.Div([
        # Header
        html.Div([
            html.H1(c.names.TITLE, id="title", style={"color": "white"})
        ], style=c.styles.STYLE_HEADER),

        # Sidebar
        html.Div(id="sidebar", style=c.styles.STYLE_SIDEBAR),

        # Sub-header
        html.Div([html.H2("Filters")], style=c.styles.STYLE_FILTER_DIV),

        # Body
        html.Div(id="body", style=c.styles.STYLE_BODY),

        # Others
        dcc.Location(id='url', refresh=False),

        # Hidden div with data
        html.Div(df_to_b64(df), id="global_df", style=c.styles.STYLE_HIDDEN),
    ])
