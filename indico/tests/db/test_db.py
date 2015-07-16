"""
Indico Test Suite
Db
"""
import unittest

import motor

from indico.tests.testutils.mongo import MongoTest
from indico.db import mongodb, mongo_obj
from indico.error import WrongFieldType

class DBTest(MongoTest):
    def test_db(self):
        self.assertIsInstance(mongodb, motor.MotorDatabase)

    def test_auth_db(self):
        self.assertIsInstance(mongodb.auth_db, motor.MotorCollection)

    def test_mongo_obj(self):
        schema = {
            'data': (str, True)
        }
        @mongo_obj(schema)
        def get_obj(data):
            return data

        self.assertIn("data", get_obj({ "data": u"test" }))
        self.assertIn("data", get_obj({ "data": "test" }))
        self.assertRaises(WrongFieldType, get_obj, {
            "data": 5
        })
        self.assertIn("data", get_obj({ }))

if __name__ == "__main__":
    unittest.main()
