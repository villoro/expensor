"""
    Utilities for pandas dataframes
"""

import constants as c


def group_df_by(df, timewindow):
    """
        Groups a dataframe by the given timewindow

        Args:
            df:         dataframe to group
            timewindow: temporal agrupation to use

        Returns:
            dataframe grouped
    """

    col = {"D": c.cols.DATE, "M": c.cols.MONTH_DATE, "Y": c.cols.YEAR}[timewindow]

    return df[[col, c.cols.AMOUNT]].groupby(col).sum()


def filter_data(df_input, values=None, col_name=c.cols.CATEGORY):
    """
        Filters the dataframe that will be reused in all plots

        Args:
            values:     values to include
            col_name:   reference column for filtering
    """

    df = df_input.copy()

    if values:
        if isinstance(values, list):
            df = df[df[col_name].isin(values)]
        else:
            df = df[df[col_name] == values]

    return df
