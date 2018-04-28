"""
	Individual plots
"""

import plotly.graph_objs as go

import constants as c


def table_transactions(dfg, n_rows=50):
    """
        Creates a table with transactions

        Args:
            dfg:        dataframe to use

        Returns:
            the plotly plot as html-div format
    """

    if (dfg is None) or (dfg.shape[0] == 0):
        return {}

    header = {
        "values": dfg.columns,
        "fill": {"color": c.colors.TABLE_HEADER_FILL},
    }
    cells = {"values": dfg.head(n_rows).transpose().values}

    data = go.Table(header=header, cells=cells)

    title = "Data preview (showing {} of {} rows)".format(n_rows, dfg.shape[0])
    layout = go.Layout(title=title, height=800)

    return {"data": [data], "layout": layout}
