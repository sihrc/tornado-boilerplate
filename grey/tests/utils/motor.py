"""
grey Test Utils for Motor
"""
import unittest

from tornado.ioloop import IOLoop

class greyAsyncTest(unittest.TestCase):
    # Ensure IOLoop stops to prevent blocking tests
    def callback(self, func):
        def wrapper(*args, **kwargs):
            IOLoop.instance().stop()
            try:
                func(*args, **kwargs)
            except AssertionError as e:
                self.error = e
        return wrapper

    def wait(self):
        IOLoop.instance().start()

    def setUp(self):
        self.error = None
        super(greyAsyncTest, self).setUp()

    def tearDown(self):
        if self.error:   self.fail(str(self.error))
        super(greyAsyncTest, self).tearDown()
