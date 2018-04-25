"""
    Folder for all dash pages
"""

import os

import utilities as u
import constants as c

from app import ui_utils as uiu


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

    exec("from app.pages import app_evolution")

    dfg = u.uos.get_df(c.os.FILE_DATA_SAMPLE)
    categories = dfg[c.cols.CATEGORY].unique().tolist()

    output = {}
    for app_name in os.listdir("app/pages"):

        # Check if it is an app
        if (app_name.startswith("app")) and (app_name.endswith(".py")):
            
            # Fix app name
            app_name = app_name.split(".")[0]

            # Import it programatically and retrive it from globals
            exec("from app.pages import {}".format(app_name))
            m_app = globals()[app_name]

            # Add content to the output dict
            content_raw, sidebar_raw = m_app.get_content(app, dfg, categories)

            content = uiu.create_body(content_raw)
            sidebar = uiu.create_sidebar(categories, sidebar_raw)

            output[m_app.LINK] = {c.dash.CONTENT: content, c.dash.SIDEBAR: sidebar}

    output[c.dash.LINK_MAIN] = output[c.dash.LANDING_APP]

    return output
