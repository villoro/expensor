"""
    Styles for dash
"""

HEIGHT_HEADER = 75
HEIGHT_FILTERS = 0
WIDTH_SIDEBAR = 200
PADDING_TOP = 10
PADDING_LEFT = 15

style_header = {
    "background-color": "#03A9F4",
    "top": 0,
    "left": 0,
    "height": "{}px".format(HEIGHT_HEADER - PADDING_TOP),
    "width": "100%",
    "position": "fixed",
    "overflow": "hidden",
    "margin": "0px",
    "padding-top": "{}px".format(PADDING_TOP),
    "padding-left": "{}px".format(PADDING_LEFT),
    "z-index": "9999"
}

style_sidebar = {
    "background-color": "#EEEEEE",
    "top": HEIGHT_HEADER,
    "left": 0,
    "height": "100%",
    "width": "{}px".format(WIDTH_SIDEBAR - PADDING_LEFT),
    "position": "fixed",
    "overflow": "hidden",
    "padding-top": "{}px".format(PADDING_TOP),
    "padding-left": "{}px".format(PADDING_LEFT),
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