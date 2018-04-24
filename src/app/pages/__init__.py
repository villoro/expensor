"""
    Folder for all dash pages
"""

from app.pages import app_evolution
from app.pages import app_comparison
from app.pages import app_heatmaps
from app.pages import app_violins
from app.pages import app_pies

import constants as c

# ALL_APPS = {
#     # c.dash.LINK_EVOLUTION: app_evolution,
#     # c.dash.LINK_COMPARISON: app_comparison,
#     # c.dash.LINK_HEATMAPS: app_heatmaps,
#     # c.dash.LINK_VIOLINS: app_violins,
#     # c.dash.LINK_PIES: app_pies,
# }

# Add an app for root path
# ALL_APPS[c.dash.LINK_MAIN] = app_evolution


def get_pages(app, dfg, pages):
    """
        Creates all dash pages

        Args:
            app:        dash app
            dfg:        dataframe with all data
            categories: list of categories avaiables

        Returns:
            Pages as a json with the next structure

            --page_link_1
                --conent
                --sidebar

            --page_link_n
                --content
                --sidebar
    """

    from app.pages import app_comparison as mapp

    output = {}
    for mapp in [app_evolution, app_comparison, app_heatmaps, app_violins, app_pies]:
        content, sidebar = mapp.get_content(app, dfg, pages)
        output[mapp.LINK] = {c.dash.CONTENT: content, c.dash.SIDEBAR: sidebar}

    output[c.dash.LINK_MAIN] = output[c.dash.LANDING_APP]

    return output
