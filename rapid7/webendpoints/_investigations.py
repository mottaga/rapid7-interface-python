import json

def get_investigation_details(self, id : str) -> dict:
    """ Get investigation details

    POST /api/1/investigations/[id]

    """

    method = "POST"
    url = f"/api/1/investigations/{id}"
    
    # Set headers
    self.session.headers.update(
        {
            "Host": "eu.razor-investigation-ui.insight.rapid7.com",
            "Referer": f"https://eu.idr.insight.rapid7.com/op/{self.ORG_TOKEN}",
            "Origin": "https://eu.idr.insight.rapid7.com",
        }
    )

    data = self.request(method = method, url = url)
    
    # Clear headers for next request
    del self.session.headers["host"]
    del self.session.headers["Referer"]
    del self.session.headers["Origin"]
    
    data = data.removeprefix("while(true){alert('Warning XSS attack');} &&&NOXSS&&&")
    data = json.loads(data)
    
    return data

