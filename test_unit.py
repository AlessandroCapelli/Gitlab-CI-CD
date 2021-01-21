import app as myapi
import unittest
import json
import sys


class TestUnit(unittest.TestCase):

    def setUp(self):
        self.app = myapi.app.test_client()

    def test_default_path(self):
        response = self.app.get('/')
        self.assertEqual(
            json.loads(response.get_data().decode(sys.getdefaultencoding())),
            {"message": "ok"}
        )


if __name__ == '__main__':

    unittest.main()
