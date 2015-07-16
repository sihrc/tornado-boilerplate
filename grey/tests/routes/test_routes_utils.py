"""
grey Test Suite
Routes - Utils
"""
import unittest, json

from mocks.request_mock import RequestHandler

import grey.routes.utils as utils
from grey.error import InvalidJSON, MissingField

# Mock request handler
req_handler = RequestHandler()

# Mongo Callback Tests
@utils.mongo_callback(req_handler)
def mongo_callback_example(result):
    req_handler.respond(result, code=200)

# UnPack Tests
@utils.unpack(["example", "data"])
def unpack_example(self, example, data):
    self.respond(data, code=200)

class RoutesUtilsTest(unittest.TestCase):

    def test_mongo_callback_success(self):
        error, result = None, "Result Successful"
        mongo_callback_example(result, error)
        self.assertEqual(req_handler.data, "Result Successful")
        self.assertEqual(req_handler.code, 200)

    def test_mongo_callback_error(self):
        error, result = "Shit went awry", None
        mongo_callback_example(result, error)
        self.assertEqual(req_handler.data, "Mongo Error " + error)
        self.assertEqual(req_handler.code, 500)

    def test_unpack_success(self):
        data = json.dumps({
            "example": "example text",
            "data": "example data"
        })

        unpack_example(req_handler, data)
        self.assertEqual(req_handler.data, "example data")
        self.assertEqual(req_handler.code, 200)

    def test_unpack_fail(self):
        data = json.dumps({
            "wrong": "thing"
        })
        self.assertRaises(MissingField, unpack_example, req_handler, data)

    def test_urlencoded_parse(self):
        self.assertRaises(InvalidJSON, utils.form_urlencoded_parse, "bad")
        self.assertTrue(utils.form_urlencoded_parse("data=example"), {"data": 'example'})

    def test_smart_parse(self):
        self.assertRaises(InvalidJSON, utils.smart_parse, "bad")
        self.assertTrue(utils.smart_parse("data=example"), {"data":"example"})
        self.assertTrue(utils.smart_parse("{\"data\":\"example\"}"), {"data": "example"})

if __name__ == "__main__":
    unittest.main()
