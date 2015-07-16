"""
grey Test Suite
routes > auth utils
"""
import unittest, os

from mock import patch

import grey.routes.utils.auth_utils as utils

def error():
    raise ImportError

class AuthUtilsTestCase(unittest.TestCase):
    def test_user_hash(self):
        reload(utils)

        phone = "fakephone"
        device = "fakedevice"

        hashed = utils.user_hash(phone, device)

        self.assertTrue(str.isalnum(hashed))
        self.assertEqual(len(hashed), 56)

    @patch("os.path.exists", lambda x: False)
    def test_import_error(self):
        reload(utils)
        self.assertEquals(
            utils.USER_SALT,
            os.environ.get("USER_SALT")
        )
