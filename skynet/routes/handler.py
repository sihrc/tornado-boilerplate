"""
SkyNet Request Handler
"""
import json
from bson.objectid import ObjectId

import tornado

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
            handler = getattr(self, str(action))
        except AttributeError:
            self.respond("%s route could not be found" % action, code = 404)
            return

        # Pass along the data and get a result
        handler(self.request.body)

    def respond(self, data, code=200):
        self.set_status(code)
        self.write(JSONEncoder().encode({
            "status": code,
            "data": data
        }))
        self.finish()
