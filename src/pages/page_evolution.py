"""
    Dash app
"""

import dash_bootstrap_components as dbc
import dash_core_components as dcc
from dash.dependencies import Input, Output

import utilities as u
import constants as c
import layout as lay
from plots import plots_evolution as plots


class Page(lay.AppPage):
    """ Page Evolution """

    link = c.dash.LINK_EVOLUTION
    def_type = c.names.EXPENSES
    def_tw = "M"

    def __init__(self, app):
        super().__init__([c.dash.INPUT_CATEGORIES, c.dash.INPUT_SMOOTHING, c.dash.INPUT_TIMEWINDOW])

        @app.callback(
            [Output(f"plot_{x}", "figure") for x in ["evol", "evo_detail"]],
            [
                Input("global_df", "children"),
                Input("input_categories", "value"),
                Input("input_timewindow", "value"),
                Input("radio_evol_type", "value"),
                Input("evo_aux", "children"),
            ],
        )
        # pylint: disable=unused-variable,unused-argument
        def update_plots(df_in, categories, timewindow, type_trans, aux):
            """
                Updates the plots

                Args:
                    df_in:      transactions dataframe
                    categories: categories to use
                    timewindow: timewindow to use for grouping
                    type_trans: type of transacions [Expenses/Inc]
            """

            df = u.dfs.filter_data(u.uos.b64_to_df(df_in), categories)
            return (
                plots.plot_timeserie(df, timewindow),
                plots.plot_timeserie_by_categories(df, type_trans, timewindow),
            )

    def get_body(self):
        return [
            lay.card(dcc.Graph(id="plot_evol", config=c.dash.PLOT_CONFIG)),
            lay.card(
                [
                    dcc.Graph(id="plot_evo_detail", config=c.dash.PLOT_CONFIG),
                    dbc.RadioItems(
                        id="radio_evol_type",
                        options=lay.get_options([c.names.EXPENSES, c.names.INCOMES]),
                        value=self.def_type,
                        inline=True,
                    ),
                ]
            ),
            lay.get_dummy_div("evo_aux"),
        ]