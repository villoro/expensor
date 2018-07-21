"""
    Dash app
"""

import dash_core_components as dcc
import dash_html_components as html

import constants as c
from static import styles


def get_layout(dfs, categories):
    """
        Creates the dash layout

        Args:
            dfs:   dict of excel bytes
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
        html.Div(dfs[c.dfs.TRANS], id="global_df_trans", style=styles.STYLE_HIDDEN),
        html.Div(dfs[c.dfs.LIQUID], id="global_df_liquid", style=styles.STYLE_HIDDEN),
        html.Div(dfs[c.dfs.LIQUID_LIST], id="global_df_liquid_list", style=styles.STYLE_HIDDEN),
        html.Div(categories, id="global_categories", style=styles.STYLE_HIDDEN),
    ])
