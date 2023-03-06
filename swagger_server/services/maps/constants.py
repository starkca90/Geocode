API_SOURCE = "geocoder_maps"
API_URL = "https://geocode.maps.co"

SEARCH_PATH = API_URL + "/search?"
SEARCH_QUERY = SEARCH_PATH + "q={{query}}"
SEARCH_NENA = SEARCH_PATH + "street={{street}}&city={{city}}&state={{state}}&postalcode={{postal}}&county={{county}}"

REVERSE_PATH = API_URL + "/reverse?"
REVERSE_QUERY = REVERSE_PATH + "lat={{latitude}}&lon={{longitude}}"
