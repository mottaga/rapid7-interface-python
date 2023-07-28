import sys
sys.path[0] = "/path/to/rapid7/package" # to be removed (use only if the package is not installed)

from rapid7.webendpoints.webendpoint import WebEndpoint
from examples.utils.load_credentials import get_credentials

credentials = get_credentials("")

region = ""

webendpoint = WebEndpoint(credentials["username"], credentials["password"],
                           credentials["org_token"], region)

investigation_id = ""

print(webendpoint.get_investigation_details(investigation_id))