"""
    Styles for dash
"""

from utilities.upalette import get_colors

STYLE_URL = "https://raw.githubusercontent.com/villoro/expensor/master/src/static/styles.css"

HEIGHT_HEADER = 75
HEIGHT_FILTERS = 0
WIDTH_SIDEBAR = 350
PADDING_V = 10
PADDING_H = 15

COLOR_HEADER = get_colors(("blue", 500))
COLOR_SIDEBAR, COLOR_SIDEBAR_SEP = get_colors([("grey", 200), ("grey", 400)])

STYLE_HEADER = {
    "background-color": COLOR_HEADER,
    "top": 0,
    "left": 0,
    "height": "{}px".format(HEIGHT_HEADER - PADDING_V),
    "width": "100%",
    "position": "fixed",
    "overflow": "hidden",
    "margin": "0px",
    "padding-top": "{}px".format(PADDING_V),
    "padding-left": "{}px".format(PADDING_H),
    "z-index": "9999"
}

STYLE_SIDEBAR = {
    "background-color": COLOR_SIDEBAR,
    "top": HEIGHT_HEADER,
    "left": 0,
    "height": "100%",
    "width": "{}px".format(WIDTH_SIDEBAR - 2*PADDING_H),
    "position": "fixed",
    "overflow": "hidden",
    "padding-top": "{}px".format(PADDING_V),
    "padding-bottom": "{}px".format(PADDING_V),
    "padding-left": "{}px".format(PADDING_H),
    "padding-right": "{}px".format(PADDING_H),
}

STYLE_FILTER_DIV = {
    "top": HEIGHT_HEADER,
    "left": WIDTH_SIDEBAR,
    "height": "{}px".format(HEIGHT_FILTERS),
    "width": "100%",
    "position": "fixed",
    "overflow": "hidden",
}

STYLE_BODY = {
    "top": HEIGHT_HEADER + HEIGHT_FILTERS,
    "left": WIDTH_SIDEBAR,
    "right": 0,
    "bottom": 0,
    "position": "fixed",
    "padding": 0,
    "overflow-y": "scroll"
}

STYLE_SIDEBAR_ELEM = {
    "padding-bottom": "15px",
    "border-bottom": "1px solid {}".format(COLOR_SIDEBAR_SEP)
}

STYLE_DIV_CONTROL_IN_BODY = {
    "text-align": "center",
    "padding-bottom": "15px",
    "border-bottom": "2px solid {}".format(COLOR_SIDEBAR)
}

STYLE_UPLOAD_CONTAINER = {
    "height": "60px",
    "lineHeight": "60px",
    "borderWidth": "1px",
    "borderStyle": "dashed",
    "borderRadius": "5px",
    "textAlign": "center",
    "margin-top": "{}px".format(PADDING_V),
    "margin-left": "{}px".format(PADDING_H),
    "margin-right": "{}px".format(PADDING_H),
}

STYLE_HIDDEN = {"display":"none"}
