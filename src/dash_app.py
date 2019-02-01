"""
    Dash app
"""

import pandas as pd
from dash import Dash

import layout
import constants as c
import utilities as u


def create_dash_app():
    """
        Creates the dash app and gets the related data
    """

    app = Dash("auth")
    app.config.supress_callback_exceptions = True

    # Load, fix and transform to b64 the transactions dataframe
    df = u.dfs.fix_df_trans(pd.read_excel(c.io.FILE_DATA_SAMPLE))

    app.title = c.names.TITLE
    app.layout = layout.get_layout(df)

    return app, df
