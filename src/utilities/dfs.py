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
