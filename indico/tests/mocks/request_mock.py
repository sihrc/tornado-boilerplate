"""
indico Test Suite Mocks
RequestHandler mock
"""
class RequestHandler(object):
    def __init__(self):
        self.data = None
        self.code = None
    def respond(self, data, code=200):
        self.data = data
        self.code = code
