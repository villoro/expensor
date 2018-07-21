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
    df_trans = pd.read_csv(c.os.FILE_DATA_SAMPLE, sep=";", index_col=0)
    df_trans = u.dfs.fix_df_trans(df_trans)
    categories = df_trans[c.cols.CATEGORY].unique().tolist()

    app.layout = layout.get_layout(df_trans, categories)
    app.css.append_css({'external_url': STYLE_URL})

    return app
