"""
    Dash app
"""

import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State, Event

import utilities as u
import constants as c
from static import styles
from app import ui_utils as uiu
from plots import plots_upload as plots


LINK = c.dash.LINK_UPLOAD

CONTENT_UPDATED = "File has been updated"

DICT_SHOW = {
    True: {},
    False: styles.STYLE_HIDDEN,
}


def get_content(app, dfg, categories):
    """
        Creates the page

        Args:
            app:        dash app
            mdata:      data helper class, used for retriving dataframes

        Returns:
            dict with content:
                body:       body of the page
                sidebar:    content of the sidebar
    """

    content = [
        dcc.Upload(
            children=html.Div([
                'Drag and Drop or ',
                html.A('Select a File')
            ]),
            style=styles.STYLE_UPLOAD_CONTAINER,
            id="upload_container"
        ),
        html.Div([
            html.Div(id="upload_results"),
            html.Button('Use this file', id='upload_button', style=DICT_SHOW[False]),
        ])
    ]

    @app.callback(Output("upload_results", "children"),
                  [Input("upload_container", "contents"),
                   Input("upload_container", "filename")])
    #pylint: disable=unused-variable
    def show_df_trans(contents, filename):
        """
            Updates the transaction dataframe

            Args:
                contents:   file uploaded
                filename:   name of the file uploaded
        """

        if (contents is None) or (filename is None):
            return []

        if contents == CONTENT_UPDATED:
            return CONTENT_UPDATED

        df = u.uos.parse_dataframe_uploaded(contents, filename)

        # If there has been a reading error, df would be an error message
        if isinstance(df, str):
            return df

        return dcc.Graph(
            id="upload_plot_trans", config=uiu.PLOT_CONFIG,
            figure=plots.table_transactions(df)
        )


    def check_contents(contents, filename):
        """
            Check if contents are valid. If they are it returns the dataframe, else return None

            Args:
                contents:   contents uploaded
                filename:   name of the file updated
        """

        if (contents is None) or (filename is None) or (contents == CONTENT_UPDATED):
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
            Updates the transaction dataframe

            Args:
                contents:   file uploaded
                filename:   name of the file uploaded
        """

        result = check_contents(contents, filename)
        return DICT_SHOW[False if result is None else True]


    @app.callback(Output("upload_container", "contents"),
                  [],
                  [State("upload_container", "contents"),
                   State('upload_container', 'filename')],
                  [Event("upload_button", "click")])
    #pylint: disable=unused-variable
    def clear_table_when_data_updated(contents, filename):
        """
            Updates the transaction dataframe

            Args:
                contents:   file uploaded
                filename:   name of the file uploaded
        """

        result = check_contents(contents, filename)
        return CONTENT_UPDATED if result is not None else None


    @app.callback(Output("global_df_trans", "children"),
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

        result = check_contents(contents, filename)
        return u.uos.df_to_b64(result) if result is not None else None


    return {c.dash.KEY_BODY: content, c.dash.KEY_INCLUDE_CATEGORIES_IN_SIDEBAR: False}
