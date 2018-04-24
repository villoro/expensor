"""
    Folder for all dash pages
"""

from app.pages import app_evolution
from app.pages import app_comparison
from app.pages import app_heatmaps
from app.pages import app_violins
from app.pages import app_pies

import utilities as u
import constants as c


def get_pages(app):
    """
        Creates all dash pages

        Args:
            app:        dash app

        Returns:
            Pages as a json with the next structure

            --page_link_1
                --conent
                --sidebar

            --page_link_n
                --content
                --sidebar
    """

    dfg = u.uos.get_df(c.os.FILE_DATA_SAMPLE)
    categories = dfg[c.cols.CATEGORY].unique().tolist()

    output = {}
    for mapp in [app_evolution, app_comparison, app_heatmaps, app_violins, app_pies]:
        content, sidebar = mapp.get_content(app, dfg, categories)
        output[mapp.LINK] = {c.dash.CONTENT: content, c.dash.SIDEBAR: sidebar}

    output[c.dash.LINK_MAIN] = output[c.dash.LANDING_APP]

    return output
