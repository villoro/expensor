""" Tests the dash app works """
import unittest

from test.selenium_utils import open_dash, wait_until_loaded

import src.constants as c


class TestApp(unittest.TestCase):
    """ Tests the dash app works """

    driver = open_dash()

    def test_title(self):
        """ Test that the app is able to load """
        self.assertEqual(c.names.TITLE, self.driver.title)

    def test_pages(self):
        """ Test that is possible to open all pages """

        for page in c.dash.LINKS_ALL:
            self.driver.get(c.dash.LINK_ROOT + page)
            wait_until_loaded(self.driver)

            # Check that there is a body and filters divs
            self.driver.find_element_by_id("body")
            self.driver.find_element_by_id("filters")

    def _check_one_page(self, page_link, elements):
        """
            Check the existence of some elements in a page

            Args:
                page_link:  relative url to the page
                elements:   what to look for
        """

        self.driver.get(c.dash.LINK_ROOT + page_link)
        wait_until_loaded(self.driver)

        # Check that there is a sidebar and a body
        for elem in elements:
            self.driver.find_element_by_id(elem)

    def test_page_upload(self):
        """ Test the content of page upload """

        contents = [
            "upload_container",
            "upload_colapse_error_message",
            "upload_colapse_success_message",
            "upload_button",
            "upload_table_preview",
            "upload_colapse_preview",
            "upload_results",
        ]
        self._check_one_page(c.dash.LINK_UPLOAD, contents)

    def test_page_evolution(self):
        """ Test the content of page evolution """

        contents = ["plot_evol", "plot_evo_detail", "radio_evol_type"]
        filters = ["input_categories", "input_smoothing", "input_timewindow"]
        self._check_one_page(c.dash.LINK_EVOLUTION, contents + filters)

    def test_page_comparison(self):
        """ Test the content of page comparison """

        contents = ["plot_comp_1", "radio_comp_1", "plot_comp_2", "radio_comp_2"]
        filters = ["input_categories", "input_smoothing"]
        self._check_one_page(c.dash.LINK_COMPARISON, contents + filters)

    def test_page_heatmaps(self):
        """ Test the content of page heatmaps """

        contents = ["plot_heat_i", "plot_heat_e", "plot_heat_distribution"]
        filters = ["input_categories"]
        self._check_one_page(c.dash.LINK_HEATMAPS, contents + filters)

    def test_page_pies(self):
        """ Test the content of page pies """

        types = [c.names.INCOMES, c.names.EXPENSES]
        contents = ["plot_pie_{}_{}".format(i, x) for i in range(2) for x in types]
        contents += ["drop_pie_0", "drop_pie_1"]

        filters = ["input_categories"]
        self._check_one_page(c.dash.LINK_PIES, contents + filters)


if __name__ == "__main__":
    unittest.main()
