import unittest
import random

import requests


class TestPurchaseOrderInvalid(unittest.TestCase):

    API_HOST = "http://petstore.swagger.io"

    def test_purchase_invalid_order_by_id(self):
        store_inventory_invalid_id=random.randint(1, 100000000)

        r=requests.get(url=f"{self.API_HOST}/v2/store/order/{store_inventory_invalid_id}")

        self.assertEqual(r.status_code, 404)
