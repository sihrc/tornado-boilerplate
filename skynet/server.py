import tornado.ioloop
import tornado.web

import skynet.config as CONFIG


def main(debug = True, port = CONFIG.PORT):
    application = tornado.web.Application([
        (r"/", MainHandler),
    ], debug = debug)
    application.listen(port)
    tornado.ioloop.IOLoop.current().start()

if __name__ == "__main__":
    main()
