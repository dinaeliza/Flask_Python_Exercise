import unittest
import requests
import json
import os

#import Python_Exercise1.common.geo_xml_parser as geo
from basic_test import names_and_notes

class TestServerOperation(unittest.TestCase):

    def test_get_notes(self):
        test_response1 = requests.get('http://127.0.0.1:5000/geo_Notes/hub_ethernet_sniffer')
        test_dict1 = test_response1.json()
        self.assertEqual(test_dict1['hub_ethernet_sniffer'] , names_and_notes['hub_ethernet_sniffer'])

    def test_get_status_code(self):
        test_response2= requests.get('http://127.0.0.1:5000/geo_Notes/ct')
        self.assertEqual(test_response2.status_code, 200)


if __name__ == '__main__':
    unittest.main()


