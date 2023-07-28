from dataclasses import asdict

from rapid7.endpoints.structures import (
    Assignee,
    SearchObject,
    SortObject,
)
from rapid7.lib.checks import check_optional_parameters


def list_investigations_v1(self, end_time : str = None, index : int = None,
                                 size : int = None, start_time : str = None,
                                 statuses : str = None) -> dict:
    """ Get investigations
    
    GET /v1/investigations

    https://help.rapid7.com/insightidr/en-us/api/v1/docs.html#tag/Investigations/operation/listInvestigations

    """
    
    method = "GET"
    url = "/v1/investigations"

    params = {"end_time" : end_time, "index" : index, "size" : size,
              "start_time" : start_time, "statuses" : statuses}
    
    params = check_optional_parameters(params)

    return self.request(method = method, url = url, params = params)


def list_investigations_v2(self, assignee_email : str = None, end_time : str = None,
                                 index : int = None, multi_customer : bool = None,
                                 priorities : str = None, size : int = None,
                                 sort : str = None, sources : str = None,
                                 start_time : str = None, statuses : str = None,
                                 tags : str = None) -> dict:
    """ Get investigations
    
    GET /v2/investigations

    https://help.rapid7.com/insightidr/en-us/api/v2/docs.html#tag/Investigations/operation/listInvestigations

    """
    
    method = "GET"
    url = "/v2/investigations"

    params = {"assignee_email" : assignee_email, "end_time" : end_time,
              "index" : index, "multi-customer" : multi_customer, 
              "priorities" : priorities, "size" : size,
              "sort" : sort, "sources" : sources,
              "start_time" : start_time, "statuses" : statuses,
              "tags" : tags}
    
    params = check_optional_parameters(params)

    # This API is in preview mode and may change behavior at any time.
    # We have to specify investigations-preview in an Accept-version header to access this API.
    temp_headers = {"Accept-version" : "investigations-preview"}
    data = self.request_with_temp_headers(method = method, url = url, params = params, temp_headers = temp_headers)

    return data


def close_investigations_in_bulk_v1(self, source : str, start_timestamp : str, end_timestamp : str,
                                          alert_type : str = None, detection_rule_rrn : str = None, max_investigations_to_close : int = None) -> dict:
    """ Close investigations in bulk

    POST /v1/investigations/bulk_close

    https://help.rapid7.com/insightidr/en-us/api/v1/docs.html#tag/Investigations/operation/bulkCloseInvestigations

    alert_type is required i the source is ALERT
    
    """
    
    method = "POST"
    url = "/v1/investigations/bulk_close"
    payload = {"source" : source, "from" : start_timestamp, "to" : end_timestamp,
              "alert_type" : alert_type, "detection_rule_rrn" : detection_rule_rrn,
              "max_investigations_to_close" : max_investigations_to_close}
    
    payload = check_optional_parameters(payload)
    
    return self.request(method = method, url = url, data = payload)


def close_investigations_in_bulk_v2(self, source : str, start_timestamp : str, end_timestamp : str,
                                          alert_type : str = None, detection_rule_rrn : str = None, max_investigations_to_close : int = None) -> dict:
    """ Close investigations in bulk

    POST /v2/investigations/bulk_close

    https://help.rapid7.com/insightidr/en-us/api/v2/docs.html#tag/Investigations/operation/bulkCloseInvestigations

    alert_type is required i the source is ALERT
    
    """

    method = "POST"
    url = "/v2/investigations/bulk_close"

    payload = {"source" : source, "from" : start_timestamp, "to" : end_timestamp,
              "alert_type" : alert_type, "detection_rule_rrn" : detection_rule_rrn,
              "max_investigations_to_close" : max_investigations_to_close}
    
    payload = check_optional_parameters(payload)
    
    # This API is in preview mode and may change behavior at any time.
    # We have to specify investigations-preview in an Accept-version header to access this API.
    temp_headers = {"Accept-version" : "investigations-preview"}
    data = self.request_with_temp_headers(method = method, url = url, data = payload, temp_headers = temp_headers)

    return data


def assign_user_to_investigation(self, id : str, user_email_address : str) -> dict:
    """ Assign user to investigation

    PUT /v1/investigations/[id]/assignee

    https://help.rapid7.com/insightidr/en-us/api/v1/docs.html#tag/Investigations/operation/assignUserToInvestigation
    
    """

    method = "PUT"
    url = f"/v1/investigations/{id}/assignee"

    payload = {"user_email_address" : user_email_address}
    
    data = self.request(method = method, url = url, data = payload)
    
    return data


def set_investigation_status_v1(self, id : str, status : str) -> dict:
    """ Set investigation status
    
    PUT /v1/investigations/[id]/status/[status]

    https://help.rapid7.com/insightidr/en-us/api/v1/docs.html#tag/Investigations/operation/setStatus
    
    """
    
    method = "PUT"
    url = f"/v1/investigations/{id}/status/{status}"

    return self.request(method = method, url = url)


