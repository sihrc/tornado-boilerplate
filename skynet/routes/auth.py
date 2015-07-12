"""
SkyNetService Authentication Route
Creating and Maintaining Users
"""
from skynet.routes.utils.auth_utils import user_hash
from skynet.routes.utils import unpack, mongo_callback
from skynet.routes.handler import SkyNetHandler
import skynet.db.user_db as UserDB

class AuthHandler(SkyNetHandler):
    # Create User if doesn't exist
    @unpack(["phone", "device"])
    def login(self, phone, device):
        @mongo_callback(self)
        def create_callback(result):
            self.respond({
                "_id": result,
                "phone": phone,
            })

        @mongo_callback(self)
        def find_callback(result):
            if result:
                self.respond({
                    "_id": result["_id"],
                    "phone": result["phone"]
                })
                return
            UserDB.create_user(phone, hashed, create_callback)

        hashed = user_hash(phone, device)
        UserDB.find_user_id(hashed, find_callback)

AuthRoute = (r"/auth/(?P<action>[a-zA-Z]+)?", AuthHandler)
