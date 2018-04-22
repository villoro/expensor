"""
    Folder for all dash pages
"""

from app.pages import app_evolution
from app.pages import app_comparison
from app.pages import app_heatmaps
from app.pages import app_violins
from app.pages import app_pies

import constants as c

ALL_APPS = {
    c.dash.LINK_EVOLUTION: app_evolution,
    c.dash.LINK_COMPARISON: app_comparison,
    c.dash.LINK_HEATMAPS: app_heatmaps,
    c.dash.LINK_VIOLINS: app_violins,
    c.dash.LINK_PIES: app_pies,
}

# Add an app for root path
ALL_APPS[c.dash.LINK_MAIN] = app_evolution
