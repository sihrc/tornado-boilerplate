"""
Indico Test Suite
Db
"""
import unittest

from indico.tests.testutils.mongo import MongoTest
from indico.tests.mocks import USER_ID, BOOLIO_KEY
from indico.db import auth_db


class AuthDbTest(MongoTest):
    def test_get_user_id(self):
        auth_db.get_user_id(BOOLIO_KEY, self.callback)
        result, error = self.wait()
        self.assertIs(error, None)
        self.assertIs(result, None)

    def test_save_key(self):
        auth_db.save_key(BOOLIO_KEY, USER_ID, self.callback)
        result, error = self.wait()
        self.assertIs(error, None)

        auth_db.get_user_id(BOOLIO_KEY, self.callback)
        result, error = self.wait()
        self.assertIs(error, None)
        self.assertEqual(result["user_id"], USER_ID)

    def test_bad_calls(self):
        random_object = object()
        auth_db.get_user_id(random_object, self.callback)
        result, error = self.wait()
        self.assertIs(result, None)
        self.assertIsNot(error, None)

if __name__ == "__main__":
    unittest.main()
