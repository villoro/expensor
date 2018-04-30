"""
    Dash app
"""

import dash_core_components as dcc
import dash_html_components as html

import utilities as u
from static import styles


def get_layout(df_trans, categories):
    """
        Creates the dash layout

        Args:
            df_trans:   excel bytes of df_trans
    """

    df_trans_bytes = u.uos.df_to_b64(df_trans)

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
        html.Div(df_trans_bytes, id="global_df_trans", style=styles.STYLE_HIDDEN),
        html.Div(categories, id="global_categories", style=styles.STYLE_HIDDEN),
    ])
