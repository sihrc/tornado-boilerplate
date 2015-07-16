"""
Indico Auth Utility functions
"""
import hashlib, os

import indico
import indico.db.auth_db as AuthDB
from indico.error import AuthError
from indico.utils import mongo_callback

USER_SALT = os.environ.get('USER_SALT')

def auth(func):
    def wrapper(self, data):
        @mongo_callback(self)
        def find_callback(result):
            if not result:
                raise AuthError()
            self.user_id = result["user_id"]
            func(self, data=data)

        indico_key = self.request.headers.get("indico_key")
        if not indico_key:
            raise AuthError()
        AuthDB.get_user_id(indico_key, find_callback)
    return wrapper

def user_hash(oauth_id):
    return hashlib.sha224(USER_SALT + oauth_id).hexdigest()
