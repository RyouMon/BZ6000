"""
Template
Statement and expression.
"""
from tornado.web import Application, RequestHandler
from tornado.ioloop import IOLoop


def reverse(l):
    if isinstance(l, list):
        l.reverse()
    return l


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class IndexHandler(RequestHandler):
    def get(self):
        student = Student('Kana', 18)
        ls = ['item0', 'item1', 'item2']
        dc = {
            's1': 'Aki',
            's2': 'Inori',
        }
        context = {
            'student': student,
            'list': ls,
            'dict': dc,
            'reverse': reverse,
        }
        return self.render('templates/lesson012_template_expression_and_statement.html', **context)


def make_app():
    return Application([
        (r'/', IndexHandler),
    ])


if __name__ == '__main__':
    app = make_app()
    app.listen(8008)
    IOLoop.current().start()
