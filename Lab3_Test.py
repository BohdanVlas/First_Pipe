import unittest
import Lab3 as test_lab
import json

class LabTests(unittest,TestCase):

    def setUp(self):
        self.app = test_lab.app.test_client()

    def test_get_hello_endpoint(self):
        r = self.app.get('/')
        self.assertEqual(r.status, '200 OK')
        self.assertEqual(r.data, b'Hello world!!! This app testing pipeline.')

if __name__ == '__main__':
    #import xmlrunner
    #runner = xmlrunner.XMLTestRunner(output='test-reports')
    #unittest.main(testRunner=runner)
    unittest.main()