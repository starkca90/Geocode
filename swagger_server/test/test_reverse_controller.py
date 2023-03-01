# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.reversed import Reversed  # noqa: E501
from swagger_server.test import BaseTestCase


class TestReverseController(BaseTestCase):
    """ReverseController integration test stubs"""

    def test_reverse(self):
        """Test case for reverse

        Get address from latitude and longitude
        """
        query_string = [('lat', 1.2),
                        ('lon', 1.2)]
        response = self.client.open(
            '/reverse',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
