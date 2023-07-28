def get_credentials(credentials_path : str) -> dict:
    with open(credentials_path, "r") as fd:
        credentials = fd.read().strip()
    
    credentials = credentials.split(":")
    credentials = {
        "username" : credentials[0],
        "password" : credentials[1],
        "org_token" : credentials[2],
    }

    return credentials