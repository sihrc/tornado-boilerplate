"""
Indico Request Handler
"""
import json, traceback
from bson.objectid import ObjectId

import tornado.web

from indico.error import IndicoError, RouteNotFound, ServerError
from indico.utils import LOGGER

class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)

class IndicoHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    def post(self, action):
        try:
            # Fetch appropriate handler
            if not hasattr(self, str(action)):
                raise RouteNotFound(action)

            # Pass along the data and get a result
            handler = getattr(self, str(action))
            handler(self.request.body)
        except IndicoError as e:
            self.respond(e.message, e.code)
        except Exception as e:
            LOGGER.error(
                "\n\n======== INDICO SERVER ERROR ========\n%s\n%s\n",
                 __file__,
                 traceback.format_exc()
            )
            error = ServerError()
            self.respond(error.message, error.code)


    def respond(self, data, code=200):
        self.set_status(code)
        self.write(JSONEncoder().encode({
            "status": code,
            "data": data
        }))
        self.finish()
