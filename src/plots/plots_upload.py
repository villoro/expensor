"""
	Individual plots
"""

import plotly.graph_objs as go

import constants as c


def plot_table(dfg, n_rows=50, with_header=True):
    """
        Creates a table with transactions

        Args:
            dfg:            dataframe to use
            n_rows:         number of rows to show
            with_header:    display titles and use a big table

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

    if with_header:
        title = "Table preview (showing {} of {} rows)".format(n_rows, dfg.shape[0])
        layout = go.Layout(title=title, height=300 + 10*n_rows)

    else:
        layout = go.Layout(height=150,
                           margin=go.layout.Margin(l=0, r=0, b=0, t=0))

    return {"data": [data], "layout": layout}
