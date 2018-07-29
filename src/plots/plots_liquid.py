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

    data = [go.Scatter(x=df_liq.index, y=df_liq[c.names.TOTAL],
                       marker={"color": "black"}, name=c.names.TOTAL)]

    for level in df_list[c.cols.LIQUID_LEVEL].unique():
        df_aux = df_list[df_list[c.cols.LIQUID_LEVEL] == level]
        name_liq = df_aux[c.cols.LIQUID_NAME].tolist()[0]
        name_trace = "{} - {}".format(level, name_liq)

        df = df_liq[df_aux[c.cols.NAME].tolist()].sum(axis=1)
        color = u.get_colors(("blue", 100 + 200*level))

        data.append(go.Bar(x=df.index, y=df, marker={"color": color}, name=name_trace))

    layout = go.Layout(title="Liquid evolution", barmode="stack")
    return go.Figure(data=data, layout=layout)


def plot_expenses_vs_liquid(df_liquid_in, df_trans_in, avg_month=12):
    
    df_l = df_liquid_in.set_index(c.cols.DATE).copy()
    df_l = df_l.rolling(avg_month, min_periods=1).mean()

    df_t = u.dfs.group_df_by(df_trans_in[df_trans_in[c.cols.TYPE] == c.names.EXPENSES], "M")
    df_t = df_t.rolling(avg_month, min_periods=1).mean()

    iter_data = [
        (df_t, df_t[c.cols.AMOUNT], c.names.EXPENSES, c.colors.EXPENSES),
        (df_t, 3*df_t[c.cols.AMOUNT], c.names.LIQUID_MIN_REC, c.colors.LIQUID_MIN_REC),
        (df_t, 6*df_t[c.cols.AMOUNT], c.names.LIQUID_REC, c.colors.LIQUID_REC),
        (df_l, df_l[c.names.TOTAL], c.names.LIQUID, c.colors.LIQUID),
    ]
    
    data = [go.Scatter(x=df.index, y=y, name=name, marker={"color": color})
            for df, y, name, color in iter_data]

    layout = go.Layout(title="Liquid vs Expenses")
    return go.Figure(data=data, layout=layout)
