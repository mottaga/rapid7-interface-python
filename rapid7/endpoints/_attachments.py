from rapid7.lib.checks import check_optional_parameters


def list_attachments(self, target : str, index : int = None, size : int = None) -> dict:
    """ List attachments
    
    GET /v1/attachments

    https://help.rapid7.com/insightidr/en-us/api/v1/docs.html#tag/Attachments/operation/listAttachments

    """

    method = "GET"
    url = "/v1/attachments"
    params = {"target" : target, "index" : index, "size" : size}

    params = check_optional_parameters(params)

    # This API is in preview mode and may change behavior at any time.
    # We have to specify strong-force-preview in an Accept-version header to access this API.
    temp_headers = {"Accept-version" : "strong-force-preview"}
    data = self.request_with_temp_headers(method = method, url = url, params = params, temp_headers = temp_headers)

    return data


def upload_attachments(self, paths : list[str]) -> dict:
    """ Upload attachments

    POST /v1/attachments

    https://help.rapid7.com/insightidr/en-us/api/v1/docs.html#tag/Attachments/operation/uploadAttachment

    """

    method = "POST"
    url = "/v1/attachments"
    payload = {"filedata" : [open(filepath, "rb") for filepath in paths]}

    # Set content type for this type of request
    self.session.headers.update(
        {
            "Contenty-Type" : "application/x-www-form-urlencoded;charset=utf-8"
        }
    )

    # This API is in preview mode and may change behavior at any time.
    # We have to specify strong-force-preview in an Accept-version header to access this API.
    temp_headers = {"Accept-version" : "strong-force-preview"}
    data = self.request_with_temp_headers(method = method, url = url, data = payload, temp_headers = temp_headers)

    self.session.headers.update(
        {
            "Contenty-Type" : "application/json;charset=utf-8"
        }
    )

    return data


def download_attachment(self, rrn : str) -> dict:
    """ Download attachment

    GET /v1/attachments/[rrn]

    https://help.rapid7.com/insightidr/en-us/api/v1/docs.html#tag/Attachments/operation/downloadAttachment

    """

    method = "GET"
    url = f"/v1/attachments/{rrn}"

    return self.request(method = method, url = url)


def delete_attachment(self, rrn : str) -> dict:
    """ Delete attachment

    DELETE /v1/attachments/[rrn]

    https://help.rapid7.com/insightidr/en-us/api/v1/docs.html#tag/Attachments/operation/deleteAttachment

    """

    method = "DELETE"
    url = f"/v1/attachments/{rrn}"

    return self.request(method = method, url = url)


def get_attachment_information(self, rrn : str) -> dict:
    """ Get attachment information

    GET v1/attachments/[rrn]/metadata

    https://help.rapid7.com/insightidr/en-us/api/v1/docs.html#tag/Attachments/operation/getAttachment
    
    """

    method = "GET"
    url = f"/v1/attachments/{rrn}/metadata"

    return self.request(method = method, url = url)

