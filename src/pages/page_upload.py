"""
    Dash app
"""

import pandas as pd
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State, Event

import constants as c
import utilities as u
import layout as lay
from plots import plots_upload as plots


STYLE_PADDING_VERTICAL = {"margin-top": "{}px".format(c.styles.PADDING_V)}

DICT_SHOW = {
    True: STYLE_PADDING_VERTICAL,
    False: c.styles.STYLE_HIDDEN,
}

class Page(lay.AppPage):
    """ Page Evolution """

    link = c.dash.LINK_UPLOAD
    def_type = c.names.EXPENSES
    def_tw = "M"


    def __init__(self, app):
        super().__init__([
            c.dash.INPUT_CATEGORIES,
            c.dash.INPUT_SMOOTHING,
            c.dash.INPUT_TIMEWINDOW
        ])

        @app.callback(Output("upload_results", "children"),
                      [Input("upload_container", "contents"),
                       Input("upload_container", "filename")])
        #pylint: disable=unused-variable,unused-argument
        def get_table(contents, filename):
            """
                Updates the transaction dataframe

                Args:
                    contents:   file uploaded
                    filename:   name of the file uploaded
                    plot_id:    id of the returning plot
            """
            # When there is no data, show tutorial
            if (contents is None) or (filename is None):

                df = pd.read_excel(c.io.FILE_DATA_SAMPLE)

                data = [
                    dcc.Markdown(c.upload.INSTRUCTIONS_1),
                    dcc.Graph(
                        id="upload_plot_demo", config=c.dash.PLOT_CONFIG,
                        figure=plots.plot_table(df, n_rows=5, with_header=False)
                    ),
                    dcc.Markdown(c.upload.INSTRUCTIONS_2)
                ]

                return html.Div(data, style=c.styles.STYLE_UPLOAD_INFO)

            # When data is updated, show the message
            if contents == c.io.CONTENT_UPDATED:
                return c.io.CONTENT_UPDATED


            df = u.uos.parse_dataframe_uploaded(contents, filename)

            # If there has been a reading error with any df, df would be an error message
            if isinstance(df, str):
                return df

            # Return the plot
            return dcc.Graph(
                id="upload_plot", config=c.dash.PLOT_CONFIG,
                figure=plots.plot_table(df)
            )


        def check_contents(contents, filename):
            """
                Check if contents are valid. If they are it returns the dataframe, else return None

                Args:
                    contents:   contents uploaded
                    filename:   name of the file updated
            """

            if (contents is None) or (filename is None) or (contents == c.io.CONTENT_UPDATED):
                return None

            df = u.uos.parse_dataframe_uploaded(contents, filename)

            # If there has been a reading error, df would be an error message
            if isinstance(df, str):
                return None

            return df


        @app.callback(Output("upload_button", "style"),
                      [Input("upload_container", "contents"),
                       Input("upload_container", "filename")])
        #pylint: disable=unused-variable
        def allow_update(contents, filename):
            """
                Shows/hide the "use this file" button

                Args:
                    contents:   file uploaded
                    filename:   name of the file uploaded
            """
            return DICT_SHOW[check_contents(contents, filename) is not None]


        @app.callback(Output("upload_container", "contents"),
                      [],
                      [State("upload_container", "contents"),
                       State('upload_container', 'filename')],
                      [Event("upload_button", "click")])
        #pylint: disable=unused-variable
        def clear_table_when_data_updated(contents, filename):
            """
                Clear the upadate container after data has been updated

                Args:
                    contents:   file uploaded
                    filename:   name of the file uploaded
            """
            return c.io.CONTENT_UPDATED if check_contents(contents, filename) is not None else None


        @app.callback(Output("global_df", "children"),
                      [],
                      [State("upload_container", "contents"),
                       State('upload_container', 'filename')],
                      [Event("upload_button", "click")])
        #pylint: disable=unused-variable
        def update_df_trans(contents, filename):
            """
                Updates the transaction dataframe

                Args:
                    contents:   file uploaded
                    filename:   name of the file uploaded
            """

            df = check_contents(contents, filename)

            if df is None:
                return None

            return u.uos.df_to_b64(u.dfs.fix_df_trans(df))

    def get_body(self):
        return [
            html.Div([
                dcc.Upload(
                    children=html.Div([
                        'Drag and Drop or ',
                        html.A('Select a File')
                    ]),
                    style=c.styles.STYLE_UPLOAD_CONTAINER,
                    id="upload_container"
                ),
                html.Button('Use this file', id='upload_button', style=STYLE_PADDING_VERTICAL),
            ]),
            html.Div(id="upload_results", style=DICT_SHOW[True])
        ]
