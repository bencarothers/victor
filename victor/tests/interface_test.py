import unittest
from ..interface import interface


class interfaceTestCase(unittest.TestCase):

    def setUp(self):
        interface.app.config['TESTING'] = True
        self.test_app = interface.app.test_client()

    def tearDown(self):
        # this will be for database tear down
        pass

    def test_holder_page(self):
        response = self.test_app.get("/")
        self.assertEquals(response.status_code, 200)
