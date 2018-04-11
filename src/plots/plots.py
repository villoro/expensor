"""
	Individual plots
"""

import plotly.graph_objs as go

import constants as c
import utilities as u


def plot_timeserie(df_input, timewindow="M"):
    """
        Creates a timeseries plot with expenses, incomes and their regressions

        Args:
            df:	dataframe with info

        Returns:
            the plotly plot as html-div format
    """

    iter_data = {c.names.INCOMES: c.colors.INCOMES, c.names.EXPENSES: c.colors.EXPENSES}

    data = []
    for name, color in iter_data.items():

        df = u.dfs.group_df_by(df_input[df_input[c.cols.TYPE] == name], timewindow)

        data.append(
            go.Scatter(
                x=df.index, y=df[c.cols.AMOUNT],
                marker={"color": color},
                name=name
            )
        )

    return go.Figure(data=data)
