def check_optional_parameters(params : dict) -> dict:
    # Clear optional values that are not given by the user
    for param in dict(params):
        if params[param] is None:
            del params[param]
    
    return params