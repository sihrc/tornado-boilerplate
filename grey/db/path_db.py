"""
Grey User database handler
"""
from grey.db.db import mongodb

path_db = mongodb.path_db

def create_path(creatorId, name, callback):
    path_db.save({
        'creatorId': creatorId,
        'name': name
    }, callback = callback)
