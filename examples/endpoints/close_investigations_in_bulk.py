import sys
sys.path[0] = "/path/to/rapid7/package" # to be removed (use only if the package is not installed)

from rapid7.endpoints.endpoint import Endpoint
from examples.utils.load_api_key import get_api_key


api_key = get_api_key("")
region = ""

endpoints_v1 = Endpoint(api_key = api_key, region = region)

source = "ALERT"
start_timestamp = ""
end_timestamp = ""
alert_type = ""

investigations = endpoints_v1.close_investigations_in_bulk_v1(source, start_timestamp, end_timestamp, alert_type = alert_type)

print(investigations)