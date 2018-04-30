"""
    Dash app
"""

import dash_core_components as dcc
from dash.dependencies import Input, Output

import utilities as u
import constants as c
from app import ui_utils as uiu
from plots import plots_evolution as plots


LINK = c.dash.LINK_EVOLUTION


def get_content(app):
    """
        Creates the page

        Args:
            app:            dash app

        Returns:
            dict with content:
                body:       body of the page
                sidebar:    content of the sidebar
    """

    content = [
        dcc.Graph(id="plot_evol", config=uiu.PLOT_CONFIG),
        [
            dcc.Graph(id="plot_evo_detail", config=uiu.PLOT_CONFIG),
            dcc.RadioItems(
                id="radio_evol_type",
                options=uiu.get_options([c.names.EXPENSES, c.names.INCOMES]),
                value=c.names.EXPENSES,
                labelStyle={'display': 'inline-block'}
            )
        ],
        uiu.get_dummy_div("evo_aux")
    ]

    sidebar = [
        ("Categories", dcc.Dropdown(id="drop_evol_categ", multi=True)),
        ("Group by", dcc.RadioItems(
            id="radio_evol_tw", value="M",
            options=[{"label": "Day", "value": "D"},
                     {"label": "Month", "value": "M"},
                     {"label": "Year", "value": "Y"}]
            )
        ),
    ]


    @app.callback(Output("drop_evol_categ", "options"),
                  [Input("global_categories", "children"),
                   Input("evo_aux", "children")])
    #pylint: disable=unused-variable
    def update_categories(categories, aux):
        """
            Updates categories dropdown with the actual categories
        """

        return uiu.get_options(categories)


    @app.callback(Output("plot_evol", "figure"),
                  [Input("global_df_trans", "children"),
                   Input("drop_evol_categ", "value"),
                   Input("radio_evol_tw", "value"),
                   Input("evo_aux", "children")])
    #pylint: disable=unused-variable
    def update_timeserie_plot(df_trans, categories, timewindow, aux):
        """
            Updates the timeserie plot

            Args:
                df_trans:   transactions dataframe
                categories:	categories to use
                timewindow:	timewindow to use for grouping
        """

        df = u.uos.b64_to_df(df_trans)
        df = u.dfs.filter_data(df, categories)

        return plots.plot_timeserie(df, timewindow)


    @app.callback(Output("plot_evo_detail", "figure"),
                  [Input("global_df_trans", "children"),
                   Input("drop_evol_categ", "value"),
                   Input("radio_evol_type", "value"),
                   Input("radio_evol_tw", "value")])
    #pylint: disable=unused-variable
    def update_ts_by_categories_plot(df_trans, categories, type_trans, timewindow):
        """
            Updates the timeserie by categories plot

            Args:
                df_trans:   transactions dataframe
                categories: categories to use
                type_trans: type of transacions [Expenses/Inc]
                timewindow: timewindow to use for grouping
        """

        df = u.uos.b64_to_df(df_trans)
        df = u.dfs.filter_data(df, categories)

        return plots.plot_timeserie_by_categories(df, type_trans, timewindow)

    return {c.dash.KEY_BODY: content, c.dash.KEY_SIDEBAR: sidebar}
