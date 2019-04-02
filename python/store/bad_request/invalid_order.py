import unittest
import requests


class TestBadRequest(unittest.TestCase):
    def test_invalid_order(self):
        r=requests.post(url="https://petstore.swagger.io/v2/store/order",
                        headers={"Content-Type": "application/json"})

        self.assertEqual(r.status_code, 500)

    def test_invalid_timestamp(self):
        r=requests.post(url="https://petstore.swagger.io/v2/store/order",
                        headers={"Content-Type": "application/json"},
                        json={
                            "id": 51828913,
                            "petId": 0,
                            "quantity": 0,
                            "shipDate": "2019na;lskdals;dksal;dkasl;dkas;ldkas;l:40:17.436Z",
                            "status": "placed",
                            "complete": False
                        })

        self.assertEqual(r.status_code, 500)

    def test_bad_request(self):
        """Status field is supposed to be string"""
        """The code is not right it should really return 400"""

        r=requests.post(url="https://petstore.swagger.io/v2/store/order",
                        headers={"Content-Type": "application/json"},
                        json={
                            "id": 51828913,
                            "petId": 0,
                            "quantity": 0,
                            "shipDate": "2019-03-27T19:40:17.436Z",
                            "status": 1,
                            "complete": False
                        })

        self.assertEqual(r.status_code, 200)
