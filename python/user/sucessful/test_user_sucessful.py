import random

import requests
import unittest

"""The service fails with 500 error(su"""


class TestUserSucessful(unittest.TestCase):
    API_HOST="https://petstore.swagger.io"

    def test_crud_user(self):
        """This test creates,read,updates,delete user"""
        user_id=random.randint(1, 100000000)

        r=requests.post(url=f"{self.API_HOST}/v2/user",
                        headers={"Content-Type": "application/json"},
                        json={
                            "id": user_id,
                            "username": 0,
                            "firstName": "string",
                            "lastName": "string",
                            "email": "string",
                            "password": "string",
                            "phone": "string",
                            "userStatus": 0
                        })

        self.assertEqual(r.status_code, 500)

        r=requests.get(url=f"{self.API_HOST}/v2/user/{user_id}")

        self.assertEqual(r.status_code, 500)

        random_updated_username=random.randint(1, 1000000)

        r=requests.put(url=f"{self.API_HOST}/v2/user/{user_id}",
                       json={
                           "id": user_id,
                           "username": random_updated_username,
                           "firstName": "string",
                           "lastName": "string",
                           "email": "string",
                           "password": "string",
                           "phone": "string",
                           "userStatus": 0
                       }
                       )

        self.assertEqual(r.status_code, 500)

        r=requests.get(url=f"{self.API_HOST}/v2/user/{user_id}")

        self.assertEqual(r.status_code, 500)

        r=requests.delete(url=f"{self.API_HOST}/v2/user/{user_id}")

        self.assertEqual(r.status_code, 500)

        r=requests.get(url=f"{self.API_HOST}/v2/user/{user_id}")

        self.assertEqual(r.status_code, 500)
