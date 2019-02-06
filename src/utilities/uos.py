"""
    os utilities
"""

import os
import io
import base64
import pandas as pd

import constants as c


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

                print(f"Path {uri} doesn't exists. Created automatically")


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
            print("Unable to delete.", e)

    return False


def parse_dataframe_uploaded(contents, filename):
    """
        Tries to parse a dataframe from a file uploaded

        Args:
            contents:   data uploaded
            filename:   name of the file uploaded

        Returns:
            dataframe if possible
    """

    if (not contents) or (contents is None):
        return None

    _, content_string = contents.split(',')

    # Decode from base64 and get from bytes
    data = io.BytesIO(base64.b64decode(content_string))

    extension = filename.split(".")[-1]

    # Try to read it as an excel file
    if extension == "xlsx":
        try:
            return pd.read_excel(data)

        except Exception: #pylint: disable=W0703
            return c.io.ERROR_UNPARSABLE

    # For unkown file extension throw an error message
    else:
        return c.io.ERROR_EXTENSION


def df_to_b64(df):
    """
        Transform a pandas dataframe to base64 encoded bytes
    """

    mbuffer = io.BytesIO()
    df.to_msgpack(mbuffer)
    mbuffer.seek(0)
    b64_string = base64.b64encode(mbuffer.read())

    return b64_string.decode()


def b64_to_df(b64_string):
    """
        Retrives a pandas dataframes from base64 encoded bytes
    """

    return pd.read_msgpack(io.BytesIO(base64.b64decode(b64_string)))


def get_image(image_uri):
    """
        Loads a local png to be shown in dash

        Args:
            image_uri:  uri of the image

        Returns:
            the string to be placed in a html.Img container
    """
    with open(image_uri, "rb") as file:
        encoded = base64.b64encode(file.read())

    return f"data:image/png;base64,{encoded.decode()}"