def set_investigation_status_v2(self, id : str, status : str, multi_customer : bool = None,
                                      disposition : str = None, threat_command_close_reason : str = None,
                                      threat_command_free_text : str = None) -> dict:
    """ Set investigation status
    
    PUT /v2/investigations/[id]/status/[status]

    https://help.rapid7.com/insightidr/en-us/api/v2/docs.html#tag/Investigations/operation/setStatus

    """

    method = "PUT"
    url = f"/v2/investigations/{id}/status/{status}"
    params = {"multi-customer" : multi_customer}
    payload = {"disposition" : disposition,
               "threat_command_close_reason" : threat_command_close_reason,
               "threat_command_free_text" : threat_command_free_text}
    
    params = check_optional_parameters(params)
    payload = check_optional_parameters(payload)

    # This API is in preview mode and may change behavior at any time.
    # We have to specify investigations-preview in an Accept-version header to access this API.
    temp_headers = {"Accept-version" : "investigations-preview"}
    data = self.request_with_temp_headers(method = method, url = url, params = params, data = payload, temp_headers = temp_headers)

    return data


def create_investigation(self, title : str, assignee : Assignee = None,
                               disposition : str = None, priority : str = None,
                               status : str = None) -> dict:
    """ Create investigation
    
    POST /v2/investigations

    https://help.rapid7.com/insightidr/en-us/api/v2/docs.html#tag/Investigations/operation/createInvestigation
    
    """

    method = "POST"
    url = "/v2/investigations"

    payload = {"title" : title, "assignee" : assignee, "disposition" : disposition,
               "priority" : priority, "status" : status}
    
    payload = check_optional_parameters(payload)
    
    # This API is in preview mode and may change behavior at any time.
    # We have to specify investigations-preview in an Accept-version header to access this API.
    temp_headers = {"Accept-version" : "investigations-preview"}
    data = self.request_with_temp_headers(method = method, url = url, data = payload, temp_headers = temp_headers)

    return data


def search_investigations(self, index : int = None, multi_customer : bool = None,
                                size : int = None, end_time : str = None,
                                search : list[SearchObject] = None, sort : list[SortObject] = None,
                                start_time : str = None) -> dict:
    """ Search investigations

    POST /v2/investigations/_search

    https://help.rapid7.com/insightidr/en-us/api/v2/docs.html#tag/Investigations/operation/searchInvestigations

    """

    method = "POST"
    url = "/v2/investigations/_search"

    # Cast dataclasses to dictionaries
    for index, elem in enumerate(search):
        search[index] = asdict(elem)

    for index, elem in enumerate(sort):
        sort[index] = asdict(elem)

    index = None

    params = {"index" : index, "multi-customer" : multi_customer, "size" : size}
    payload = {"end_time" : end_time, "search" : search, "sort" : sort, "start_time" : start_time}
    
    params = check_optional_parameters(params)
    payload = check_optional_parameters(payload)

    # This API is in preview mode and may change behavior at any time.
    # We have to specify investigations-preview in an Accept-version header to access this API.
    temp_headers = {"Accept-version" : "investigations-preview"}
    data = self.request_with_temp_headers(method = method, url = url, params = params, data = payload, temp_headers = temp_headers)

    return data


def list_alerts_associated_with_investigation(self, identifier : str, index : int = None,
                                                    multi_customer : bool = None, size : int = None) -> dict:
    """ List alerts associated with the specified investigation

    GET /v2/investigations/[identifier]/alerts

    https://help.rapid7.com/insightidr/en-us/api/v2/docs.html#tag/Investigations/operation/listInvestigationAlerts

    """

    method = "GET"
    url = f"/v2/investigations/{identifier}/alerts"
    params = {"index" : index, "multi-customer" : multi_customer, "size" : size}

    params = check_optional_parameters(params)
    
    # This API is in preview mode and may change behavior at any time.
    # We have to specify investigations-preview in an Accept-version header to access this API.
    temp_headers = {"Accept-version" : "investigations-preview"}
    data = self.request_with_temp_headers(method = method, url = url, params = params, temp_headers = temp_headers)

    return data


def get_rapid7_product_alerts_associated_with_investigation(self, identifier : str,
                                                                  multi_customer : bool = None) -> dict:
    """ Get a list of Rapid7 product alerts associated with the specified investigation

    GET /v2/investigations/[identifier]/rapid7-product-alerts

    https://help.rapid7.com/insightidr/en-us/api/v2/docs.html#tag/Investigations/operation/getInvestigationRapid7ProductAlertInfo

    """

    method = "GET"
    url = f"/v2/investigations/{identifier}/rapid7-product-alerts"
    params = {"multi-customer" : multi_customer}

    params = check_optional_parameters(params)
    
    # This API is in preview mode and may change behavior at any time.
    # We have to specify investigations-preview in an Accept-version header to access this API.
    temp_headers = {"Accept-version" : "investigations-preview"}
    data = self.request_with_temp_headers(method = method, url = url, params = params, temp_headers = temp_headers)

    return data


