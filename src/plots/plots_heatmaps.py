"""
	Individual plots
"""

import plotly.graph_objs as go

import constants as c
import utilities as u


def get_heatmap(dfg, type_trans):
    """
        Creates a heatmap with expenses or incomes

        Args:
            dfg:        dataframe to use
            type_trans: type of transaction [Income/Expense]

        Returns:
            the plotly plot as html-div format
    """

    df = u.dfs.group_df_by(dfg[dfg[c.cols.TYPE] == type_trans], "M")

    # No data no fun
    if df.shape[0] < 2:
        return None

    df[c.cols.YEAR], df[c.cols.MONTH] = df.index.year, df.index.month

    df = df.pivot(c.cols.MONTH, c.cols.YEAR, c.cols.AMOUNT).copy()

    cmap = {c.names.INCOMES: "Greens", c.names.EXPENSES: "YIOrRd"}[type_trans]

    data = go.Heatmap(x=df.columns, y=df.index, z=df.values,
                      colorscale=cmap, reversescale=True, showscale=False)

    layout = go.Layout(title="Heatmap ({})".format(type_trans))
    return go.Figure(data=[data], layout=layout)
