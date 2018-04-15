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

    col = {"D": c.cols.DATE, "M": c.cols.MONTH, "Y": c.cols.YEAR}[timewindow]

    return df[[col, c.cols.AMOUNT]].groupby(col).sum()


def filter_data(df_input, categories):
    """
        Filters the dataframe that will be reused in all plots

        Args:
            categories
    """

    df = df_input.copy()

    if categories:
        if isinstance(categories, list):
            df = df[df[c.cols.CATEGORY].isin(categories)]
        else:
            df = df[df[c.cols.CATEGORY] == categories]

    return df
