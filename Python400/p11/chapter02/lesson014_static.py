"""
Manage Static File
"""
import os
from tornado.web import Application, RequestHandler, StaticFileHandler
from tornado.ioloop import IOLoop


class IndexHandler(RequestHandler):
    def get(self):
        return self.render('templates/lesson014_static.html')


def make_app():
    return Application([
        (r'/', IndexHandler),
        (r'/static/(.*)', StaticFileHandler, {'path': os.path.join(os.getcwd(), 'static')})
    ])


if __name__ == '__main__':
    app = make_app()
    app.listen(8008)
    IOLoop.current().start()
