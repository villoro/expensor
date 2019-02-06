"""
    OS related constants
"""

LINK_ROOT = "http://localhost:8050"

LINK_MAIN = "/"
LINK_UPLOAD = "/upload"
LINK_EVOLUTION = "/evolution"
LINK_COMPARISON = "/comparison"
LINK_HEATMAPS = "/heatmaps"
LINK_PIES = "/pies"

LINKS_ALL = [
    LINK_UPLOAD,
    LINK_EVOLUTION,
    LINK_COMPARISON,
    LINK_HEATMAPS,
    LINK_PIES,
]

LANDING_APP = LINK_UPLOAD

NUM_DICT = {
    1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six",
    7: "seven", 8: "eight", 9: "nine", 10: "ten", 11: "eleven", 12: "twelve"
}

INPUT_CATEGORIES = "categories"
INPUT_SMOOTHING = "smoothing"
INPUT_TIMEWINDOW = "timewindow"

DEFAULT_SMOOTHING = 3

PLOT_CONFIG = {
    "displaylogo": False,
    "modeBarButtonsToRemove": ["sendDataToCloud", "select2d", "lasso2d", "resetScale2d"]
}
