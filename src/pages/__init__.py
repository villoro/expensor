"""
    Folder for all dash pages
"""

import os
import importlib

import constants as c


def get_pages(app):
    """
        Creates all dash pages

        Args:
            app:        dash app

        Returns:
            dict with pages
    """

    output = {}
    for page_name in os.listdir("src/pages"):

        # Check if it is a page
        if (page_name.startswith("page")) and (page_name.endswith(".py")):

            # Fix app name
            page_name = ".{}".format(page_name.split(".")[0])

            # Import it programatically
            m_page = importlib.import_module(page_name, "pages").Page(app)

            # Add content to the output dict
            output[m_page.link] = m_page

    # Clone content of the page that will appear in the root path
    output[c.dash.LINK_MAIN] = output[c.dash.LANDING_APP]

    return output
