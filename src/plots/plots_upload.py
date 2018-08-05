"""
	Individual plots
"""

import plotly.graph_objs as go

import constants as c


def plot_table(dfg, name, n_rows=50, header=False):
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

    if not header:
        title = "{} preview (showing {} of {} rows)".format(name, n_rows, dfg.shape[0])
        layout = go.Layout(title=title, height=300 + 10*n_rows)

    else:
        layout = go.Layout(height=150,
                           margin=go.Margin(l=0, r=0, b=0, t=0))

    return {"data": [data], "layout": layout}
