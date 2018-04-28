"""
    Folder for all dash pages
"""

import os
import importlib

import data_helper
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

    mdata = data_helper.Data()

    output = {}
    for app_name in os.listdir("app/pages"):

        # Check if it is an app
        if (app_name.startswith("app")) and (app_name.endswith(".py")):

            # Fix app name
            app_name = ".{}".format(app_name.split(".")[0])

            # Import it programatically
            m_app = importlib.import_module(app_name, "app.pages")

            # Retrive lists with content and sidebar
            content_raw, sidebar_raw = m_app.get_content(app, mdata)

            # Construct body and sidebar
            content = uiu.create_body(content_raw)
            sidebar = uiu.create_sidebar(mdata.categories, sidebar_raw)

            # Add content to the output dict
            output[m_app.LINK] = {c.dash.CONTENT: content, c.dash.SIDEBAR: sidebar}

    # Clone content of the page that will appear in the root path
    output[c.dash.LINK_MAIN] = output[c.dash.LANDING_APP]

    return output
