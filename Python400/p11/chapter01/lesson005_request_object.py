import tornado.web
import tornado.ioloop


class GetRequestInfo(tornado.web.RequestHandler):
    def get(self):
        # Get request object
        request = self.request
        self.write(r'%s</br>%s</br>%s' % (request.protocol, request.uri, request.headers))


def make_app():
    return tornado.web.Application([
        (r'/Rq/', GetRequestInfo),
    ])


if __name__ == '__main__':
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
