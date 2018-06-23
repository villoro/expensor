"""
    Time utilities
"""

import time
from datetime import datetime


class Timer():
    """
        Object used to show times of execution

        Args:
            baseline:    time of the last measure
    """

    def __init__(self):
        self.baseline = time.time()
        self.baseline_global = time.time()

    def get_time(self):
        """
            It gives the time passed since the last measure. It restart everytime it is asked.

            Returns:
                time as string rounded at 2
        """

        seconds = time.time() - self.baseline

        # reset time
        self.baseline = time.time()

        return seconds


    def get_global_time(self):
        """
            It gives the time passed since the first measure.

            Returns:
                time as string rounded at 2
        """

        return time.time() - self.baseline_global


def wait_until(mdatetime):
    """
        Given a datetime do nothing if is minus than now or wait
        for datettime_object if it's moren than now
    """

    while True:
        mtime = (mdatetime - datetime.now()).total_seconds()
        if mtime <= 0:
            break

        else:
            time.sleep(mtime)
