"""
	Individual plots
"""

from calendar import month_abbr # options: [month_name, month_abbr]
from plotly import figure_factory as FF
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

    df = df.pivot(c.cols.MONTH, c.cols.YEAR, c.cols.AMOUNT).sort_index(ascending=False)

    # Fix month names
    df.index = [month_abbr[x] for x in df.index]

    cmap = {c.names.INCOMES: "Greens", c.names.EXPENSES: "YIOrRd"}[type_trans]

    data = go.Heatmap(x=df.columns, y=df.index, z=df.values,
                      colorscale=cmap, reversescale=True, showscale=False)

    layout = go.Layout(title="Heatmap ({})".format(type_trans))
    return go.Figure(data=[data], layout=layout)


def dist_plot(dfg):
    """
        Creates a distribution plot with expenses, incomes and ebit

        Args:
            dfg:    dataframe to use

        Returns:
            the plotly plot as html-div format
    """

    dfe = u.dfs.group_df_by(dfg[dfg[c.cols.TYPE] == c.names.EXPENSES], "M")
    dfi = u.dfs.group_df_by(dfg[dfg[c.cols.TYPE] == c.names.INCOMES], "M")

    # Minimum of 2 months of data
    if min(dfe.shape[0], dfi.shape[0]) < 2:
        return None

    df_baii = dfi - dfe

    df_baii.fillna(0, inplace=True)

    fig = FF.create_distplot(
        [df_baii[c.cols.AMOUNT], dfe[c.cols.AMOUNT], dfi[c.cols.AMOUNT]],
        [c.names.EBIT,  c.names.EXPENSES, c.names.INCOMES],
        colors=u.get_colors([("amber", 500), ("red", 500), ("green", 500)]),
        bin_size=100)

    fig['layout'].update(title="Incomes, Expenses and EBIT distribution")

    return fig
