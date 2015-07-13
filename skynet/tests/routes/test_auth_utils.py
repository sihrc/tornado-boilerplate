"""
SkyNet Test Suite
routes > auth utils
"""
import unittest

from skynet.routes.utils.auth_utils import user_hash

class AuthUtilsTestCase(unittest.TestCase):
    def test_user_hash(self):
        phone = "fakephone"
        device = "fakedevice"

        hashed = user_hash(phone, device)

        self.assertTrue(str.isalnum(hashed))
        self.assertEqual(len(hashed), 56)
