"""
    Styles for dash
"""

HEIGHT_HEADER = 75
HEIGHT_FILTERS = 0
WIDTH_SIDEBAR = 350
PADDING_V = 10
PADDING_H = 15

style_header = {
    "background-color": "#2196F3", # Blue 500
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

style_sidebar = {
    "background-color": "#FAFAFA", # Grey 50
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
    "overflow-y": "scroll"
}

style_filters_container = {
    "top": HEIGHT_HEADER,
    "left": WIDTH_SIDEBAR,
    "height": "{}px".format(HEIGHT_FILTERS),
    "width": "100%",
    "position": "fixed",
    "overflow": "hidden",
}

style_body = {
    "top": HEIGHT_HEADER + HEIGHT_FILTERS,
    "left": WIDTH_SIDEBAR,
    "right": 0,
    "bottom": 0,
    "position": "fixed",
    "padding": 0,
    "overflow-y": "scroll"
}

style_sidebar_elem = {
    "padding-bottom": "15px",
    "border-bottom": "1px solid #E0E0E0" # Grey 300
}