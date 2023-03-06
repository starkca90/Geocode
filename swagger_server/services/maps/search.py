import chevron
import json
import requests

from swagger_server.services.maps import constants


def __format_return(result_template: dict, request_result: str) -> dict:
    request_dict = json.loads(request_result)

    if request_dict.__len__() > 0:
        # Got a result, bundle it up
        result_template['result'] = 200
        result_template['lat'] = request_dict[0]['lat']
        result_template['lon'] = request_dict[0]['lon']
        result_template['bounds'] = request_dict[0]['boundingbox']
    else:
        # Didn't get a result
        result_template['result'] = 404

    return result_template


def search_query(address: str) -> dict:
    """
    Queries maps.co to obtain latitude and longitude of given address

    Query must have spaces replaced with '+' (does not work with %20)

    :parameter
    query : str
        The address to attempt to resolve
    :returns
    dict
        Results from the query
        Will always contain source and result
    """
    result = {'source': constants.API_SOURCE}

    sanitized_address = address.replace(' ', '+')

    request_res = requests.get(chevron.render(constants.SEARCH_QUERY, {'query': sanitized_address}))

    return __format_return(result, request_res.text)


def search_nena(nena: dict) -> dict:
    """
    Queries maps.co to obtain latitude and longitude of given address

    Query must have spaces replaced with '+' (does not work with %20)

    :parameter
    nena : dict
        NENA information of desired location
    :returns
    dict
        Results from the query
        Will always contain source and result
    """
    result = {'source': constants.API_SOURCE}

    # Need to sanitize input to ensure spaces are +
    nena.street = ' '.join(filter(None,
                                  [nena.house_number, nena.house_number_suffix, nena.prefix_directional,
                                   nena.street_name, nena.street_suffix,
                                   nena.post_directional])).replace(' ', '+')
    nena.community_name = nena.community_name.replace(' ', '+')
    nena.state = nena.state.replace(' ', '+')
    nena.zip_code = nena.zip_code.replace(' ', '+')

    request_res = requests.get(chevron.render(constants.SEARCH_NENA, {'street': nena.street,
                                                                      'city': nena.community_name,
                                                                      'state': nena.state,
                                                                      'postal': nena.zip_code,
                                                                      'county': nena.country}))

    return __format_return(result, request_res.text)
