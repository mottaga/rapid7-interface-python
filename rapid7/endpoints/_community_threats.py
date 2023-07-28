from dataclasses import asdict

from rapid7.endpoints.structures import CommunityThreat, Indicators
from rapid7.lib.checks import check_optional_parameters



def create_community_threat(self, community_threat : CommunityThreat) -> dict:
    """ Create community threat
    
    POST /v1/customthreats

    https://help.rapid7.com/insightidr/en-us/api/v1/docs.html#tag/Community-Threats/operation/createCommunityThreat

    Atleast one indicator must be inserted
    
    """

    method = "POST"
    url = "/v1/customthreats"

    community_threat.indicators = asdict(community_threat.indicators)
    payload = asdict(community_threat)

    return self.request(method = method, url = url, data = payload)


def delete_community_threat(self, key : str, reason : str = None) -> dict:
    """ Delete community threat
    
    POST /v1/customthreats/key/[key]/delete
    
    https://help.rapid7.com/insightidr/en-us/api/v1/docs.html#tag/Community-Threats/operation/deleteCommunityThreat

    """

    method = "POST"
    url = f"/v1/customthreats/key/{key}/delete"
    payload = {"reason" : reason}

    payload = check_optional_parameters(payload)

    return self.request(method = method, url = url, data = payload)


def add_indicators_to_community_threat(self, key : str, format : str, indicators : Indicators) -> dict:
    """ Add indicators to existent community threat
    
    POST /v1/customthreats/key/[key]/indicators/add

    https://help.rapid7.com/insightidr/en-us/api/v1/docs.html#tag/Community-Threats/operation/addIndicators

    Atleast one indicator must be inserted
    
    """

    method = "POST"
    url = f"/v1/customthreats/key/{key}/indicators/add"

    params = {"format" : format}
    payload = asdict(indicators)

    return self.request(method = method, url = url, params = params, data = payload)


def replace_indicators_to_community_threat(self, key : str, format : str, indicators : Indicators) -> dict:
    """ Replace indicators to existent community threat
    
    POST /v1/customthreats/key/[key]/indicators/replace

    https://help.rapid7.com/insightidr/en-us/api/v1/docs.html#tag/Community-Threats/operation/replaceIndicators

    Atleast one indicator must be inserted
    
    """

    method = "POST"
    url = f"/v1/customthreats/key/{key}/indicators/replace"

    params = {"format" : format}
    payload = asdict(indicators)

    return self.request(method = method, url = url, params = params, data = payload)
