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

LANDING_APP = LINK_UPLOAD

NUM_DICT = {
    1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six",
    7: "seven", 8: "eight", 9: "nine", 10: "ten", 11: "eleven", 12: "twelve"
}

LINKS_ALL = [
    LINK_UPLOAD, LINK_EVOLUTION, LINK_COMPARISON, LINK_PIES, LINK_HEATMAPS
]

DICT_APPS = {"{}. {}".format(i + 1, x[1:].title()): x for i, x in enumerate(LINKS_ALL)}

CONTENT = "content"
SIDEBAR = "sidebar"
DUMMY_DIV = "dummy_div"

KEY_BODY = "body"
KEY_SIDEBAR = "sidebar"
