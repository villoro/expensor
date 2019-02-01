"""
    Dash app
"""

from abc import ABC, abstractmethod

import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd # TODO: delete that import

import constants as c
from utilities.uos import df_to_b64
from utilities.dfs import fix_df_trans # TODO: delete that import

DEFAULT_PADDING = 9



# TODO: Move that part...
#DF = u.dfs.fix_df_trans(pd.read_excel(c.io.FILE_DATA_SAMPLE))
DF = fix_df_trans(pd.read_excel(c.io.FILE_DATA_SAMPLE))


def padding(value=DEFAULT_PADDING):
    """ gets a dict with padding in each direction """
    return {f"padding-{x}": f"{value}px" for x in ["right", "left", "top", "bottom"]}


def get_options(iterable):
    """
        Populates a dash dropdawn from an iterable
    """
    return [{"label": x, "value": x} for x in iterable]


FILTERS = {
    c.dash.INPUT_SMOOTHING: (
        "Smoothing:",
        dbc.Input(
            id='input_smoothing',
            type='number',
            value=c.dash.DEFAULT_SMOOTHING,
        ),
    ),
    c.dash.INPUT_TIMEWINDOW: (
        "Grouping:",
        dcc.Dropdown(
            id="input_timewindow",
            value="M",
            options=[
                {"label": "Month ", "value": "M"},
                {"label": "Year ", "value": "Y"}
            ],
        ),
    ),
    c.dash.INPUT_CATEGORIES: (
        "Categories:",
        dcc.Dropdown(
            id="input_categories",
            multi=True,
            options=get_options(DF[c.cols.CATEGORY].unique())
        )
    )
}


def get_layout():
    """ Creates the dash layout """

    navbar_right = dbc.Row(
        [
            dbc.DropdownMenu(
                label="Pages",
                children=[
                    dbc.DropdownMenuItem(
                        x[1:], href=x, id="section_{}".format(x[1:]),
                    ) for x in c.dash.LINKS_ALL
                ],
                direction="left",
                className="mr-1",
            ),
            dbc.Button(
                "Filters",
                id="filters-button",
                className="mr-1",
                color="danger",
            ),
        ],
        no_gutters=True,
        className="ml-auto",
        align="center",
    )

    navbar = dbc.Navbar(
        [
            dbc.Row(
                [
                    dbc.Col(html.Img(src="assets/logo.png", height="30px")),
                    dbc.Col(dbc.NavbarBrand("Expensor", className="ml-2")),
                ],
                align="center",
                no_gutters=True,
            ),
            navbar_right
        ],
        sticky="top",
        className="w3-light-grey w3-card"
    )

    filters = dbc.Collapse(
        dbc.CardDeck(id="filters"), id="filters-container", style=padding(2*DEFAULT_PADDING)
    )

    content = [
        # Body
        html.Div(id="body", style=padding()),

        # Others
        html.Div(id="sync_count", style={"display": "none"}),
        dcc.Location(id='url', refresh=False),

        # Hidden div with data
        html.Div(df_to_b64(DF), id="global_df", style=c.styles.STYLE_HIDDEN),
    ]

    return html.Div([navbar, filters] + content)


def two_columns(elements):
    """
        Creates a layout with two columns.
        In large screens will be displayed as two columns.
        In medium and smalls will be shown as only one.
    """

    return html.Div(
        [
            html.Div(
                x, className="w3-col l6 m12 s12"
            ) for x in elements
        ],
        className="w3-row"
    )

class AppPage(ABC):
    """
        Raw Page class that is meant to be extended
    """

    def __init__(self, mlist=[]):
        self.filters = [FILTERS[x] for x in mlist]


    def get_filters(self):
        """ Retrives the html body """

        return [
            dbc.Card(
                [
                    dbc.CardHeader(title),
                    html.Div(element, className="w3-padding")
                ],
                color="secondary",
                outline=True,
            ) for title, element in self.filters
        ]


    #pylint: disable=R0201
    @abstractmethod
    def get_body(self):
        """
            Dummy function to be overrided by every page. It should create the body
            The @abstractmethod decorator ensures that this function is implemented
        """
        return []


    def get_body_html(self):
        """ Retrives the html body """

        return [
            html.Div(data) for data in self.get_body()
        ]


def card(data, **kwa):
    """ Create one card """

    return html.Div(
        dbc.Card(data, style=padding(), **kwa),
        className="w3-center",
        style=padding(),
    )

def get_dummy_div(name, value="Dummy"):
    """
        Creates a dummy div that will be used to draw plots when a page is loaded
        using the callbacks in the page
    """
    return html.Div(value, id=name, style=c.styles.STYLE_HIDDEN)
