"""
grey Request/Response Utils
"""
import json, urlparse

from grey.error import MissingField, InvalidJSON

def mongo_callback(req):
    def decorator(func):
        def wrapper(result, error):
            if error:
                req.respond("Mongo Error " + error, code = 500)
                return
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
            except KeyError:
                raise MissingField(item)
            func(_self, *args)
        return wrapper
    return decorator

def form_urlencoded_parse(body):
    """
    Parse x-www-form-url encoded data
    """
    try:
        data = urlparse.parse_qs(body, strict_parsing=True)
        for key in data:
            data[key] = data[key][0]
        return data
    except ValueError:
        raise InvalidJSON()

def smart_parse(body):
    """
    Handle json, fall back to x-www-form-urlencoded
    """
    try:
        data_dict = json.loads(body)
    except ValueError:
        return form_urlencoded_parse(body)
    return data_dict
