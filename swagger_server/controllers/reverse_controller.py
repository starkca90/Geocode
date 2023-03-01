import connexion
import six

from swagger_server.models.reversed import Reversed  # noqa: E501
from swagger_server import util


def reverse(lat, lon):  # noqa: E501
    """Get address from latitude and longitude

    Provide latitude and longitude and get the address # noqa: E501

    :param lat: The latitude to do a reverse lookup on
    :type lat: float
    :param lon: The longitude to do a reverse lookup on
    :type lon: float

    :rtype: Reversed
    """
    return 'do some magic!'
