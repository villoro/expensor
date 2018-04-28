"""
    Dash app
"""

import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import utilities as u
import constants as c
from static import styles
from app import ui_utils as uiu
from plots import plots_upload as plots


LINK = c.dash.LINK_UPLOAD


def get_content(app, mdata):
    """
        Creates the page

        Args:
            app:        dash app
            mdata:      data helper class, used for retriving dataframes

        Returns:
            content:    body of the page
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
        html.Div(id="upload_results")
    ]

    @app.callback(Output("upload_results", "children"),
                  [Input("upload_container", "contents"),
                   Input("upload_container", "filename")])
    #pylint: disable=unused-variable
    def update_df_trans(contents, filename):
        """
            Updates the transaction dataframe

            Args:
                contents:   file uploaded
                filename:   name of the file uploaded
        """

        if (contents is None) or (filename is None):
            return []

        df = u.uos.parse_dataframe_uploaded(contents, filename)

        # If there has been a reading error, df would be an error message
        if isinstance(df, str):
            return df

        return dcc.Graph(
            id="upload_plot_trans", config=uiu.PLOT_CONFIG,
            figure=plots.table_transactions(df)
        )

    return content, None
