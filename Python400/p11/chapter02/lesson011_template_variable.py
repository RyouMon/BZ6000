"""
Template
Use variable in template.
"""
from tornado.web import Application, RequestHandler
from tornado.ioloop import IOLoop


class IndexHandler(RequestHandler):
    def get(self):
        return self.render('templates/lesson011_template_variable.html', name='Kana')


def make_app():
    return Application([
        (r'/', IndexHandler),
    ])


if __name__ == '__main__':
    app = make_app()
    app.listen(8008)
    IOLoop.current().start()
