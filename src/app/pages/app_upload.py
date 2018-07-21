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

STYLE_PADDING_VERTICAL = {"margin-top": "{}px".format(styles.PADDING_V)}

DICT_SHOW = {
    True: STYLE_PADDING_VERTICAL,
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
            html.Button('Use this file', id='upload_button', style=STYLE_PADDING_VERTICAL),
        ]),
        html.Div(id="upload_results", style=DICT_SHOW[True])
    ]


    @app.callback(Output("upload_results", "children"),
                  [Input("upload_container", "contents"),
                   Input("upload_container", "filename")])
    def get_table(contents, filename):
        """
            Updates the transaction dataframe

            Args:
                contents:   file uploaded
                filename:   name of the file uploaded
                plot_id:    id of the returning plot
        """
        if (contents is None) or (filename is None):
            return html.Img(src=u.uos.get_image(c.os.IMAGE_UPLOAD_TUTORIAL))

        if contents == c.os.CONTENT_UPDATED:
            return c.os.CONTENT_UPDATED

        out = []

        for name in c.dfs.ALL:
            df = u.uos.parse_dataframe_uploaded(contents, filename, name)

            # If there has been a reading error, df would be an error message
            if isinstance(df, str):
                return df

            out.append(dcc.Graph(
                id="upload_plot_{}".format(name), config=uiu.PLOT_CONFIG,
                figure=plots.table_transactions(df, name)
            ))

        return out


    def check_contents(contents, filename, df_name):
        """
            Check if contents are valid. If they are it returns the dataframe, else return None

            Args:
                contents:   contents uploaded
                filename:   name of the file updated
        """

        if (contents is None) or (filename is None) or (contents == c.os.CONTENT_UPDATED):
            return None

        df = u.uos.parse_dataframe_uploaded(contents, filename, df_name)

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

        result = True

        for name in c.dfs.ALL:
            result &= False if check_contents(contents, filename, name) is None else True

        return DICT_SHOW[result]


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

        result = True

        for name in c.dfs.ALL:
            result &= False if check_contents(contents, filename, name) is None else True

        return c.os.CONTENT_UPDATED if result is not None else None


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

        df = check_contents(contents, filename, c.dfs.TRANS)

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

        df = check_contents(contents, filename, c.dfs.TRANS)

        if df is None:
            return None

        df = u.dfs.fix_df_trans(df)
        return df[c.cols.CATEGORY].unique().tolist()


    return {c.dash.KEY_BODY: content}
