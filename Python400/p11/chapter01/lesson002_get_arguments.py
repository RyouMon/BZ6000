import tornado.ioloop
import tornado.web


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('templates/lesson002/index.html')

    def post(self):
        username = self.get_argument('username')
        password = self.get_argument('pwd')
        self.write(f'{username} + {password}')


def make_app():
    return tornado.web.Application([
        (r'/', MainHandler)
    ])


if __name__ == '__main__':
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
