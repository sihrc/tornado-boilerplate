"""
indico Test Suite
routes > auth utils
"""
import unittest, os

from mock import patch

import indico.utils.auth.auth_utils as utils
from indico.tests.mocks import BOOLIO_KEY

def error():
    raise ImportError

class AuthUtilsTestCase(unittest.TestCase):
    def test_user_hash(self):
        reload(utils)

        hashed = utils.user_hash(BOOLIO_KEY)

        self.assertTrue(str.isalnum(hashed))
        self.assertEqual(len(hashed), 56)

    def test_import_from_environ(self):
        reload(utils)
        self.assertEquals(
            utils.USER_SALT,
            os.environ.get("USER_SALT")
        )
