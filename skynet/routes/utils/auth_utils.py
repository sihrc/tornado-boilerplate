"""
SkyNet Auth Utility functions
"""
import hashlib

try:
    from skynet.private import USER_SALT
except ImportError:
    import os
    USER_SALT = os.environ.get('USER_SALT')

def user_hash(phone, device):
    return hashlib.sha224(USER_SALT + phone + device).hexdigest()
