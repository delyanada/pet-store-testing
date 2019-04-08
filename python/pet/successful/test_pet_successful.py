import json
import random

import requests
import unittest


class TestPetSuccessful(unittest.TestCase):

    API_HOST = "https://petstore.swagger.io"

    def test_crud_pet(self):
        # Add test to create pet
        """This test creates,read,updates,delete pet"""
        pet_id=random.randint(1, 100000000)

        r=requests.post(url=f"{self.API_HOST}/v2/pet",
                        headers={"Content-Type": "application/json"},
                        json={
                            "id": pet_id,
                            "category": {
                                "id": 0,
                                "name": "string"
                            },
                            "name": "doggie",
                            "photoUrls": [
                                "string"
                            ],
                            "tags": [
                                {
                                    "id": 0,
                                    "name": "string"
                                }
                            ],
                            "status": "available"
                        })

        self.assertEqual(200, r.status_code)

        # Add test to update

        r=requests.get(url=f"{self.API_HOST}/v2/pet/{pet_id}")

        self.assertEqual(r.status_code, 200)

        # Add test to read
        r=requests.put(url=f"{self.API_HOST}/v2/pet",
                       json={
                           "id": pet_id,
                           "category": {
                               "id": 0,
                               "name": "hhhh"
                           },
                           "name": "borko",
                           "photoUrls": [
                               "string"
                           ],
                           "tags": [
                               {
                                   "id": 0,
                                   "name": "string"
                               }
                           ],
                           "status": "available"})

        self.assertEqual(r.status_code, 200)

        new_dog=json.loads(r.text)
        self.assertEqual(new_dog['name'], 'borko')

        # Add test to delete
        r=requests.delete(url=f"{self.API_HOST}/v2/pet/{pet_id}")
        self.assertEqual(r.status_code, 200)

        r=requests.get(url=f"{self.API_HOST}/v2/pet/{pet_id}")
        self.assertEqual(r.status_code, 404)

    def test_fetch_by_status_available(self):
        r=requests.get(f"{self.API_HOST}/v2/pet/findByStatus?status=available")

        self.assertEqual(r.status_code, 200)

        response_list = json.loads(r.text)
        for pet in response_list:
            self.assertEqual(pet["status"],"available")

    def test_fetch_by_pending(self):
        r=requests.get(f"{self.API_HOST}/v2/pet/findByStatus?status=pending")

        self.assertEqual(r.status_code, 200)

        response_list=json.loads(r.text)
        for pet in response_list:
            self.assertEqual(pet["status"], "pending")

    def test_fetch_by_sold(self):
        r=requests.get(f"{self.API_HOST}/v2/pet/findByStatus?status=sold")

        self.assertEqual(r.status_code, 200)

        response_list=json.loads(r.text)
        for pet in response_list:
            self.assertEqual(pet["status"], "sold")

    def test_by_status(self):
        """ Tests finding pet by status (available, pending, sold) """

