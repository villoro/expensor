"""
    Dash app
"""

import pandas as pd
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State, Event

import constants as c
import utilities as u
from app import ui_utils as uiu
from plots import plots_upload as plots


LINK = c.dash.LINK_UPLOAD

STYLE_PADDING_VERTICAL = {"margin-top": "{}px".format(c.styles.PADDING_V)}

DICT_SHOW = {
    True: STYLE_PADDING_VERTICAL,
    False: c.styles.STYLE_HIDDEN,
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
                style=c.styles.STYLE_UPLOAD_CONTAINER,
                id="upload_container"
            ),
            html.Button('Use this file', id='upload_button', style=STYLE_PADDING_VERTICAL),
        ]),
        html.Div(id="upload_results", style=DICT_SHOW[True])
    ]

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

            dfs = {sheet: pd.read_excel(c.io.FILE_DATA_SAMPLE, sheet) for sheet in c.dfs.ALL}

            data = []
            for instruc, name in zip(c.upload.INSTRUCTIONS_ALL, c.dfs.ALL):
                data += [
                    dcc.Markdown(instruc),
                    dcc.Graph(
                        id="upload_plot_demo_{}".format(name), config=uiu.PLOT_CONFIG,
                        figure=plots.plot_table(dfs[name], name, n_rows=5, with_header=False)
                    )
                ]

            return html.Div(data, style=c.styles.STYLE_UPLOAD_INFO)

        # When data is updated, show the message
        if contents == c.io.CONTENT_UPDATED:
            return c.io.CONTENT_UPDATED

        out = []

        for name in c.dfs.ALL:
            df = u.uos.parse_dataframe_uploaded(contents, filename, name)

            # If there has been a reading error with any df, df would be an error message
            if isinstance(df, str):
                return df

            out.append(dcc.Graph(
                id="upload_plot_{}".format(name), config=uiu.PLOT_CONFIG,
                figure=plots.plot_table(df, name)
            ))

        # return a list with a plot for every df read
        return out


    def check_contents(contents, filename, df_name):
        """
            Check if contents are valid. If they are it returns the dataframe, else return None

            Args:
                contents:   contents uploaded
                filename:   name of the file updated
        """

        if (contents is None) or (filename is None) or (contents == c.io.CONTENT_UPDATED):
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
            Shows/hide the "use this file" button

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
            Clear the upadate container after data has been updated

            Args:
                contents:   file uploaded
                filename:   name of the file uploaded
        """

        result = True

        for name in c.dfs.ALL:
            result &= False if check_contents(contents, filename, name) is None else True

        return c.io.CONTENT_UPDATED if result is not None else None


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

        df = check_contents(contents, filename, c.dfs.CATEG)

        if df is None:
            return None

        return u.uos.df_to_b64(df)


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


    @app.callback(Output("global_df_liquid_list", "children"),
                  [],
                  [State("upload_container", "contents"),
                   State('upload_container', 'filename')],
                  [Event("upload_button", "click")])
    #pylint: disable=unused-variable
    def update_df_liquid_list(contents, filename):
        """
            Updates the liquid list dataframe

            Args:
                contents:   file uploaded
                filename:   name of the file uploaded
        """

        df = check_contents(contents, filename, c.dfs.LIQUID_LIST)

        if df is None:
            return None

        return u.uos.df_to_b64(df)


    @app.callback(Output("global_df_liquid", "children"),
                  [],
                  [State("upload_container", "contents"),
                   State('upload_container', 'filename')],
                  [Event("upload_button", "click")])
    #pylint: disable=unused-variable
    def update_df_liquid(contents, filename):
        """
            Updates the liquid dataframe

            Args:
                contents:   file uploaded
                filename:   name of the file uploaded
        """

        df = check_contents(contents, filename, c.dfs.LIQUID)

        if df is None:
            return None

        # Add total column
        if c.names.TOTAL in df.columns:
            del df[c.names.TOTAL]

        df[c.names.TOTAL] = df.sum(axis=1)

        return u.uos.df_to_b64(df)


    return {c.dash.KEY_BODY: content}
