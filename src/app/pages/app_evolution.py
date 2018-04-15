"""
    Dash app
"""

import dash_core_components as dcc
from dash.dependencies import Input, Output

import utilities as u
import constants as c
from app import layout
from dash_app import DFG, APP
from plots import plots


CONTENT = [
    layout.get_body_elem(
        dcc.Graph(
            id="plot_ts", config=layout.PLOT_CONFIG,
            figure=plots.plot_timeserie(DFG)
        )
    ),
    layout.get_body_elem(
        [
            dcc.Graph(
                id="plot_ts_detail", config=layout.PLOT_CONFIG,
                figure=plots.plot_timeserie_by_categories(DFG)
            ),
            dcc.RadioItems(
                id="radio_type_trans",
                options=layout.get_options([c.names.EXPENSES, c.names.INCOMES]),
                value=c.names.EXPENSES,
                labelStyle={'display': 'inline-block'}
            )
        ]
    ),
]


@APP.callback(Output("plot_ts", "figure"),
              [Input("category", "value"), Input("timewindow", "value")])
def update_timeserie_plot(categories, timewindow):
    """
        Updates the timeserie plot

        Args:
            categories:	categories to use
            timewindow:	timewindow to use for grouping
    """

    df = u.dfs.filter_data(DFG, categories)

    return plots.plot_timeserie(df, timewindow)


@APP.callback(Output("plot_ts_detail", "figure"),
              [Input("category", "value"), Input("radio_type_trans", "value"),
               Input("timewindow", "value")])
def update_ts_by_categories_plot(categories, type_trans, timewindow):
    """
        Updates the timeserie by categories plot

        Args:
            categories: categories to use
            timewindow: timewindow to use for grouping
    """

    df = u.dfs.filter_data(DFG, categories)

    return plots.plot_timeserie_by_categories(df, type_trans, timewindow)
