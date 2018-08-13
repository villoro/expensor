"""
    Dash app
"""

import pandas as pd
from dash import Dash

from app import layout
import constants as c
import utilities as u


def create_dash_app():
    """
        Creates the dash app and gets the related data
    """

    app = Dash("auth")
    app.config.supress_callback_exceptions = True

    # Load sample data
    dfs = {sheet: pd.read_excel(c.io.FILE_DATA_SAMPLE, sheet) for sheet in c.dfs.ALL}

    # Fix transactions
    dfs[c.dfs.TRANS] = u.dfs.fix_df_trans(dfs[c.dfs.TRANS])

    # Transformt to b64 in order to store data
    dfs = {sheet: u.uos.df_to_b64(df) for sheet, df in dfs.items()}

    app.title = c.names.TITLE
    app.layout = layout.get_layout(dfs)

    return app
