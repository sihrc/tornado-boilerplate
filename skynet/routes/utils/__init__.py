"""
SkyNet Request/Response Utils
"""
import json, urlparse

def mongo_callback(req):
    def decorator(func):
        def wrapper(result, error):
            if error:
                req.respond("Mongo Error " + error, code = 500)
            func(result)
        return wrapper
    return decorator

def unpack(arguments = []):
    """
    Unpack arguments to be used in methods wrapped
    """
    def decorator(func):
        def wrapper(_self, data):
            data = smart_parse(data)
            try:
                args = [data[item] for item in arguments]
            except AttributeError:
                return 400, "%s field was not provided" % item
            return func(_self, *args)
        return wrapper
    return decorator

def form_urlencoded_parse(body):
    """
    Parse x-www-form-url encoded data
    """
    try:
        data = urlparse.parse_qs(body)
        if not data:
            raise ParseError("No JSON object could be decoded")
        for key in data:
            data[key] = data[key][0]
        return data
    except ValueError:
        raise ParseError("No JSON object could be decoded.")


def smart_parse(body):
    """
    Handle json, fall back to x-www-form-urlencoded
    """
    try:
        data_dict = json.loads(body)
        if not isinstance(data_dict, dict):
            raise ParseError('Input must be JSON dictionary')
        return data_dict
    except ValueError:
        return form_urlencoded_parse(body)
