"""
Indico Request/Response Utils
"""
import json, urlparse, logging

from indico.error import MissingField, InvalidJSON, MongoError
from indico.error import IndicoError, WrongFieldType

LOGGER = logging.getLogger("indico")
def mongo_callback(req):
    def decorator(func):
        def wrapper(result, error):
            try:
                if error:
                    raise MongoError(error)
                func(result)
            except IndicoError as e:
                req.respond(e.message, e.code)
        return wrapper
    return decorator

def unpack(*arguments):
    """
    Unpack arguments to be used in methods wrapped
    """
    def decorator(func):
        def wrapper(_self, data, **kwargs):
            data = smart_parse(data)
            try:
                args = [data[item] for item in arguments]
            except KeyError:
                raise MissingField(item)

            kwargs["_arguments"] = arguments

            func(_self, *args, **kwargs)
        return wrapper
    return decorator

def type_check(*types):
    """
    Checks unpacked arguments for types
    """
    def decorator(func):
        def wrapper(_self, *args, **kwargs):
            for arg, _type, _arg in zip(args, types, kwargs.pop("_arguments")):
                if not isinstance(arg, _type):
                    if _type is str and isinstance(arg, unicode):
                        continue
                    raise WrongFieldType(_arg, arg, _type)
            func(_self, *args, **kwargs)
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
