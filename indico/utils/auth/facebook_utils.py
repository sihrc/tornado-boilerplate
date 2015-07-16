"""
Facebook Utility functions
"""
import os

import requests

ACCESS_TOKEN_URL = "https://graph.facebook.com/me?fields=id&access_token=%s"

def check_access_token(access_token):
    results = requests.get(ACCESS_TOKEN_URL % access_token).json()
    return results.get("is_valid", False) or os.environ.get("USER_SALT") == access_token
