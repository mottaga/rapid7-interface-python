import sys
sys.path[0] = "/path/to/rapid7/package" # to be removed (use only if the package is not installed)

from rapid7.endpoints.endpoint import Endpoint
from examples.utils.load_api_key import get_api_key


api_key = get_api_key("")
region = ""

endpoints_v1 = Endpoint(api_key = api_key, region = region)

investigation_id = ""
status = "CLOSED"

investigation = endpoints_v1.set_investigation_status_v1(investigation_id, status)

print(investigation)