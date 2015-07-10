"""
SkyNetService Authentication Route
Creating and Maintaining Users
"""
import hashlib

import tornado
import simplecrypt

from skynet.routes.utils.auth_utils import user_hash
from skynet.routes.utils import unpack, mongo_callback
import skynet.db.user_db as UserDB


class AuthHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    def post(self, action):
        try:
            handler = getattr(AuthHandler, action)
        except AttributeError:
            self.respond("%s route could not be found" % action, code = 404)
            return

        # Pass along the data and get a result
        handler(self, self.request.body)

    def respond(self, data, code=200):
        self.set_status(code)
        self.write(tornado.escape.json_encode({
            "status": code,
            "data": data
        }))
        self.finish()

    # Create User if doesn't exist
    @unpack(["phone", "device"])
    def create(self, phone, device):
        @mongo_callback(self)
        def find_callback(result):
            self.respond("Found me! %s, %s" % (phone, device))

        hashed = user_hash(phone, device)
        UserDB.find_user_id(hashed, find_callback)

AuthRoute = (r"/auth/(?P<action>[a-zA-Z]+)?", AuthHandler)
