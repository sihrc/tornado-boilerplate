"""
Indico Mock Data
"""
import os

from indico.utils.auth.auth_utils import user_hash

USER_ID = "facebook742627827"
BOOLIO_KEY = user_hash(USER_ID)

USER = {
    "name": "Christopher Lee",
    "location": "Cambridge, MA",
    "phone": "9097208906",
    "birthday": 754722000000,
    "profilePic": "http://graph.facebook.com/742627827/picture?type=square",
    "email": "sihrc.c.lee@gmail.com",
    "user_id": USER_ID
}

HEADERS = {
    "indico_key": BOOLIO_KEY
}

LOGIN_DATA = {
    "access_token": os.environ.get("USER_SALT"),
    "oauth_id": "742627827",
    "user": USER
}

QUESTION = {
    "question": "Is this a sample question?",
    "creator": USER_ID,
    "image": "http://graph.facebook.com/742627827/picture?type=square",
    "left": "Left Answer",
    "right": "Right Answer"
}
