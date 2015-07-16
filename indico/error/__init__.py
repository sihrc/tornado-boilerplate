"""
IndicoServer Errors
"""

class IndicoError(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code
        super(Exception, self).__init__(message)

# 400
class MissingField(IndicoError):
    def __init__(self, field):
        IndicoError.__init__(self,
            "%s field was not provided" % field,
            400
        )

class WrongFieldType(IndicoError):
    def __init__(self, field, _given, _required):
        IndicoError.__init__(self,
            "Field %s - %s is type %s but should be %s" %
                (field, _given, type(_given), _required),
            400
        )

class InvalidJSON(IndicoError):
    def __init__(self):
        IndicoError.__init__(self,
            "No JSON object could be decoded.",
            400
        )

# 401
class FacebookTokenError(IndicoError):
    def __init__(self):
            IndicoError.__init__(self,
            "Facebook Auth Token invalid",
            401
        )

class AuthError(IndicoError):
    def __init__(self):
        IndicoError.__init__(self,
            "User not authenticated",
            401
        )

# 404
class RouteNotFound(IndicoError):
    def __init__(self, action):
        IndicoError.__init__(self,
            "%s route could not be found" % action,
            404
        )

# 500
class MongoError(IndicoError):
    def __init__(self, message):
        IndicoError.__init__(self,
            message,
            500
        )

class ServerError(IndicoError):
    def __init__(self):
        IndicoError.__init__(self,
            "we screwed up and have some debugging to do",
            500
        )
