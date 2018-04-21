"""
	Individual plots
"""

import plotly.graph_objs as go

import constants as c


def violin_plot(dfg, col_group):
    """
        Creates a violin plot with expenses and incomes

        Args:
            dfg:        dataframe to use
            col_group:  grouping column

        Returns:
            the plotly plot as html-div format
    """

    df = dfg.groupby([c.cols.YEAR, c.cols.MONTH, c.cols.TYPE]).sum().reset_index()

    iter_data = [
        (c.names.EXPENSES, "negative", c.colors.EXPENSES),
        (c.names.INCOMES, "positive", c.colors.INCOMES)
    ]

    data = []

    for name, side, color in iter_data:

        df_aux = df[df[c.cols.TYPE] == name]

        data.append(
            go.Violin(
                x=df_aux[col_group], y=df_aux[c.cols.AMOUNT],
                name=name, side=side, line={"color": color}
            )
        )

    layout = go.Layout(title="Violin ({})".format(col_group))
    return go.Figure(data=data, layout=layout)
