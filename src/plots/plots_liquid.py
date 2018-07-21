"""
	Individual plots
"""

import plotly.graph_objs as go

import constants as c


def liquid_plot(df_liq_in, df_list):
    """
        Creates a pie with expenses or incomes

        Args:
            df_liq_in:  dataframe with liquid info
            df_list:    dataframe with types of liquids

        Returns:
            the plotly plot as html-div format
    """

    df_liq = df_liq_in.set_index("Date")

    data = []
    for level in df_list["Liquidity level"].unique():
        df_aux = df_list[df_list["Liquidity level"] == level]
        name = df_aux["Liquidity name"].tolist()[0]
        
        df = df_liq[df_aux["Name"].tolist()].sum(axis=1)
        
        data.append(go.Bar(x=df.index, y=df, name="{} - {}".format(level, name)))

    layout = go.Layout(title="Liquid evolution", barmode="stack")
    return go.Figure(data=data, layout=layout)
