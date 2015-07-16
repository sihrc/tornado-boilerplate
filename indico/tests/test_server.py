"""
Indico Test server.py
"""
import unittest, threading, sys, logging

import requests
from tornado.ioloop import IOLoop

from indico import server

# Disable tornado access warnings
logging.getLogger("tornado.access").propagate = False
logging.getLogger("tornado.access").addHandler(logging.NullHandler())

class TestingThread(threading.Thread):
    error = None

    def __init__(self, target, args = ()):
        super(TestingThread, self).__init__(target = self.run)
        self.test = target
        self.args = args
        self.daemon = True

    def run(self):
        try:
            self.test(self.args)
            return
        except Exception:
            self.error = sys.exc_info()
        finally:
            IOLoop.instance().stop()

    def errors(self):
        if self.error:
            raise self.error[1], None, self.error[2]

class TestServerCase(unittest.TestCase):
    def test_main(self):
        port = 7869
        def test(cls):
            import time
            time.sleep(.5)
            result = requests.post("http://localhost:%s/auth/login" % port, {}).json()
            self.assertEqual(result["status"], 400)

        thread = TestingThread(target = test)
        thread.start()
        server.main(True, port)
        thread.join()
        thread.errors()

if __name__ == "__main__":
    unittest.main()
