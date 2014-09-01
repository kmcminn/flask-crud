import sys, os
import unittest

# might be a better way to run tests from project root and satisfy ide?
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..')))
sys.path.insert(0, os.getcwd())

from flaskapi import app

class BasicTestCase(unittest.TestCase):

    def test_publish_get_form(self):
        """Test status code 405 from improper JSON on post to raw"""
        tester = app.test_client(self)
        response = tester.get('/api/publish')
        self.assertEqual(response.status_code, 200)

    def test_search_monitor_record_exists(self):
        """Test monitor object is present"""
        tester = app.test_client(self)
        response = tester.get('/monitor', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, "OK")

    def test_get_single_record_html(self):
        """Test monitor object is present"""
        tester = app.test_client(self)
        response = tester.get('/api/view/1', content_type='html/text')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
