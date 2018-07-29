"""
    Dash app
"""

import dash_core_components as dcc
from dash.dependencies import Input, Output

import utilities as u
import constants as c
from app import ui_utils as uiu
from plots import plots_comparison as plots


LINK = c.dash.LINK_COMPARISON


def get_content(app):
    """
        Creates the page

        Args:
            app:            dash app

        Returns:
            dict with content:
                body:       body of the page
    """

    radio_opt = uiu.get_options([c.names.INCOMES, c.names.EXPENSES, c.names.EBIT])

    content = [
        [
            dcc.Graph(id="plot_comp_i", config=uiu.PLOT_CONFIG),
            dcc.RadioItems(
                id="radio_comp_1", options=radio_opt,
                value=c.names.INCOMES, labelStyle={'display': 'inline-block'}
            )
        ],
        [
            dcc.Graph(id="plot_comp_e", config=uiu.PLOT_CONFIG),
            dcc.RadioItems(
                id="radio_comp_2", options=radio_opt,
                value=c.names.EXPENSES, labelStyle={'display': 'inline-block'}
            )
        ]
    ]

    sidebar = [
        ("Categories", dcc.Dropdown(id="drop_comp_categ", multi=True)),
        ("Rolling Average", dcc.Slider(
            id="slider_comp_rolling_avg",
            min=1, max=12, value=1,
            marks={i: str(i) if i > 1 else "None" for i in range(1, 13)},
        ))
    ]


    @app.callback(Output("drop_comp_categ", "options"),
                  [Input("global_categories", "children"),
                   Input("comp_aux", "children")])
    #pylint: disable=unused-variable,unused-argument
    def update_categories(categories, aux):
        """
            Updates categories dropdown with the actual categories
        """

        return uiu.get_options(categories)


    @app.callback(Output("plot_comp_i", "figure"),
                  [Input("global_df_trans", "children"),
                   Input("drop_comp_categ", "value"),
                   Input("slider_comp_rolling_avg", "value"),
                   Input("radio_comp_1", "value"),
                   Input("comp_aux", "children")])
    #pylint: disable=unused-variable,unused-argument
    def update_ts_grad_1(df_trans, categories, avg_month, type_trans, aux):
        """
            Updates the timeserie gradient plot

            Args:
                df_trans:   transactions dataframe
                categories: categories to use
                avg_month:  month to use in rolling average
        """

        df = u.uos.b64_to_df(df_trans)
        df = u.dfs.filter_data(df, categories)

        return plots.ts_gradient(df, type_trans, avg_month)


    @app.callback(Output("plot_comp_e", "figure"),
                  [Input("global_df_trans", "children"),
                   Input("drop_comp_categ", "value"),
                   Input("slider_comp_rolling_avg", "value"),
                   Input("radio_comp_2", "value"),
                   Input("comp_aux", "children")])
    #pylint: disable=unused-variable,unused-argument
    def update_ts_grad_2(df_trans, categories, avg_month, type_trans, aux):
        """
            Updates the timeserie gradient plot

            Args:
                df_trans:   transactions dataframe
                categories: categories to use
                avg_month:  month to use in rolling average
        """

        df = u.uos.b64_to_df(df_trans)
        df = u.dfs.filter_data(df, categories)

        return plots.ts_gradient(df, type_trans, avg_month)

    return {
        c.dash.DUMMY_DIV: "comp_aux",
        c.dash.KEY_BODY: content,
        c.dash.KEY_SIDEBAR: sidebar
    }
