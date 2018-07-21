"""
    Dash app
"""

import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State, Event

import constants as c
import utilities as u
from static import styles
from app import ui_utils as uiu
from plots import plots_upload as plots


LINK = c.dash.LINK_UPLOAD

CONTENT_UPDATED = "File has been updated"

DICT_SHOW = {
    True: {},
    False: styles.STYLE_HIDDEN,
}


def get_content(app):
    """
        Creates the page

        Args:
            app:        dash app

        Returns:
            dict with content:
                body:       body of the page
                sidebar:    content of the sidebar
    """

    content = [
        html.Div([
            dcc.Upload(
                children=html.Div([
                    'Drag and Drop or ',
                    html.A('Select a File')
                ]),
                style=styles.STYLE_UPLOAD_CONTAINER,
                id="upload_container"
            ),
            html.Button('Use this file', id='upload_button', style=DICT_SHOW[False]),
        ]),
        html.Div([
            html.Div(id="upload_results_liquid_list"),
            html.Div(id="upload_results_liquid"),
            html.Div(id="upload_results_trans"),
        ])
    ]

    def get_table(contents, filename, df_name, plot_id):
        """
            Updates the transaction dataframe

            Args:
                contents:   file uploaded
                filename:   name of the file uploaded
                plot_id:    id of the returning plot
        """
        if (contents is None) or (filename is None):
            return []

        if contents == CONTENT_UPDATED:
            return CONTENT_UPDATED

        df = u.uos.parse_dataframe_uploaded(contents, filename, df_name)

        # If there has been a reading error, df would be an error message
        if isinstance(df, str):
            return df

        return dcc.Graph(
            id=plot_id, config=uiu.PLOT_CONFIG,
            figure=plots.table_transactions(df, df_name)
        )

    @app.callback(Output("upload_results_trans", "children"),
                  [Input("upload_container", "contents"),
                   Input("upload_container", "filename")])
    #pylint: disable=unused-variable
    def show_df_trans(contents, filename):
        """ Dummy function to show df trans """

        return get_table(contents, filename, c.dfs.TRANS, "upload_plot_trans")


    @app.callback(Output("upload_results_liquid", "children"),
                  [Input("upload_container", "contents"),
                   Input("upload_container", "filename")])
    #pylint: disable=unused-variable
    def show_df_liquid(contents, filename):
        """ Dummy function to show df liquid """

        return get_table(contents, filename, c.dfs.LIQUID, "upload_plot_liquid")


    @app.callback(Output("upload_results_liquid_list", "children"),
                  [Input("upload_container", "contents"),
                   Input("upload_container", "filename")])
    #pylint: disable=unused-variable
    def show_df_liquid_list(contents, filename):
        """ Dummy function to show df liquid list """

        return get_table(contents, filename, c.dfs.LIQUID_LIST, "upload_plot_liquid_list")


    def check_contents(contents, filename):
        """
            Check if contents are valid. If they are it returns the dataframe, else return None

            Args:
                contents:   contents uploaded
                filename:   name of the file updated
        """

        if (contents is None) or (filename is None) or (contents == CONTENT_UPDATED):
            return None

        df = u.uos.parse_dataframe_uploaded(contents, filename, c.dfs.TRANS)

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

        df = check_contents(contents, filename)

        if df is None:
            return None

        df = u.dfs.fix_df_trans(df)
        return u.uos.df_to_b64(df)

    @app.callback(Output("global_categories", "children"),
                  [],
                  [State("upload_container", "contents"),
                   State('upload_container', 'filename')],
                  [Event("upload_button", "click")])
    #pylint: disable=unused-variable
    def update_categories(contents, filename):
        """
            Updates the list of categories

            Args:
                contents:   file uploaded
                filename:   name of the file uploaded
        """

        df = check_contents(contents, filename)

        if df is None:
            return None

        df = u.dfs.fix_df_trans(df)
        return df[c.cols.CATEGORY].unique().tolist()


    return {c.dash.KEY_BODY: content}
