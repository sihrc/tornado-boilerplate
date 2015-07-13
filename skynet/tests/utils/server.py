"""
SkyNet Test Utils for Running Servers
"""
import threading, requests, json, logging
from functools import wraps

from tornado.web import Application
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop

# Disable tornado access warnings
logging.getLogger("tornado.access").propagate = False
logging.getLogger("tornado.access").addHandler(logging.NullHandler())

def post(port, route, data):
    result = requests.post("http://localhost:%d/%s" % (port, route),
        data = json.dumps(data)).text
    return json.loads(result)

def get(port, route):
    result = requests.get("http://localhost:%d/%s" % (port, route)).text
    return json.loads(result)

def server(port, routes):
    def decorator(func):
        @wraps(func)
        def wrapper(*args):
            server, thread = _startServer(port, routes)
            try:
                func(*args)
            except Exception:
                raise
            finally:
                _stopServer(server, thread)
        return wrapper
    return decorator

def _startServer(port, routes):
    # Start Server
    application = Application(routes, debug = False)
    application.logging = "none"
    server = HTTPServer(application)
    server.listen(port)
    # Start nonblocking IOLoop
    thread = threading.Thread(target=IOLoop.instance().start)
    thread.start()
    return server, thread

def _stopServer(server, thread):
    IOLoop.instance().stop()
    thread.join()
    server.stop()
