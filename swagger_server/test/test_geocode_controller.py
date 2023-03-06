# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.address import Address  # noqa: E501
from swagger_server.models.geocoded import Geocoded  # noqa: E501
from swagger_server.models.nena import NENA  # noqa: E501
from swagger_server.test import BaseTestCase


class TestGeocodeController(BaseTestCase):
    """GeocodeController integration test stubs"""

    def test_geocode_addr(self):
        """Test case for geocode_addr

        Get latitude and longitude from string containing address
        """
        body = Address()
        data = dict(address='address_example')
        response = self.client.open(
            '/geocode/address',
            method='POST',
            data=json.dumps(body),
            data=data,
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_geocode_nena(self):
        """Test case for geocode_nena

        Get latitude and longitude from NENA formatted address
        """
        body = NENA()
        data = dict(house_number='house_number_example',
                    house_number_suffix='house_number_suffix_example',
                    prefix_directional='prefix_directional_example',
                    street_name='street_name_example',
                    street_suffix='street_suffix_example',
                    post_directional='post_directional_example',
                    community_name='community_name_example',
                    state='state_example',
                    zip_code='zip_code_example',
                    country='country_example')
        response = self.client.open(
            '/geocode/nena',
            method='POST',
            data=json.dumps(body),
            data=data,
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
