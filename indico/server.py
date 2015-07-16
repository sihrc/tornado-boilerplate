import tornado.ioloop
import tornado.web

import indico.config as CONFIG
from indico.routes.auth import AuthRoute
from indico.routes.user import UserRoute

def main(debug = True, port = CONFIG.PORT):
    application = tornado.web.Application([
        AuthRoute,
        UserRoute
    ], debug = debug
     , autoreload = debug)

    application.listen(port)
    tornado.ioloop.IOLoop.current().start()
