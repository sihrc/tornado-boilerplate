"""
SkyNet Test Suite
Db
"""
import unittest, time
from mock import patch

import motor
from tornado.ioloop import IOLoop
from bson.objectid import ObjectId

from skynet.db import db, user_db
from skynet.tests import SkyNetAsyncTest

@patch("skynet.db.user_db.user_db", db.mongodb.test_user_db)
class DBTest(SkyNetAsyncTest):
    def test_db(self):
        self.assertIsInstance(db.mongodb, motor.MotorDatabase)

    def test_user_db(self):
        self.assertIsInstance(user_db.user_db, motor.MotorCollection)

    def test_find_user_id(self):
        @self.callback
        def callback(result, error):
            self.assertIs(error, None)
            self.assertIs(result, None)

        hashed = "distincthash1"
        user_db.find_user_id(hashed, callback)
        self.wait()

    def test_create_user(self):
        phone = "fakephonenumber"
        hashed = "distincthash2"

        # Create
        @self.callback
        def callback(result, error):
            self.assertIs(error, None)
            self.assertIsInstance(result, ObjectId)
        user_db.create_user(phone, hashed, callback)
        self.wait()

        # Check if created
        @self.callback
        def check_created(result, error):
            self.assertIs(error, None)
            self.assertEqual(result["phone"], phone)
        user_db.find_user_id(hashed, check_created)
        self.wait()

    def test_bad_calls(self):
        @self.callback
        def error_callback(result, error):
            self.assertIs(result, None)
            self.assertIsNot(error, None)
        random_object = object()
        user_db.find_user_id(random_object, error_callback)
        self.wait()

if __name__ == "__main__":
    unittest.main()
