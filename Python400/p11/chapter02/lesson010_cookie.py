"""
Cookies
Access 127.0.0.1:8008/set/ first, then access 127.0.0.1:8008/get/.
"""
from tornado.web import Application, RequestHandler
from tornado.ioloop import IOLoop


class SetCookieHandler(RequestHandler):
    def get(self):
        # Set cookie
        # self.set_cookie('name', 'kana')

        # Set secure cookie
        self.set_secure_cookie('name', 'kana')


class GetCookieHandler(RequestHandler):
    def get(self):
        # Get and write cookie
        # self.write(self.get_cookie('name'))

        # Get and write secure cookie
        self.write(self.get_secure_cookie('name'))


settings = {
    'cookie_secret': b'au\x90]\xb1?,\xdeb\x81e\xad_!\x99`'
}


def make_app():
    return Application([
        (r'/set/', SetCookieHandler),
        (r'/get/', GetCookieHandler),
    ], **settings)


if __name__ == '__main__':
    app = make_app()
    app.listen(8008)
    IOLoop.current().start()
