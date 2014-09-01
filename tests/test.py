import sys
import os
import unittest

# might be a better way to run tests from project root and satisfy ide?
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.insert(0, os.getcwd())

from flaskapi import app
from BeautifulSoup import *


class BasicTestCase(unittest.TestCase):

    def setup_get_html_test(self, url):
        tester = app.test_client(self)
        response = tester.get(url, content_type='html/text')
        return response

    def count_markup_elements(self, markup, element):
        parsed = BeautifulSoup(markup)
        count = len(parsed.findAll(str(element)))
        return count

    def test_get_publish_html(self):
        """Test status code 405 from improper JSON on post to raw"""
        response = self.setup_get_html_test('/api/publish')
        self.assertEqual(response.status_code, 200)

    def test_get_publish_content_html(self):
        """make sure we have a form rendered"""
        response = self.setup_get_html_test('/api/publish')
        count_elements = self.count_markup_elements(response.data, 'input')
        self.assertEqual(count_elements, 4)

    def test_get_monitor_html(self):
        """Test monitor object is present"""
        response = self.setup_get_html_test('/monitor')
        self.assertEqual(response.status_code, 200)

    def test_get_monitor_content_html(self):
        """Test monitor object is present"""
        response = self.setup_get_html_test('/monitor')
        self.assertEqual(response.data, "OK")

    def test_get_view_html(self):
        """Test monitor object is present"""
        response = self.setup_get_html_test('/api/view/1')
        self.assertEqual(response.status_code, 200)

    def test_get_index_html(self):
        """query the index view"""
        response = self.setup_get_html_test('/api/index')
        self.assertEqual(response.status_code, 200)

    def test_get_get_html(self):
        """test download"""
        response = self.setup_get_html_test('/api/get/1')
        self.assertEqual(response.status_code, 200)

    def test_get_404_html(self):
        """test 404 error"""
        response = self.setup_get_html_test('/api/nothing/is/here')
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()
