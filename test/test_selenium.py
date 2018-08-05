""" Tests the dash app works """
import unittest

from test.selenium_utils import open_dash, wait_until_loaded

import src.constants as c

class TestApp(unittest.TestCase):
    """ Tests the dash app works """

    driver = open_dash()

    def test_title(self):
        """ Test that the app is able to load """
        self.assertEqual("Dash", self.driver.title)


    def test_pages(self):
        """ Test that is possible to open all pages """

        for page in c.dash.DICT_APPS.values():
            print(c.dash.LINK_ROOT + page)
            self.driver.get(c.dash.LINK_ROOT + page)
            wait_until_loaded(self.driver)
            self.assertEqual("Dash", self.driver.title)



if __name__ == '__main__':
    unittest.main()
