from rapid7.webclient import WebClient

class WebEndpoint(WebClient):
    def __init__(self, session_cookie : str,  csrf_token : str,
                       org_token : str, region : str) -> None:
        
        super().__init__(session_cookie, csrf_token, org_token, region)
        return
    

    # INVESTIGATIONS
    from rapid7.webendpoints._investigations import get_investigation_details