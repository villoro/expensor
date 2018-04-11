"""
	Individual plots
"""

import plotly.graph_objs as go

import constants as c
import utilities as u


def plot_timeserie(dfg, timewindow="M"):
    """
        Creates a timeseries plot with expenses, incomes and their regressions

        Args:
            dfg:	dataframe with info

        Returns:
            the plotly plot as html-div format
    """

    # Income/Expense traces
    iter_data = {c.names.INCOMES: c.colors.INCOMES, c.names.EXPENSES: c.colors.EXPENSES}

    data = []

    for name, color in iter_data.items():
        df = u.dfs.group_df_by(dfg[dfg[c.cols.TYPE] == name], timewindow)
        data.append(
            go.Scatter(
                x=df.index, y=df[c.cols.AMOUNT],
                marker={"color": color},
                name=name
            )
        )

    # Calculate EBIT
    df = dfg.copy()
    mfilter = df[c.cols.TYPE] == c.names.EXPENSES
    df.loc[mfilter, c.cols.AMOUNT] = - df.loc[mfilter, c.cols.AMOUNT]

    # EBIT trace
    df = u.dfs.group_df_by(df, timewindow)
    data.append(
        go.Scatter(
            x=df.index, y=df[c.cols.AMOUNT],
            marker={"color": c.colors.EBIT},
            name=c.names.EBIT
        )
    )

    # EBIT cum trace
    data.append(
        go.Scatter(
            x=df.index, y=df[c.cols.AMOUNT].cumsum(),
            marker={"color": c.colors.EBIT_CUM},
            name=c.names.EBIT_CUM
        )
    )

    layout = go.Layout(title="Evolution")
    return go.Figure(data=data, layout=layout)
