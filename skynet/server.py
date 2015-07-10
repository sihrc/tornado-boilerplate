import tornado.ioloop
import tornado.web

import skynet.config as CONFIG
from skynet.routes.auth import AuthRoute

def main(debug = True, port = CONFIG.PORT):
    application = tornado.web.Application([
        AuthRoute,
    ], debug = debug
     , autoreload = debug)

    application.listen(port)
    tornado.ioloop.IOLoop.current().start()

if __name__ == "__main__":
    main()
