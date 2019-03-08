"""
    Dash app
"""

import pandas as pd
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import dash_table as dt
from dash import callback_context
from dash.dependencies import Input, Output, State

import constants as c
import utilities as u
import layout as lay
from plots import plots_upload as plots


class Page(lay.AppPage):
    """ Page Evolution """

    link = c.dash.LINK_UPLOAD
    def_type = c.names.EXPENSES
    def_tw = "M"
    rows_preview = 20

    style_table = {
        "style_header": c.styles.STYLE_TABLE_HEADER,
        "style_cell": c.styles.STYLE_TABLE_CELL,
    }

    def __init__(self, app):
        super().__init__([])

        @app.callback(
            [Output("upload_table_preview", "columns"), Output("upload_table_preview", "data")],
            [Input("upload_container", "contents"), Input("upload_container", "filename")],
        )
        # pylint: disable=unused-variable
        def update_table(contents, filename):
            """
                Update the preview table

                Args:
                    contents:   file uploaded
                    filename:   name of the file uploaded
            """

            df = u.uos.parse_dataframe_uploaded(contents, filename)

            if isinstance(df, str):
                return [], {}

            return (
                [{"name": i, "id": i} for i in df.columns],
                df.head(self.rows_preview).to_dict("rows"),
            )

        @app.callback(
            [
                Output("upload_colapse_error_message", "is_open"),
                Output("upload_colapse_preview", "is_open"),
                Output("upload_colapse_success_message", "is_open"),
                Output("global_df", "children"),
            ],
            [
                Input("upload_container", "contents"),
                Input("upload_container", "filename"),
                Input("upload_button", "n_clicks"),
            ],
            [State("global_df", "children")],
        )
        # pylint: disable=unused-variable
        def show_collapsibles(contents, filename, n_clicks, df_old):
            """
                Shows/hide the collapsibles and updates the global df if needed

                Args:
                    error_text: text of error message
            """

            df = u.uos.parse_dataframe_uploaded(contents, filename)

            if df is None:
                return False, False, False, df_old

            elif isinstance(df, str):
                return True, False, False, df_old

            context = callback_context

            # If sync button pressed, sync the app
            if context.triggered and context.triggered[0]["prop_id"] == "upload_button.n_clicks":
                return False, True, True, u.uos.df_to_b64(u.dfs.fix_df_trans(df))

            # If button not pressed return old data
            return False, True, False, df_old

        @app.callback(
            Output("upload_error_message", "children"),
            [Input("upload_container", "contents"), Input("upload_container", "filename")],
        )
        # pylint: disable=unused-variable
        def update_error_message(contents, filename):
            """
                Shows or deletes the rror message

                Args:
                    contents:   file uploaded
                    filename:   name of the file uploaded
            """
            out = u.uos.parse_dataframe_uploaded(contents, filename)

            if isinstance(out, str):
                return out

            return False

    def get_body(self):
        return [
            html.Div(
                [
                    # Upload widget
                    lay.card(
                        dcc.Upload(
                            children=html.Div(["Drag and Drop or ", html.A("Select a File")]),
                            style=c.styles.STYLE_UPLOAD_CONTAINER,
                            id="upload_container",
                        )
                    ),
                    # Error message
                    dbc.Collapse(
                        lay.card(html.Div(id="upload_error_message"), color="danger"),
                        id="upload_colapse_error_message",
                        is_open=False,
                    ),
                    # Success message
                    dbc.Collapse(
                        lay.card(html.Div(c.io.CONTENT_UPDATED), color="success"),
                        id="upload_colapse_success_message",
                        is_open=False,
                    ),
                    # Table preview and upload button
                    dbc.Collapse(
                        lay.card(
                            [
                                lay.two_columns(
                                    [
                                        html.H4(f"Previewing first {self.rows_preview} rows"),
                                        dbc.Button("Use this file", id="upload_button"),
                                    ]
                                ),
                                html.Div(
                                    dt.DataTable(id="upload_table_preview", **self.style_table),
                                    style=c.styles.STYLE_INSTRUCTIONS,
                                ),
                            ]
                        ),
                        id="upload_colapse_preview",
                        is_open=False,
                    ),
                    # Instruccions
                    lay.card(
                        html.Div(
                            [
                                dcc.Markdown(c.upload.INSTRUCTIONS_1),
                                html.Div(
                                    dt.DataTable(
                                        columns=[
                                            {"name": i, "id": i} for i in u.dfs.DF_SAMPLE.columns
                                        ],
                                        data=u.dfs.DF_SAMPLE.head(5).to_dict("rows"),
                                        **self.style_table,
                                    ),
                                    style=c.styles.STYLE_TABLE,
                                ),
                                dcc.Markdown(c.upload.INSTRUCTIONS_2),
                            ],
                            style=c.styles.STYLE_INSTRUCTIONS,
                        )
                    ),
                ]
            ),
            html.Div(id="upload_results"),
        ]
