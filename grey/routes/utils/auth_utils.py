"""
grey Auth Utility functions
"""
import hashlib, os
import grey

def user_hash(phone, device):
    return hashlib.sha224(USER_SALT + phone + device).hexdigest()

# Find the user salt in a manner that allows unittesting
path = os.path.join(os.path.dirname(grey.__file__), "private.py")
if os.path.exists(path):
    from grey.private import USER_SALT
else:
    USER_SALT = os.environ.get('USER_SALT')
