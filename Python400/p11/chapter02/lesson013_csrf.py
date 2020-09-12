
"""
XSRF protect
"""
from tornado.web import Application, RequestHandler
from tornado.ioloop import IOLoop


class IndexHandler(RequestHandler):
    def get(self):
        return self.render('templates/lesson013_csrf.html')

    def post(self):
        name = self.get_argument('username')
        pwd = self.get_argument('pwd')
        self.write(f'{name} + {pwd}')


def make_app():
    return Application([
        (r'/', IndexHandler),
    ], xsrf_cookies=True)


if __name__ == '__main__':
    app = make_app()
    app.listen(8008)
    IOLoop.current().start()
