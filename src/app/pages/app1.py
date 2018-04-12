"""
    Dash app
"""

import pandas as pd
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import constants as c
from app.layout import PLOT_CONFIG
from static import styles
from dash_app import DFG, APP
from plots import plots


CONTENT = [
    html.Div(
        dcc.Graph(
            id="plot_ts", config=PLOT_CONFIG,
            figure=plots.plot_timeserie(DFG)
        ),
        style=styles.STYLE_DIV_CONTROL_IN_BODY
    ),
    html.Div(
        [
            dcc.Graph(
                id="plot_ts_detail", config=PLOT_CONFIG,
                figure=plots.plot_timeserie_by_categories(DFG)
            ),
            dcc.RadioItems(
                id="radio_type_trans",
                options=[
                    {'label': c.names.EXPENSES, 'value': c.names.EXPENSES},
                    {'label': c.names.INCOMES, 'value': c.names.INCOMES},
                ],
                value=c.names.EXPENSES,
                labelStyle={'display': 'inline-block'}
            )
        ],
        style=styles.STYLE_DIV_CONTROL_IN_BODY
    ),
]


@APP.callback(Output("plot_ts", "figure"),
              [Input("df", "children"), Input("timewindow", "value")])
def update_timeserie_plot(df_input, timewindow):
    """
        Updates the timeserie plot

        Args:
            df_input:	dataframe to use
            timewindow:	timewindow to use for grouping
    """

    df = DFG if df_input is None else pd.read_json(df_input)

    return plots.plot_timeserie(df, timewindow)


@APP.callback(Output("plot_ts_detail", "figure"),
              [Input("df", "children"), Input("radio_type_trans", "value"),
               Input("timewindow", "value")])
def update_timeserie_by_categories_plot(df_input, type_trans, timewindow):
    """
        Updates the timeserie by categories plot

        Args:
            df_input:   dataframe to use
            timewindow: timewindow to use for grouping
    """

    df = DFG if df_input is None else pd.read_json(df_input)

    return plots.plot_timeserie_by_categories(df, type_trans, timewindow)
