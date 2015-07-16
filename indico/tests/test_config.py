"""
Indico Test Suite
Indico > config
"""
import unittest, re

mongo_uri = re.compile(r'^(mongodb:(?:\/{2})?)((\w+?):(\w+?)@|:?@?)(\w+?):(\d+)')

class ConfigTestCase(unittest.TestCase):
    def test_port(self):
        from indico import config
        self.assertTrue(config.PORT >= 80)

    def test_mongo(self):
        from indico import config
        self.assertTrue(mongo_uri.match(config.MONGODB))

if __name__ == "__main__":
    unittest.main()
