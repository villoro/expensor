"""
    Tests for constants.py
"""

import unittest
import os

from src import constants as c

class TestConstants(unittest.TestCase):
    """Test constants"""

    def test_sample_data(self):
        """
            Tests that Path data exists
        """
        self.assertTrue(os.path.isfile(c.io.FILE_DATA_SAMPLE))



if __name__ == '__main__':
    unittest.main()
