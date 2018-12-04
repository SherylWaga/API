import unittest
import os
import json
from app import create_app
class user(unittest.TestCase):
    def setUp(self):
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client
        self.data = {
            "Firstname": "sheryl",
            "Lastname": "omondi",
            "Registered": "Tue, 04 Dec 2018 19:41:50 GMT",
            "email": "sherylwaga@gmail.com",
            "id": 1,
            "password": "waga1236",
            "phonenumber": "07890567812",
            "username": "wags"
        }

    def test_register_user(self):
        res = self.client().post('/api/v1/users', data=json.dumps(self.data),
                                 content_type="application/json")
        self.assertEqual(res.status_code, 201)
        self.assertIn("Registration successful", str(res.data))
    def test_get_users(self):
        res = self.client().get('/api/v1/users', data=json.dumps(self.data),
                                content_type="application/json")
        self.assertEqual(res.status_code, 200)

if __name__ == '__main__':
    unittest.main()