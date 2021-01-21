import app as myapi
import unittest
import json
import sys

from app import db

class TestIntegration(unittest.TestCase):
    def setUp(self):
        db.create_all()
        self.app = myapi.app.test_client()

    def test_add_user(self):
        response = self.app.post('/api/user', json={'email': 'test@mail.com',
                                 'password': 'testPsw'})
        self.assertEqual(
            json.loads(response.get_data().decode(sys.getdefaultencoding()))
            ["member"]["email"], "test@mail.com")

    def test_list_users(self):
        response = self.app.get('/api/user')
        self.assertEqual(
            json.loads(response.get_data().decode(sys.getdefaultencoding()))
            [0]["email"], "test@mail.com")


if __name__ == '__main__':

    unittest.main()
