"""
    Dash app
"""

import dash_core_components as dcc
from dash.dependencies import Input, Output

import utilities as u
import constants as c
import layout as lay
from plots import plots_heatmaps as plots


class Page(lay.AppPage):
    """ Page Heatmaps """

    link = c.dash.LINK_HEATMAPS

    def __init__(self, app):
        super().__init__([c.dash.INPUT_CATEGORIES])

        @app.callback(
            [Output(f"plot_heat_{x}", "figure") for x in ["i", "e", "distribution"]],
            [
                Input("global_df", "children"),
                Input("input_categories", "value"),
                Input("heat_aux", "children"),
            ],
        )
        # pylint: disable=unused-variable,unused-argument
        def update_plots(df_in, categories, aux):
            """
                Updates the plots

                Args:
                    df_in:      transactions dataframe
                    categories: categories to use
            """
            df = u.dfs.filter_data(u.uos.b64_to_df(df_in), categories)
            return (
                plots.get_heatmap(df, c.names.INCOMES),
                plots.get_heatmap(df, c.names.EXPENSES),
                plots.dist_plot(df),
            )

    def get_body(self):
        return [
            lay.two_columns(
                [
                    lay.card(dcc.Graph(id="plot_heat_i", config=c.dash.PLOT_CONFIG)),
                    lay.card(dcc.Graph(id="plot_heat_e", config=c.dash.PLOT_CONFIG)),
                ]
            ),
            lay.card(dcc.Graph(id="plot_heat_distribution", config=c.dash.PLOT_CONFIG)),
            lay.get_dummy_div("heat_aux"),
        ]