def get_investigation(self, id : str, multi_customer : bool = None) -> dict:
    """ Get investigation details
    
    GET /v2/investigations/[id]

    https://help.rapid7.com/insightidr/en-us/api/v2/docs.html#tag/Investigations/operation/getInvestigationById

    """

    method = "GET"
    url = f"/v2/investigations/{id}"
    params = {"multi-customer" : multi_customer}

    params = check_optional_parameters(params)
    
    # This API is in preview mode and may change behavior at any time.
    # We have to specify investigations-preview in an Accept-version header to access this API.
    temp_headers = {"Accept-version" : "investigations-preview"}
    data = self.request_with_temp_headers(method = method, url = url, params = params, temp_headers = temp_headers)

    return data


def update_investigation(self, id : str, multi_customer : bool = None, assignee : Assignee = None,
                               disposition : str = None, priority : str = None, status : str = None,
                               threat_command_close_reason : str = None, threat_command_free_text : str = None,
                               title :str = None) -> dict:
    """ Update investigation
    
    PATCH /v2/investigations/[id]

    https://help.rapid7.com/insightidr/en-us/api/v2/docs.html#tag/Investigations/operation/updateInvestigation
    
    """

    method = "PATCH"
    url = f"/v2/investigations/{id}"

    if assignee is not None:
        assignee = asdict(assignee)

    params = {"multi-customer" : multi_customer}
    payload = {"assignee" : assignee, "disposition" : disposition,
               "priority" : priority, "status" : status,
               "threat_command_close_reason" : threat_command_close_reason,
               "threat_command_free_text" : threat_command_free_text,
               "title" : title}
    
    params = check_optional_parameters(params)
    payload = check_optional_parameters(payload)

    # This API is in preview mode and may change behavior at any time.
    # We have to specify investigations-preview in an Accept-version header to access this API.
    temp_headers = {"Accept-version" : "investigations-preview"}
    data = self.request_with_temp_headers(method = method, url = url, params = params, data = payload, temp_headers = temp_headers)

    return data


def assign_user_to_investigation(self, id : str, user_email_address : str, multi_customer : bool = None) -> dict:
    """ Assign user to investigation
    
    PUT /v2/investigations/[id]/assignee

    https://help.rapid7.com/insightidr/en-us/api/v2/docs.html#tag/Investigations/operation/assignUserToInvestigation

    """

    method = "PUT"
    url = f"/v2/investigations/{id}/assignee"
    params = {"multi-customer" : multi_customer}
    payload = {"user_email_address" : user_email_address}

    params = check_optional_parameters(params)
    payload = check_optional_parameters(payload)

    # This API is in preview mode and may change behavior at any time.
    # We have to specify investigations-preview in an Accept-version header to access this API.
    temp_headers = {"Accept-version" : "investigations-preview"}
    data = self.request_with_temp_headers(method = method, url = url, params = params, data = payload, temp_headers = temp_headers)

    return data


def set_investigation_disposition(self, disposition : str, id : str, multi_customer : bool = None) -> dict:
    """ Set the disposition of an investigation
    
    PUT /v2/investigations/[id]/disposition/[disposition]
    
    https://help.rapid7.com/insightidr/en-us/api/v2/docs.html#tag/Investigations/operation/setDisposition
    
    """

    method = "PUT"
    url = f"/v2/investigations/{id}/disposition/{disposition}"
    params = {"multi-customer" : multi_customer}

    params = check_optional_parameters(params)

    # This API is in preview mode and may change behavior at any time.
    # We have to specify investigations-preview in an Accept-version header to access this API.
    temp_headers = {"Accept-version" : "investigations-preview"}
    data = self.request_with_temp_headers(method = method, url = url, params = params, temp_headers = temp_headers)

    return data


def set_investigation_priority(self, id : str, priority : str, multi_customer : bool = None) -> dict:
    """ Set the priority of an investigation
    
    PUT /v2/investigations/[id]/priority/[priority]

    https://help.rapid7.com/insightidr/en-us/api/v2/docs.html#tag/Investigations/operation/setPriority
    
    """

    method = "PUT"
    url = f"/v2/investigations/{id}/priority/{priority}"
    params = {"multi-customer" : multi_customer}

    params = check_optional_parameters(params)

    # This API is in preview mode and may change behavior at any time.
    # We have to specify investigations-preview in an Accept-version header to access this API.
    temp_headers = {"Accept-version" : "investigations-preview"}
    data = self.request_with_temp_headers(method = method, url = url, params = params, temp_headers = temp_headers)

    return data


