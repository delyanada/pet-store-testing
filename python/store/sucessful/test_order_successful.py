import random

import requests
import unittest


class TestOrderSuccessful(unittest.TestCase):

    def test_crud_store(self):
        store_inventory_id=random.randint(1, 100000000)

        r=requests.post(url="https://petstore.swagger.io/v2/store/order",
                        headers={"Content-Type": "application/json"},
                        json={
                            "id": store_inventory_id,
                            "petId": 0,
                            "quantity": 0,
                            "shipDate": "2019-03-27T19:40:17.436Z",
                            "status": "placed",
                            "complete": False}
                        )

        self.assertEqual(r.status_code, 200)

        r=requests.get(url=f"http://petstore.swagger.io/v2/store/order/{store_inventory_id}")

        self.assertEqual(r.status_code, 200)

        r=requests.delete(url=f"http://petstore.swagger.io/v2/store/order/{store_inventory_id}")

        self.assertEqual(r.status_code, 200)

        r=requests.get(url=f"http://petstore.swagger.io/v2/store/order/{store_inventory_id}")

        self.assertEqual(r.status_code, 404)

    def test_find_by_inventory(self):

        r=requests.get(url=f"http://petstore.swagger.io/v2/store/inventory")

        self.assertEqual(r.status_code, 200)
