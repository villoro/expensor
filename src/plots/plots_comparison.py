"""
	Individual plots
"""

import plotly.graph_objs as go

import constants as c
import utilities as u


def ts_gradient(dfg, type_trans):
    """
        Creates a timeseries plot where all years are ploted simultaneously

        Args:
            dfg:        dataframe to use
            type_trans: type of transaction [Income/Expense]

        Returns:
            the plotly plot as html-div format
    """

    df = u.dfs.group_df_by(dfg[dfg[c.cols.TYPE] == type_trans], "M")

    if df.shape[0] == 0:
        return None

    min_size, max_width = 3, 5

    mdict = {c.names.INCOMES: "green", c.names.EXPENSES: "red"}
    color_name = mdict[type_trans]

    data = []

    min_year, max_year = min(df.index.year), max(df.index.year)

    for year in sorted(set(df.index.year), reverse=False):

        if year == max_year:
            index_color = 900
        else:
            index_color = max(100, 600 - 200*(max_year - year))

        color = u.get_colors([(color_name, index_color)])

        data.append(
            go.Scatter(
                x=df.index.month,
                y=df[df.index.year == year][c.cols.AMOUNT].values,
                line={"width": min(0.5*(year - min_year) + 1, max_width)},
                marker={"color": color, "size": year - min_year + min_size},
                name=year
            )
        )

    layout = go.Layout(title="Time comparison ({})".format(type_trans))
    return go.Figure(data=data, layout=layout)
