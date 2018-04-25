"""
    Tests for constants.py
"""

import unittest

import sys
sys.path.append("../src")

import constants as c

class Test_constants(unittest.TestCase):
    """Test constants"""

    def test_path_data(self):
        """
            Tests that Path data exists
        """
        self.assertEqual(c.os.PATH_DATA, "../data/")



if __name__ == '__main__':
    unittest.main()
