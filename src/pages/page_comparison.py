"""
    Dash app
"""

import dash_bootstrap_components as dbc
import dash_core_components as dcc
from dash.dependencies import Input, Output

import utilities as u
import constants as c
import layout as lay
from plots import plots_comparison as plots


class Page(lay.AppPage):
    """ Page Comparison """

    link = c.dash.LINK_COMPARISON
    radio_opt = lay.get_options([c.names.INCOMES, c.names.EXPENSES, c.names.EBIT])


    def __init__(self, app):
        super().__init__([
            c.dash.INPUT_CATEGORIES,
            c.dash.INPUT_SMOOTHING,
        ])

        @app.callback(Output("plot_comp_1", "figure"),
                      [Input("global_df", "children"),
                       Input("input_categories", "value"),
                       Input("input_smoothing", "value"),
                       Input("radio_comp_1", "value"),
                       Input("comp_aux", "children")])
        #pylint: disable=unused-variable,unused-argument
        def update_ts_grad_1(df_in, categories, avg_month, type_trans, aux):
            """
                Updates the timeserie gradient plot

                Args:
                    df_in:      transactions dataframe
                    categories: categories to use
                    avg_month:  month to use in rolling average
            """

            df = u.uos.b64_to_df(df_in)
            df = u.dfs.filter_data(df, categories)

            return plots.ts_gradient(df, type_trans, avg_month)


        @app.callback(Output("plot_comp_2", "figure"),
                      [Input("global_df", "children"),
                       Input("input_categories", "value"),
                       Input("input_smoothing", "value"),
                       Input("radio_comp_2", "value"),
                       Input("comp_aux", "children")])
        #pylint: disable=unused-variable,unused-argument
        def update_ts_grad_2(df_in, categories, avg_month, type_trans, aux):
            """
                Updates the timeserie gradient plot

                Args:
                    df_in:      transactions dataframe
                    categories: categories to use
                    avg_month:  month to use in rolling average
            """

            df = u.uos.b64_to_df(df_in)
            df = u.dfs.filter_data(df, categories)

            return plots.ts_gradient(df, type_trans, avg_month)


    def get_body(self):
        return [
            lay.card([
                dcc.Graph(id="plot_comp_1", config=c.dash.PLOT_CONFIG),
                dbc.RadioItems(
                    id="radio_comp_1", options=self.radio_opt,
                    value=c.names.INCOMES, inline=True
                )
            ]),
            lay.card([
                dcc.Graph(id="plot_comp_2", config=c.dash.PLOT_CONFIG),
                dbc.RadioItems(
                    id="radio_comp_2", options=self.radio_opt,
                    value=c.names.EXPENSES, inline=True
                )
            ]),
            lay.get_dummy_div("comp_aux")
        ]
