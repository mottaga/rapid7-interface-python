from dataclasses import asdict

from rapid7.endpoints.structures import SearchObject, SortObject
from rapid7.lib.checks import check_optional_parameters



def search_user(self, search : list[SearchObject], sort : list[SortObject], 
                      index : int = None, size : int = None) -> dict:
    """ Search user
    
    POST /v1/users/_search

    https://help.rapid7.com/insightidr/en-us/api/v1/docs.html#tag/Users/operation/searchUsers

    """
    
    method = "POST"
    url = "/v1/users/_search"
    
    # Cast dataclasses to dictionaries
    for index, elem in enumerate(search):
        search[index] = asdict(elem)

    for index, elem in enumerate(sort):
        sort[index] = asdict(elem)

    index = None
    
    params = {"index" : index, "size" : size}
    payload = {"search" : search, "sort" : sort}
    
    params = check_optional_parameters(params)
    
    # This API is in preview mode and may change behavior at any time.
    # We have to specify strong-force-preview in an Accept-version header to access this API.
    temp_headers = {"Accept-version" : "strong-force-preview"}
    data = self.request_with_temp_headers(method = method, url = url, params = params, data = payload, temp_headers = temp_headers)

    return data


def get_user_by_rrn(self, rrn : str) -> dict:
    """ Get user by rrn
    
    GET /v1/users/[rrn]

    https://help.rapid7.com/insightidr/en-us/api/v1/docs.html#tag/Users/operation/getUserByRrn

    """

    method = "GET"
    url = f"/v1/users/{rrn}"

    # This API is in preview mode and may change behavior at any time.
    # We have to specify strong-force-preview in an Accept-version header to access this API.
    temp_headers = {"Accept-version" : "strong-force-preview"}
    data = self.request_with_temp_headers(method = method, url = url, temp_headers = temp_headers)

    return data