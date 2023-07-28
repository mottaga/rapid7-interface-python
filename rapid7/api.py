import requests
import json

from .__version__ import __version__


class API():
    def __init__(self, api_key : str, region : str) -> None:
        self.API_KEY = api_key
        
        self.BASE_URL = f"https://{region}.api.insight.rapid7.com/idr/"
        self.ALLOWED_METHODS = ["GET", "POST", "PUT", "DELETE", "PATCH"]

        self.session = requests.Session()
        self.session.headers.update(
            {
                "Content-Type" : "application/json;charset=utf-8",
                "User-Agent" : f"rapid7-interface-python/{__version__}",
                "X-API-Key" : api_key,
            }
        )

        return
    

    #
    # Perform an API request checking only the method,
    # if an error is raised from the server just return the error string.
    #
    def request(self, method : str, url : str, params : dict = None, data : dict = None) -> dict | str:
        if not self._check_method(method):
            return f"Invalid method {method}, use {self.ALLOWED_METHODS}."
        
        data = json.dumps(data)
        response = self.session.request(method = method, url = f"{self.BASE_URL}/{url}", params = params, data = data)

        try:
            return response.json()
        
        except ValueError:
            return response.text
        
    
    #
    # Perform an API request checking only the method,
    # if an error is raised from the server just return the error string.
    # Set a temporary header
    #
    def request_with_temp_headers(self, method : str, url : str, temp_headers : dict, params : dict = None, data : dict = None) -> dict | str:
        # Set header
        self.session.headers.update(temp_headers)

        # Perform request
        data = self.request(method = method, url = url, params = params, data = data)

        # Remove header
        for key in temp_headers:
            del self.session.headers[key]

        return data
        
    
    #
    # Check the request method using [self.ALLOWED_METHODS]
    #
    def _check_method(self, method : str) -> bool:
        if method not in self.ALLOWED_METHODS:
            return False
        
        return True

        