"""
SkyNet Auth Utility functions
"""
import hashlib

from skynet.private import USER_SALT

def user_hash(phone, device):
    return hashlib.sha224(USER_SALT + phone + device).hexdigest()
