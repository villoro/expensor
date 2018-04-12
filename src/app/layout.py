"""
    Dash app
"""

import dash_core_components as dcc
import dash_html_components as html

from static import styles


PLOT_CONFIG = {
    "displaylogo": False,
    "modeBarButtonsToRemove": ["sendDataToCloud", "select2d", "lasso2d", "resetScale2d"]
}


def get_options(iterable):
    """
        Populates a dash dropdawn from an iterable
    """
    return [{"label": x, "value": x} for x in iterable]


def get_sidebar_elem(title, data):
    """
        Creates an element for the sidebar

        Args:
            title:  name to display
            data:   what to include in the element

        Return:
            html div with the element
    """

    aux = html.H6(title + ":")
    children = [aux] + data if isinstance(data, list) else [aux, data]

    return html.Div(children, style=styles.STYLE_SIDEBAR_ELEM)


def get_body_elem(data):
    """
        Creates an element for the body

        Args:
            data:   what to include in the element

        Return:
            html div with the element
    """

    return html.Div(data, style=styles.STYLE_DIV_CONTROL_IN_BODY)


def get_layout(categories):
    """
        Creates the dash layout

        Args:
            categories: values for categories dropdown

        Returns:
            html layout
    """
    sidebar = [
        get_sidebar_elem(
            "Sections",
            [
                html.Div(dcc.Link("Evolution", href="/evolution")),
                html.Div(dcc.Link("App 2", href="/app2"))
            ]
        ),
        get_sidebar_elem(
            "Categories",
            dcc.Dropdown(id="category", options=get_options(categories), multi=True)
        ),
        get_sidebar_elem(
            "Group by",
            dcc.RadioItems(id="timewindow", value="M",
                           options=[{"label": "Day", "value": "D"},
                                    {"label": "Month", "value": "M"},
                                    {"label": "Year", "value": "Y"}])
        ),
    ]

    return html.Div([
        # Header
        html.Div([
            html.H1("ExpensORpy", id="title", style={"color": "white"})
        ], style=styles.STYLE_HEADER),

        # Sidebar
        html.Div(sidebar, id="sidebar", style=styles.STYLE_SIDEBAR),

        # Header
        html.Div([
            html.H2("Filters")
        ], style=styles.STYLE_FILTER_DIV),

        # Body
        html.Div(id="page-content", style=styles.STYLE_BODY),

        # Others
        html.Link(rel='stylesheet', href='/static/styles.css'),
        dcc.Location(id='url', refresh=False),
        html.Div(id='df', style={'display': 'none'})
    ])
