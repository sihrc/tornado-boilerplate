"""
grey Test Suite
Routes > Handler
"""
import unittest

from mock import patch

from grey.routes.handler import greyHandler, JSONEncoder
from grey.tests.utils.server import server, post
from grey.routes.utils import unpack

@unpack(["data"])
def example(self, data):
    self.respond(data)

def bad(x):
    raise ValueError

@patch("grey.routes.utils.smart_parse", bad)
@unpack(["data"])
def bad_json_example(self, data):
    print "Shouldn't run"

greyHandler.example = example
greyHandler.badexample = bad_json_example
ROUTES = [(r"/(?P<action>[a-zA-Z]+)?", greyHandler)]

class RouteHandlerTest(unittest.TestCase):
    port = 7000

    @server(port, ROUTES)
    def test_post(self):
        result = post(self.port, "example", {
            "data": "example data"
        })

        self.assertIn("data", result)
        self.assertEqual(result["data"], "example data")

    @server(port, ROUTES)
    def test_bad_post(self):
        result = post(self.port, "example", {
            "not_data": "example data"
        })
        self.assertEqual(result["status"], 400)

    @server(port, ROUTES)
    def test_bad_post_missing(self):
        result = post(self.port, "notexample", {
            "not_data": "example data"
        })
        self.assertEqual(result["status"], 404)

    @server(port, ROUTES)
    def test_bad_json_post(self):
        result = post(self.port, "badexample", {
            "data": "bad example"
        })
        self.assertEqual(result["status"], 400)

    def test_JSONEncoder_error(self):
        self.assertRaises(TypeError,
            JSONEncoder().encode, object())

    def test_JSONEncoder_mongo(self):
        from bson.objectid import ObjectId
        data = {
            "_id": ObjectId("a"*24)
        }
        self.assertEqual(
            JSONEncoder().encode(data),
            "{\"_id\": \"%s\"}" % data["_id"]
        )

    def test_JSONEncoder_success(self):
        data = { "sample": "sample" }
        self.assertEqual(
            JSONEncoder().encode(data),
            "{\"sample\": \"sample\"}"
        )

if __name__ == "__main__":
    unittest.main()
