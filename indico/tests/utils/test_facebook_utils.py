"""
Testing Facebook Utils
"""
import unittest, os

from indico.utils.auth.facebook_utils import check_access_token

class TestFacebookUtils(unittest.TestCase):
    def test_access_token(self):
        self.assertTrue(
            check_access_token(os.environ.get("USER_SALT"))
        )

        self.assertFalse(
            check_access_token("wrong_token")
        )

if __name__ == "__main__":
    unittest.main()
