"""
Indico Test Utils for Motor
"""
from tornado.testing import AsyncTestCase
from motor import MotorClient

from indico.config import MONGODB
import indico.db

class MongoTest(AsyncTestCase):
    def callback(self, result, error):
        self.stop((result, error))

    def setUp(self):
        super(MongoTest, self).setUp()
        name = str(self).split(" ")
        self.name = name[0].replace("_","") + name[1].split(".")[-1][:-1]
        indico.db.CLIENT = MotorClient(MONGODB)
        indico.db.mongodb = indico.db.CLIENT[self.name]

    def tearDown(self):
        indico.db.CLIENT.drop_database(self.name)
        super(MongoTest, self).tearDown()
