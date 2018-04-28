"""
    Some colors
"""

from utilities.upalette import get_colors

_COLORS = [("red", 500), ("green", 500), ("amber", 500), ("blue", 500)]

EXPENSES, INCOMES, EBIT, EBIT_CUM = get_colors(_COLORS)

TABLE_HEADER_FILL = get_colors(("light blue", 300))
