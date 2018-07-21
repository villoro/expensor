"""
	Individual plots
"""

import plotly.graph_objs as go

import constants as c
import utilities as u


def liquid_plot(df_liq_in, df_list):
    """
        Creates a pie with expenses or incomes

        Args:
            df_liq_in:  dataframe with liquid info
            df_list:    dataframe with types of liquids

        Returns:
            the plotly plot as html-div format
    """

    df_liq = df_liq_in.set_index(c.cols.DATE)

    data = []
    for level in df_list[c.cols.LIQUID_LEVEL].unique():
        df_aux = df_list[df_list[c.cols.LIQUID_LEVEL] == level]
        name_liq = df_aux[c.cols.LIQUID_NAME].tolist()[0]
        name_trace = "{} - {}".format(level, name_liq)

        df = df_liq[df_aux[c.cols.NAME].tolist()].sum(axis=1)
        color = u.get_colors(("blue", 100 + 200*level))

        data.append(go.Bar(x=df.index, y=df, marker={"color": color}, name=name_trace))

    layout = go.Layout(title="Liquid evolution", barmode="stack")
    return go.Figure(data=data, layout=layout)
