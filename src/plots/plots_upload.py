"""
	Individual plots
"""

import plotly.graph_objs as go


def table_transactions(dfg, n_rows=100):
    """
        Creates a table with transactions

        Args:
            dfg:        dataframe to use

        Returns:
            the plotly plot as html-div format
    """

    if dfg.shape[0] == 0:
        return {}

    data = go.Table(cells={"values": dfg.head(n_rows).transpose().values})
    return {"data": [data]}
