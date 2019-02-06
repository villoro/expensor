"""
    Dash app
"""

import pandas as pd
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State, Event

import constants as c
import utilities as u
import layout as lay
from plots import plots_upload as plots


class Page(lay.AppPage):
    """ Page Evolution """

    link = c.dash.LINK_UPLOAD
    def_type = c.names.EXPENSES
    def_tw = "M"


    def __init__(self, app):
        super().__init__([])


        @app.callback(Output("upload_plot_preview", "figure"),
                      [Input("upload_container", "contents"),
                       Input("upload_container", "filename")])
        #pylint: disable=unused-variable
        def update_plot_preview(contents, filename):
            """
                Shows or deletes the rror message

                Args:
                    contents:   file uploaded
                    filename:   name of the file uploaded
            """

            out = u.uos.parse_dataframe_uploaded(contents, filename)

            if isinstance(out, str):
                return {}

            # No error, preview plot
            return plots.plot_table(out)


        @app.callback(Output("upload_error_message", "children"),
                      [Input("upload_container", "contents"),
                       Input("upload_container", "filename")])
        #pylint: disable=unused-variable
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


        @app.callback(Output("upload_colapse_error_message", "is_open"),
                      [Input("upload_container", "contents"),
                       Input("upload_container", "filename")])
        #pylint: disable=unused-variable
        def show_error_message(contents, filename):
            """
                Shows/hide the error message

                Args:
                    error_text: text of error message
            """

            if isinstance(u.uos.parse_dataframe_uploaded(contents, filename), str):
                return True

            return False

        @app.callback(Output("upload_colapse_success_message", "is_open"),
                      [],
                      [],
                      [Event("upload_button", "click")])
        #pylint: disable=unused-variable
        def show_success_message():
            """
                Shows/hide the success message
            """

            return True


        @app.callback(Output("upload_colapse_preview", "is_open"),
                      [Input("upload_container", "contents"),
                       Input("upload_container", "filename")])
        #pylint: disable=unused-variable
        def show_preview(contents, filename):
            """
                Shows/hide the preview of the dataframe loaded

                Args:
                    contents:   file uploaded
                    filename:   name of the file uploaded
            """

            out = u.uos.parse_dataframe_uploaded(contents, filename)

            if isinstance(out, str) or out is None:
                return False

            return True


        @app.callback(Output("global_df", "children"),
                      [],
                      [State("upload_container", "contents"),
                       State("upload_container", "filename"),
                       State("upload_colapse_preview", "is_open")],
                      [Event("upload_button", "click")])
        #pylint: disable=unused-variable
        def update_df_trans(contents, filename, file_ok):
            """
                Updates the transaction dataframe

                Args:
                    contents:   file uploaded
                    filename:   name of the file uploaded
                    file_ok:    bool checking if file is uploadable
            """

            if not file_ok:
                return None

            df = u.uos.parse_dataframe_uploaded(contents, filename)

            return u.uos.df_to_b64(u.dfs.fix_df_trans(df))


    def get_body(self):
        return [
            html.Div([
                # Upload widget
                lay.card(
                    dcc.Upload(
                        children=html.Div([
                            'Drag and Drop or ',
                            html.A('Select a File')
                        ]),
                        style=c.styles.STYLE_UPLOAD_CONTAINER,
                        id="upload_container"
                    )
                ),
                # Error message
                dbc.Collapse(
                    lay.card(
                        html.Div(id="upload_error_message"),
                        color="danger"
                    ),
                    id="upload_colapse_error_message",
                    is_open=False,
                ),
                # Success message
                dbc.Collapse(
                    lay.card(
                        html.Div(c.io.CONTENT_UPDATED),
                        color="success"
                    ),
                    id="upload_colapse_success_message",
                    is_open=False,
                ),
                # Table preview and upload button
                dbc.Collapse(
                    lay.card(
                        [
                            html.Button('Use this file', id='upload_button'),
                            dcc.Graph(id="upload_plot_preview", config=c.dash.PLOT_CONFIG),
                        ],
                    ),
                    id="upload_colapse_preview",
                    is_open=False,
                ),
                # Instruccions
                lay.card(
                    html.Div(
                        [
                            dcc.Markdown(
                                c.upload.INSTRUCTIONS_1,
                            ),
                            dcc.Graph(
                                id="upload_plot_demo", config=c.dash.PLOT_CONFIG,
                                figure=plots.plot_table(
                                    u.dfs.DF_SAMPLE, n_rows=5, with_header=False
                                )
                            ),
                            dcc.Markdown(c.upload.INSTRUCTIONS_2)
                        ],
                        style=c.styles.STYLE_INSTRUCTIONS,
                    ),
                ),
            ]),
            html.Div(id="upload_results")
        ]
