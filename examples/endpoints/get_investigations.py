import sys
sys.path[0] = "/path/to/rapid7/package" # to be removed (use only if the package is not installed)

from rapid7.endpoints.endpoint import Endpoint
from examples.utils.load_api_key import get_api_key


api_key = get_api_key("")
region = ""

endpoints_v1 = Endpoint(api_key = api_key, region = region)

investigations = endpoints_v1.list_investigations_v1()["data"]

for investigation in investigations:
    print(investigation)
    print()
