"""
grey User database handler
"""
from grey.db.db import mongodb

user_db = mongodb.user_db

def find_user_id(hashed, callback):
    user_db.find_one({'hashed': hashed}, callback = callback)

def create_user(phone, hashed, callback):
    user_db.save({
        'hashed': hashed,
        'phone': phone
    }, callback = callback)
