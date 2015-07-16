"""
IndicoService User Route
Creating and Maintaining Users
"""
import indico.db.user_db as UserDB
from indico.utils import unpack, mongo_callback, type_check
from indico.routes.handler import IndicoHandler
from indico.utils.auth.auth_utils import auth


class UserHandler(IndicoHandler):
    @auth
    @unpack("update_user")
    @type_check(dict)
    def update(self, update_user):
        @mongo_callback(self)
        def update_callback(result):
            self.respond(result)

        UserDB.update({ "$set": update_user }, self.user_id, update_callback)

UserRoute = (r"/user/(?P<action>[a-zA-Z]+)?", UserHandler)
