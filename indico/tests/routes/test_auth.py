"""
Grey Test Suite
Routes > Path
"""
import unittest

from indico.tests.testutils.server import ServerTest
from indico.tests.mocks import LOGIN_DATA, USER
from indico.routes.auth import AuthRoute

class AuthRouteTest(ServerTest):
    routes = [AuthRoute]
    def setUp(self):
        super(AuthRouteTest, self).setUp()

    def test_non_authenticated(self):
        result = self.post("auth/check", USER)

        self.assertIn("data", result)
        self.assertEqual("User not authenticated", result["data"])

    def test_missing_credentials(self):
        result = self.post("auth/check", USER, {})
        self.assertEquals(result["status"], 401)

    def test_wrong_access_key_credentials(self):
        BAD_LOGIN = LOGIN_DATA.copy()
        BAD_LOGIN["access_token"] = "wrong_token"
        result = self.post("auth/login", BAD_LOGIN)
        self.assertEquals(result["status"], 401)

    def test_authed(self):
        self.post("auth/login", LOGIN_DATA)
        result = self.post("auth/check", data=None)

        self.assertTrue(result["data"])

    def test_login_created(self):
        result = self.post("auth/login", LOGIN_DATA)
        self.assertIn("data", result)
        self.assertIn("user", result["data"])
        self.assertIn("indico_key", result["data"])

    def test_login_existing(self):
        result = self.post("auth/login", LOGIN_DATA)
        # Again to test existing user
        result_again = self.post("auth/login", LOGIN_DATA)
        self.assertEqual(
            result["data"]["user"]["created"],
            result_again["data"]["user"]["created"],
        )


if __name__ == "__main__":
    unittest.main()
