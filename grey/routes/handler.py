"""
grey Request Handler
"""
import json
from bson.objectid import ObjectId

import tornado.web

from grey.routes.utils.auth_utils import user_hash
from grey.error import GreyError, RouteNotFound

class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)

class GreyHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    def post(self, action):
        try:
            # Fetch appropriate handler
            handler = getattr(self, str(action))

            # Pass along the data and get a result
            handler(self.request.body)
        except AttributeError:
            e = RouteNotFound(action)
            self.respond(e.message, e.code)
        except GreyError as e:
            self.respond(e.message, e.code)


    def respond(self, data, code=200):
        self.set_status(code)
        self.write(JSONEncoder().encode({
            "status": code,
            "data": data
        }))
        self.finish()
