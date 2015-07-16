"""
Indico User database handler
"""
import indico.db

USER_SCHEMA = {
    'user_id': (str, True),
    'name': (str, True),
    'phone': (str, True),
    'email': (str, True),
    'created':  (int, False),          #UTC milliseconds
    'birthday': (int, True),       #UTC milliseconds
    'location': (str, False),
    'profilePic': (str, True),
    'gcm': (str, False),
    'asked': (list, False),
    'favorite': (list, False),
    'discussed': (list, False),
    'hide': (list, False)
}

@indico.db.mongo
def find_user(user_id, callback):
    indico.db.mongodb.user.find_one(
        { "user_id": user_id },
        new=True,
        callback = callback
    )

@indico.db.mongo_obj(USER_SCHEMA)
@indico.db.mongo
def sync_user(update_dic, user_id, callback):
    indico.db.mongodb.user.find_and_modify(
        query={ 'user_id': user_id },
        update= { "$set": update_dic },
        new=True,
        callback = callback,
        upsert=True
    )

@indico.db.mongo
def update(update_dic, user_id, callback):
    indico.db.mongodb.user.find_and_modify(
        query={ 'user_id': user_id },
        update=update_dic,
        new=True,
        callback = callback,
        upsert=True
    )
