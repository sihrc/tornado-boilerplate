"""
SkyNet Request Handler
"""
import json
from bson.objectid import ObjectId

import tornado.web

from skynet.routes.utils.auth_utils import user_hash

class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)

class SkyNetHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    def post(self, action):
        try:
            # Fetch appropriate handler
            handler = getattr(self, str(action))

            # Pass along the data and get a result
            handler(self.request.body)
        except AttributeError:
            self.respond("%s route could not be found" % action, code = 404)
            return
        except ValueError as e:
            self.respond(str(e), code=400)



    def respond(self, data, code=200):
        self.set_status(code)
        self.write(JSONEncoder().encode({
            "status": code,
            "data": data
        }))
        self.finish()
