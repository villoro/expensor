"""
    Tests for dash_app.py
"""

import unittest

from src import dash_app


class TestDashApp(unittest.TestCase):
    """Test dash_app"""


    def test_app_creation(self):
        """
            Test the creation of dash app
        """

        app, _ = dash_app.create_dash_app()

        self.assertEqual(app.url_base_pathname, "/")

        self.assertTrue(app.config['supress_callback_exceptions'])



if __name__ == '__main__':
    unittest.main()
