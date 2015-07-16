"""
Indico Auth database handler
"""

import indico.db

@indico.db.mongo
def save_key(key, user_id, callback):
    indico.db.mongodb.auth.find_and_modify(
        query = { "key" : key },
        update = { "$set" : { "user_id": user_id } },
        new = True,
        upsert = True,
        callback = callback
    )

@indico.db.mongo
def get_user_id(key, callback):
    indico.db.mongodb.auth.find_one(
        { "key" : key },
        callback = callback
    )
