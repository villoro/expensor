"""
    Dash app
"""

import pandas as pd

import constants as c


def get_df(uri):
    """
        Retrives a dataframe with data.
    """

    df = pd.read_csv(uri, sep=";", index_col=0)

    # Add time filter columns (store everything as string to ensure JSON compatibility)
    df[c.cols.DATE] = pd.to_datetime(df[c.cols.DATE])
    df[c.cols.MONTH_DATE] = pd.to_datetime(df[c.cols.DATE].dt.strftime("%Y-%m-01"))
    df[c.cols.MONTH] = df[c.cols.DATE].dt.month
    df[c.cols.YEAR] = df[c.cols.DATE].dt.year

    # Tag expenses/incomes
    df.loc[df[c.cols.AMOUNT] > 0, c.cols.TYPE] = c.names.INCOMES
    df[c.cols.TYPE].fillna(c.names.EXPENSES, inplace=True)

    # Amount as positve number
    df[c.cols.AMOUNT] = df[c.cols.AMOUNT].apply(abs)

    return df

class Data:
    """
        Object that handles global dataframes

        Atributes:
            df_trans:   dataframe of transactions
            categories: list of all posible categories
    """

    def __init__(self, uri=c.os.FILE_DATA_SAMPLE):
        """
            Intialize the Data helper class.

            Args:
                uri:        uri of the starter dataframe to load
        """

        df = get_df(uri)
        self.set_transactions(df)


    def set_transactions(self, df):
        """
            Updates the transactions dataframe with the given dataframe
        """

        self.df_trans = df
        self.categories = df[c.cols.CATEGORY].unique().tolist()
