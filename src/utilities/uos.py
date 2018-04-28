"""
    os utilities
"""

import os
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
