def get_api_key(api_key_path : str) -> str:
    with open(api_key_path, "r") as fd:
        return fd.read().strip()
    
    