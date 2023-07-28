import requests
import json
from bs4 import BeautifulSoup
from http.cookiejar import CookieJar

from .__version__ import __version__


class WebClient():
    def __init__(self, username : str,  password : str,
                       org_token : str, region : str) -> None:
        
        self.USERNAME = username
        self.PASSWORD = password
        self.ORG_TOKEN = org_token
        self.REGION = region
        
        auth_data = self._authentication(username, password)

        self.IPIMS_SESSION_COOKIE = auth_data["IPIMS_SESSION_COOKIE"]
        self.CSRF_TOKEN = auth_data["CSRF_TOKEN"]


        self.BASE_URL = f"https://{region}.razor-investigation-ui.insight.rapid7.com"
        self.ALLOWED_METHODS = ["POST"]

        self.session = requests.Session()
        self.session.headers.update(
            {
                "Contenty-Type" : "application/json;charset=utf-8",
                "User-Agent" : f"rapid7-interface-python/{__version__}",
                "X-CSRF-TOKEN": self.CSRF_TOKEN,
                "CSRFToken": self.CSRF_TOKEN,
                "X-ORGPRODUCT-TOKEN": org_token,
                "R7-Organization-Product-Token": org_token,
                "Cookie": f"IPIMS_SESSION={self.IPIMS_SESSION_COOKIE};",
            }
        )

        return
    

    #
    # Perform a request to get json data
    # from an API accessible through the web
    #
    def request(self, method : str, url : str, params : dict = None) -> dict | str:
        if not self._check_method(method):
            return f"Invalid method {method}, use {self.ALLOWED_METHODS}."
        
        url = f"{self.BASE_URL}{url}"
        response = self.session.request(method = method, url = url, params = params)

        try:
            return response.json()
        
        except ValueError:
            return response.text
        
    
    #
    # Refresh session cookie
    #
    def refresh_session_cookie(self) -> None:
        auth_data = self._authentication(self.USERNAME, self.PASSWORD)

        self.IPIMS_SESSION_COOKIE = auth_data["IPIMS_SESSION_COOKIE"]
        self.CSRF_TOKEN = auth_data["CSRF_TOKEN"]

        self.session.headers["X-CSRF-TOKEN"] = self.CSRF_TOKEN
        self.session.headers["CSRFToken"] = self.CSRF_TOKEN
        self.session.headers["Cookie"] = f"IPIMS_SESSION={self.IPIMS_SESSION_COOKIE};"

        return
    

    #
    # Check the request method using [self.ALLOWED_METHODS]
    #
    def _check_method(self, method : str) -> bool:
        if method not in self.ALLOWED_METHODS:
            return False
        
        return True
    

    #
    # Get ipims_session cookie and csrf_token
    #
    def _authentication(self, username : str, password : str) -> dict:
        dt_cookie = self._get_dt_cookie()
        session_token = self._get_session_token(dt_cookie, username, password)
        sid_cookie = self._get_sid_cookie(dt_cookie, session_token)
        login_payload = self._get_login_payload(dt_cookie, sid_cookie)

        return self._get_auth_data(login_payload)
        

    #
    # Get dt_cookie from response cookies
    #
    def _get_dt_cookie(self) -> str:
        url = "https://rapid7ipimseu.okta-emea.com/api/v1/authn"
        resp = requests.options(url = url)

        return self._extract_cookie("DT", resp.cookies)
    
    
    #
    # Get session_token from response data
    #
    def _get_session_token(self, dt_cookie : str, username : str, password : str) -> str:
        url = "https://rapid7ipimseu.okta-emea.com/api/v1/authn"

        headers = {
                "Accept" : "application/json",
                "Content-Type" : "application/json",
                }
        
        cookies = {"DT" : dt_cookie}

        data = json.dumps(
            {
                "password" : password,
                "username" : username,
                "options": {
                    "warnBeforePasswordExpired":"true",
                    "multiOptionalFactorEnroll":"true",
                    }
            }
        )

        resp = requests.post(url = url, headers = headers, cookies = cookies, data = data)
        
        return resp.json()["sessionToken"]
    

    #
    # Get sid_cookie from response cookies
    #
    def _get_sid_cookie(self, dt_cookie : str, session_token : str) -> str:
        url = "https://rapid7ipimseu.okta-emea.com/login/sessionCookieRedirect?" \
              f"checkAccountSetupComplete=true&token={session_token}&" \
              "redirectUrl=https://rapid7ipimseu.okta-emea.com/home/template_saml_2_0/0oatgdg8ruitg9ZTr0i6/3079"
        
        cookies = {"DT" : dt_cookie}

        resp = requests.get(url = url, cookies = cookies, allow_redirects = True)

        return self._extract_cookie("sid", resp.cookies)
    
    
    #
    # Get RelayState and SAMLResponse contained
    # in two hidde input fields
    #
    def _get_login_payload(self, dt_cookie : str, sid_cookie : str) -> dict:
        url = "	https://rapid7ipimseu.okta-emea.com/app/template_saml_2_0/exktgdg8qiL1JmBvC0i6/sso/saml"

        cookies = {"DT" : dt_cookie, "sid" : sid_cookie}

        resp = requests.get(url = url, cookies = cookies)

        # Extract login payload
        soup = BeautifulSoup(resp.content, "html.parser")
        relay_state = soup.find("input", {"name" : "RelayState"})["value"]
        saml_response = soup.find("input", {"name" : "SAMLResponse"})["value"]

        return {"RelayState" : relay_state, "SAMLResponse" : saml_response}
    
    
    #
    # Get IPIMS_SESSION_COOKIE AND CSRF_TOKEN
    #
    def _get_auth_data(self, login_payload : dict) -> dict:
        url = "https://insight.rapid7.com/saml/SSO"

        resp = requests.post(url = url, data = login_payload, allow_redirects = True)

        # Extract csrf_token from last redirect
        soup = BeautifulSoup(resp.content, "html.parser")
        window_options = soup.find_all("script")[2].text.replace("\n", "").replace(" ", "")
        window_options = window_options[15 : len(window_options) - 1]
        window_options = json.loads(window_options)
        csrf_token = window_options["csrfToken"]

        # Extract ipims session cookie from first redirect    
        ipims_cookie = ""
        cookies = resp.history[0].headers["Set-Cookie"].split(" ")
        for cookie in cookies:
            if cookie.startswith("IPIMS_SESSION"):
                ipims_cookie = cookie.replace("IPIMS_SESSION=", "")
                ipims_cookie = ipims_cookie[:-1]

        return {"CSRF_TOKEN" : csrf_token, "IPIMS_SESSION_COOKIE" : ipims_cookie}

    
    #
    # Extract cookie from CookieJar by name
    #
    def _extract_cookie(self, name : str, cookies : CookieJar) -> str:
        for cookie in cookies:
            if cookie.name == name:
                return cookie.value



