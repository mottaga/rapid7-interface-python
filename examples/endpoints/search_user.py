import sys
sys.path[0] = "/path/to/rapid7/package" # to be removed (use only if the package is not installed)

from rapid7.endpoints.endpoint import Endpoint
from rapid7.endpoints._accounts import SortObject, SearchObject
from examples.utils.load_api_key import get_api_key


api_key = get_api_key("")
region = ""

endpoints_v1 = Endpoint(api_key = api_key, region = region)

sort = SortObject(field = "name", order = "ASC")
search = SearchObject(field = "name", operator = "EQUALS", value = "")

print(endpoints_v1.search_user([search], [sort], size = 1))