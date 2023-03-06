import connexion

from swagger_server.models.address import Address  # noqa: E501
from swagger_server.models.geocoded import Geocoded  # noqa: E501
from swagger_server.models.nena import NENA  # noqa: E501

from swagger_server.services.maps import search


def geocode_addr(body):  # noqa: E501
    """Get latitude and longitude from string containing address

    Provide an address and get back it&#x27;s latitude and longitude # noqa: E501

    :param body: String Address
    :type body: dict | bytes

    :rtype: Geocoded
    """
    if connexion.request.is_json:
        body = Address.from_dict(connexion.request.get_json())  # noqa: E501

    res = search.search_query(body.address)

    return res, res['result']


def geocode_nena(body):  # noqa: E501
    """Get latitude and longitude from NENA formatted address

    Provide a NENA formatted address and get back it&#x27;s latitude and longitude # noqa: E501

    :param body: NENA formatted address
    :type body: dict | bytes

    :rtype: Geocoded
    """
    if connexion.request.is_json:
        body = NENA.from_dict(connexion.request.get_json())  # noqa: E501

    res = search.search_nena(body)

    return res, res['result']
