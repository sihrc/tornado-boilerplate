"""
Indico Test Suite
Routes > User
"""
import unittest

from indico.tests.testutils.server import ServerTest
from indico.tests.mocks import LOGIN_DATA
from indico.routes.user import UserRoute
from indico.routes.auth import AuthRoute


class UserRouteTest(ServerTest):
    routes = [UserRoute, AuthRoute]

    def test_update(self):
        update_user = { "update_user":
                { "new_field": "new field", "location": "updated location" }
        }
        # headers for auth/login is used for request params
        self.post("auth/login", LOGIN_DATA)
        user = self.post("user/update", update_user)

        self.assertIn("data", user)
        self.assertIn("user_id", user["data"])
        self.assertIn("new_field", user["data"])
        self.assertIn("location", user["data"])
        self.assertEqual(
            update_user["update_user"]["location"],
            user["data"]["location"]
        )

if __name__ == "__main__":
    unittest.main()
