"""
	Individual plots
"""

import plotly.graph_objs as go

import constants as c


def table_transactions(dfg, name, n_rows=50):
    """
        Creates a table with transactions

        Args:
            dfg:        dataframe to use

        Returns:
            the plotly plot as html-div format
    """

    if (dfg is None) or (dfg.shape[0] == 0):
        return {}

    n_rows = min(dfg.shape[0], n_rows)

    header = {
        "values": dfg.columns,
        "fill": {"color": c.colors.TABLE_HEADER_FILL},
    }
    cells = {"values": dfg.head(n_rows).transpose().values}

    data = go.Table(header=header, cells=cells)

    title = "{} preview (showing {} of {} rows)".format(name, n_rows, dfg.shape[0])
    layout = go.Layout(title=title, height=300 + 10*n_rows)

    return {"data": [data], "layout": layout}
