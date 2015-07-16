"""
GreyService Path Route
Creating and Maintaining Paths
"""
from grey.routes.utils.auth_utils import user_hash
from grey.routes.utils import unpack, mongo_callback
from grey.routes.handler import GreyHandler
import grey.db.path_db as PathDB

class PathHandler(GreyHandler):
    # Create User if doesn't exist
    @unpack(["creatorId", "name"])
    def create(self, creatorId, name):
        @mongo_callback(self)
        def create_callback(_id):
            self.respond({
                "_id": _id,
            })
        PathDB.create_path(creatorId, name, create_callback)

PathRoute = (r"/path/(?P<action>[a-zA-Z]+)?", PathHandler)
