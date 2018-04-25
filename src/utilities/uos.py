"""
    os utilities
"""

import os
import pandas as pd
import constants as c
from utilities import ulog

log = ulog.set_logger(__file__)


def check_if_uri_exist(uris):
    """
        Checks if the folder is trying to use exists and if not, it will create it.

        Args:
            uris:    name or URI to be checked or list of uris
    """

    # If is not a list, make a list in order to iterate
    if not isinstance(uris, list):
        uris = [uris]

    for uri in uris:
        # Check that it is not a file without path
        if len(uri.split("/")) > 1:
            uri = uri.rsplit('/', 1)[0]

            # If the directory doesn't exist, it will be created.
            if not os.path.isdir(uri):
                os.makedirs(uri, exist_ok=True)

                log.info("Path %s doesn't exists. Created automatically", uri)


def delete_if_possible(uri):
    """
        Deletes a file if exists

        Args:
            uri:    file to delete
    """

    if os.path.isfile(uri):
        try:
            os.remove(uri)
            return True

        except IOError as e:
            log.error("Unable to delete.", error=e)

    return False


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
