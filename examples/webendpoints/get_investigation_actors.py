import sys
sys.path[0] = "/path/to/rapid7/package" # to be removed (use only if the package is not installed)

from rapid7.webendpoints.webendpoint import WebEndpoint
from examples.utils.load_credentials import get_credentials
from examples.utils.print_json import print_json


credentials = get_credentials("")

region = ""

webendpoint = WebEndpoint(credentials["username"], credentials["password"],
                           credentials["org_token"], region)

investigation_id = ""

data = webendpoint.get_investigation_details(investigation_id)

actors = []
for item in data["items"]:
    if "actor" in item["item"]:
        actor = {"name" : item["item"]["actor"]["name"],
                 "type" : item["item"]["actor"]["type"],
                 "domain" : item["item"]["actor"].get("domain", ""),
                 "sourceAsset" : item["item"].get("sourceAsset", ""),
                 "destAsset" : item["item"].get("destAsset", ""),
                 }
        actors.append(actor)

for actor in actors:
    print_json(actor)
