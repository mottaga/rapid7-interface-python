from rapid7.lib.checks import check_optional_parameters


def list_comments(self, target : str, index : int = None, size : int = None) -> dict:
    """ List comments
    
    GET /v1/comments

    https://help.rapid7.com/insightidr/en-us/api/v1/docs.html#tag/Comments/operation/listComments

    """

    method = "GET"
    url = "/v1/comments"
    params = {"target" : target, "index" : index, "size" : size}

    params = check_optional_parameters(params)

    # This API is in preview mode and may change behavior at any time.
    # We have to specify strong-force-preview in an Accept-version header to access this API.
    temp_headers = {"Accept-version" : "strong-force-preview"}
    data = self.request_with_temp_headers(method = method, url = url, params = params, temp_headers = temp_headers)

    return data


def create_comment(self, target : str, attachments : list[str] = None, body : str = None) -> dict:
    """ Create comment
    
    POST /v1/comments

    https://help.rapid7.com/insightidr/en-us/api/v1/docs.html#tag/Comments/operation/createComment

    """

    method = "POST"
    url = "/v1/comments"
    payload = {"target" : target, "attachments" : attachments, "body" : body}

    payload = check_optional_parameters(payload)

    # This API is in preview mode and may change behavior at any time.
    # We have to specify strong-force-preview in an Accept-version header to access this API.
    temp_headers = {"Accept-version" : "strong-force-preview"}
    data = self.request_with_temp_headers(method = method, url = url, data = payload, temp_headers = temp_headers)

    return data


def delete_comment(self, rrn : str) -> dict:
    """ Delete comment

    DELETE /v1/comments/[rrn]

    https://help.rapid7.com/insightidr/en-us/api/v1/docs.html#tag/Comments/operation/deleteComment

    """

    method = "DELETE"
    url = f"/v1/comments/{rrn}"

    return self.request(method = method, url = url)
