# Implementation of a test suite for the IoT-sdk for Python.
# This is kind of over-tested and the type of tests are not
# well separated (unit, integration, etc)
# 
# To run the tests:
#   source ../.env/bin/activate && nosetests --verbose


import unittest
import secrets
from iotsdk import Iot


class TestIotSdk(unittest.TestCase):
    """ Tests the IotSDK """
    
    def setUp(self):
        self.iot = Iot("um_token")

    def test_build_endpoints(self):
        stub_endpoints_route = {
            "service_details": "services/um_token",
            "asset_details": "services/um_token/assets",
            "asset_history": "services/um_token/assets/um_token",
            "asset_data": "services/um_token/assets/um_token/data" 
        }
        self.assertEqual(self.iot._buildEndpointsRoute(),\
            stub_endpoints_route)

    def test_build_query(self):
        stub_args = {"key": "value", "key2": "value2"}
        stub_query = "key2=value2&key=value"
        self.assertEqual(self.iot._buildQuery(stub_args), stub_query)

    def test_build_path(self):
        base_path = "http://dca.telefonicabeta.com/m2m/v2/"
        expected_sd = base_path + "services/um_token"
        expected_ad = base_path + "services/um_token/assets"
        expected_ah = base_path + "services/um_token/assets/um_token"
        expected_adata = base_path + "services/um_token/assets/um_token/data"

        path_service_details = self.iot._buildPath("service_details")
        path_asset_details = self.iot._buildPath("asset_details")
        path_asset_history = self.iot._buildPath("asset_history")
        path_asset_adata = self.iot._buildPath("asset_data")

        self.assertEqual(path_service_details, expected_sd) 
        self.assertEqual(path_asset_details, expected_ad)
        self.assertEqual(path_asset_history, expected_ah)
        self.assertEqual(path_asset_adata, expected_adata)
        # it needs some tests with params

    def test_get_services_details(self):
        self.assertFalse(self.iot.get_services_details())
        self.iot2 = Iot(secrets.IOT_TOKEN)  # get from the testing env
        self.assertTrue(self.iot2.get_services_details())

    def test_get_connected_devices(self):
        self.assertFalse(self.iot.get_connected_devices())
        self.iot2 = Iot(secrets.IOT_TOKEN)  # get from the testing env
        self.assertTrue(self.iot2.get_connected_devices())        

    def test_get_device_data(self):
        self.assertFalse(self.iot.get_device_data())
        self.iot2 = Iot(secrets.IOT_TOKEN)
        self.assertTrue(self.iot2.get_device_data()) # will take a while

        self.assertTrue(self.iot2.get_device_data(limit=10))
        self.assertTrue(self.iot2.get_device_data(limit=10,lol=10))

    def test_get_device_full_data(self):
        self.assertFalse(self.iot.get_device_full_data())
        self.iot2 = Iot(secrets.IOT_TOKEN)
        self.assertTrue(self.iot2.get_device_full_data())


if __name__ == "__main__":
    unittest.main()