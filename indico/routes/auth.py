"""
IndicoService Authentication Route
Creating and Maintaining Users
"""
from indico.utils.auth.auth_utils import auth, user_hash
from indico.utils.auth.facebook_utils import check_access_token
from indico.error import FacebookTokenError
from indico.utils import unpack, mongo_callback, type_check
from indico.routes.handler import IndicoHandler
from indico.db import current_time
import indico.db.user_db as UserDB
import indico.db.auth_db as AuthDB


class AuthHandler(IndicoHandler):
    # Create User if doesn't exist
    @unpack("access_token", "oauth_id", "user")
    @type_check(str, str, dict)
    def login(self, access_token, oauth_id, user):
        if not check_access_token(access_token):
            raise FacebookTokenError()

        @mongo_callback(self)
        def sync_callback(result):
            self.respond({
                "user": result,
                "indico_key": indico_key
            })

        @mongo_callback(self)
        def find_callback(result):
            if not result:
                user["created"] = current_time()
            UserDB.sync_user(user, "facebook" + oauth_id, sync_callback)


        @mongo_callback(self)
        def save_key_callback(result):
            UserDB.find_user(user_id, find_callback)

        user_id = "facebook" + oauth_id
        indico_key = user_hash(user_id)
        AuthDB.save_key(indico_key, user_id, save_key_callback)

    @auth
    def check(self, data):
        self.respond(True)

AuthRoute = (r"/auth/(?P<action>[a-zA-Z]+)?", AuthHandler)
