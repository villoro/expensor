"""
    Dash app
"""

import dash_core_components as dcc
import dash_html_components as html

import constants as c


def get_layout(dfs):
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
        html.Div(id="page-content", style=c.styles.STYLE_BODY),

        # Others
        dcc.Location(id='url', refresh=False),

        # Hidden divs with data
        html.Div(dfs[c.dfs.TRANS], id="global_df_trans", style=c.styles.STYLE_HIDDEN),
        html.Div(dfs[c.dfs.CATEG], id="global_categories", style=c.styles.STYLE_HIDDEN),
        html.Div(dfs[c.dfs.LIQUID], id="global_df_liquid", style=c.styles.STYLE_HIDDEN),
        html.Div(dfs[c.dfs.LIQUID_LIST], id="global_df_liquid_list", style=c.styles.STYLE_HIDDEN),
    ])
