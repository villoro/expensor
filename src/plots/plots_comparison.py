"""
	Individual plots
"""

import plotly.graph_objs as go

import constants as c
import utilities as u


def ts_gradient(dfg, type_trans, avg_month):
    """
        Creates a timeseries plot where all years are ploted simultaneously

        Args:
            dfg:        dataframe to use
            type_trans: type of transaction [Income/Expense]
            avg_month:  month to use in rolling average

        Returns:
            the plotly plot as html-div format
    """

    if type_trans in [c.names.INCOMES, c.names.EXPENSES]:
        df = dfg[dfg[c.cols.TYPE] == type_trans].copy()

    else:
        df = dfg.copy()
        mfilter = df[c.cols.TYPE] == c.names.EXPENSES
        df.loc[mfilter, c.cols.AMOUNT] = - df.loc[mfilter, c.cols.AMOUNT]

    df = u.dfs.group_df_by(df, "M")

    if df.shape[0] == 0:
        return {}

    # Compute rolling average
    if avg_month > 0:
        df = df.rolling(avg_month, min_periods=1).mean()

    min_size, max_width = 3, 5

    color_name = {c.names.INCOMES: "green", c.names.EXPENSES: "red"}.get(type_trans, "amber")

    data = []

    for year in sorted(set(df.index.year), reverse=False):

        if year == max(df.index.year):
            index_color = 900
        else:
            index_color = max(100, 600 - 200*(max(df.index.year) - year))

        color = u.get_colors([(color_name, index_color)])

        df_aux = df[df.index.year == year]

        data.append(
            go.Scatter(
                x=df_aux.index.month,
                y=df_aux[c.cols.AMOUNT].values,
                line={"width": min(0.5*(year - min(df.index.year)) + 1, max_width)},
                marker={"color": color, "size": year - min(df.index.year) + min_size},
                name=year
            )
        )

    layout = go.Layout(title="Time comparison ({})".format(type_trans))
    return go.Figure(data=data, layout=layout)
