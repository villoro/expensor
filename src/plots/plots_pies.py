"""
	Individual plots
"""

import plotly.graph_objs as go

import utilities as u
import constants as c

def get_pie(dfg, type_trans, years=None):
    """
        Creates a pie with expenses or incomes

        Args:
            dfg:        dataframe to use
            type_trans: type of transaction [Income/Expense]

        Returns:
            the plotly plot as html-div format
    """

    df = u.dfs.filter_data(dfg, years, c.cols.YEAR)
    df = df[df[c.cols.TYPE] == type_trans]

    df = df.groupby(c.cols.CATEGORY).sum()

    data = go.Pie(values=df[c.cols.AMOUNT], labels=df.index)

    layout = go.Layout(title="{} distribution".format(type_trans))
    return go.Figure(data=[data], layout=layout)
