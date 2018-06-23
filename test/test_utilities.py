"""
    Tests for utilities.py
"""

import unittest
from os import rmdir
from datetime import datetime, timedelta

from src import utilities as u

class TestUtilities(unittest.TestCase):
    """Test utilities"""

    dummy_path = "imaginary_path_for_testing/"


    def test_palette(self):
        """
            Test palette
        """

        # Test that you can call one color with a list of tuples or with a tuple
        self.assertEqual(u.get_colors([("red", 100)]), "#FFCDD2")
        self.assertEqual(u.get_colors(("red", 100)), "#FFCDD2")

        # Test that you can call more than one color
        self.assertEqual(u.get_colors([("red", 100), ("blue", 100)]),
                         ["#FFCDD2", "#BBDEFB"])


    def test_utime(self):
        """
            Test utime
        """

        # Try invalid time
        u.utime.wait_until(datetime.now() - timedelta(seconds=1))

        # Try valid time
        u.utime.wait_until(datetime.now() + timedelta(seconds=1))

        # This should be faster than 10 seconds
        timer = u.utime.Timer()
        self.assertLess(timer.get_time(), 10)
        self.assertLess(timer.get_global_time(), 10)


    def test_check_uri(self):
        """
            Test check_if_uri_exist
        """

        u.uos.check_if_uri_exist(self.dummy_path)

        rmdir(self.dummy_path)



if __name__ == '__main__':
    unittest.main()
