"""
Indico Test Suite
Db
"""
import unittest

from indico.tests.testutils.mongo import MongoTest
from indico.tests.mocks import USER, USER_ID
from indico.db import user_db

class UserDBTest(MongoTest):
    def test_find_user(self):
        user_db.sync_user(USER, USER_ID, self.callback)
        result, error = self.wait()
        self.assertIs(error, None)
        self.assertIsNot(result, None)

        user_db.find_user(USER_ID, self.callback)
        result, error = self.wait()
        self.assertIs(error, None)
        self.assertIsNot(result, None)

    def test_sync_user(self):
        user_db.sync_user(USER, USER_ID, self.callback)
        result, error = self.wait()
        self.assertIs(error, None)
        self.assertIsNot(result, None)

    def test_update(self):
        user_db.sync_user(USER, USER_ID, self.callback)
        result, error = self.wait()
        self.assertIs(error, None)
        self.assertIsNot(result, None)

        user_db.update(
            { "$set": { "name": "updated_name" } },
            USER_ID,
            self.callback
        )
        result, error = self.wait()
        self.assertIs(error, None)
        self.assertEqual(result["name"], "updated_name")

    def test_bad_calls(self):
        random_object = object()
        user_db.find_user(random_object, self.callback)
        result, error = self.wait()
        self.assertIs(result, None)
        self.assertIsNot(error, None)

if __name__ == "__main__":
    unittest.main()
