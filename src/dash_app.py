"""
    Dash app
"""

import pandas as pd
from dash import Dash

from static.styles import STYLE_URL
from app import layout
import constants as c
import utilities as u


def create_dash_app():
    """
        Creates the dash app and gets the related data
    """

    app = Dash()
    app.config.supress_callback_exceptions = True

    # Load sample data
    dfs = {sheet: pd.read_excel(c.os.FILE_DATA_SAMPLE, sheet) for sheet in c.dfs.ALL}

    # Fix trans and get categories
    dfs[c.dfs.TRANS] = u.dfs.fix_df_trans(dfs[c.dfs.TRANS])
    categories = dfs[c.dfs.TRANS][c.cols.CATEGORY].unique().tolist()

    # Transformt to b64 in order to store data
    dfs = {sheet: u.uos.df_to_b64(df) for sheet, df in dfs.items()}

    app.layout = layout.get_layout(dfs, categories)
    app.css.append_css({'external_url': STYLE_URL})

    return app
