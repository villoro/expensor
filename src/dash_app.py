"""
    Dash app
"""
import os
import pandas as pd
from flask import send_from_directory
from dash import Dash

from app import layout
import constants as c
import utilities as u


def create_dash_app():
    """
        Creates the dash app and gets the related data
    """

    app = Dash()
    app.config.supress_callback_exceptions = True
    app.css.config.serve_locally = True

    # Load sample data
    df_trans = pd.read_csv(c.os.FILE_DATA_SAMPLE, sep=";", index_col=0)
    df_trans = u.dfs.fix_df_trans(df_trans)
    categories = df_trans[c.cols.CATEGORY].unique().tolist()

    app.layout = layout.get_layout(df_trans, categories)


    @app.server.route('/static/<path:path>')
    #pylint: disable=unused-variable
    def static_file(path):
        """Adds local css to dash """
        static_folder = os.path.join(os.getcwd(), 'static')
        return send_from_directory(static_folder, path)

    return app
