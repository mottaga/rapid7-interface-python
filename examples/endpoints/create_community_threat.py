import sys
sys.path[0] = "/path/to/rapid7/package" # to be removed (use only if the package is not installed)

from rapid7.endpoints.endpoint import Endpoint
from rapid7.endpoints.structures import Indicators, CommunityThreat
from examples.utils.load_api_key import get_api_key


api_key = get_api_key("")
region = ""

endpoints_v1 = Endpoint(api_key = api_key, region = region)

indicators = Indicators(ips = ["192.168.0.1"], hashes = [], domain_names = [], urls = [])
community_threat = CommunityThreat(threat = "threat_test", note = "note_test", indicators = indicators)

print(endpoints_v1.create_community_threat(community_threat))
