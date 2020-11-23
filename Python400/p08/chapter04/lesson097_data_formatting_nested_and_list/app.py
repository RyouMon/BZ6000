from flask import Flask
from flask_restful import Api, Resource, marshal_with, fields


class Author:
    def __init__(self, _id, name, age):
        self.id = _id
        self.name = name
        self.age = age


class Post:
    def __init__(self, _id, title, content, author):
        self.id = _id
        self.title = title
        self.content = content
        self.author = author
        self.tags = []


class Tag:
    def __init__(self, _id, name):
        self.id = _id
        self.name = name


def create_post():
    author = Author(1, 'kana', 18)
    post = Post(1, 'Today is my birthday!', 'I\' very happy!', author)
    tag_1 = Tag(1, 'Birthday')
    tag_2 = Tag(2, 'Hanazawa Kana')
    post.tags.extend([tag_1, tag_2])
    return post


class PostDetail(Resource):

    resource_fields = {
        '_id': fields.Integer,
        'title': fields.String,
        'content': fields.String,
        'author': fields.Nested({
            '_id': fields.Integer,
            'name': fields.String,
            'age': fields.Integer,
        }),
        'tags': fields.List(fields.Nested({
            '_id': fields.Integer,
            'name': fields.String,
        })),
    }

    @marshal_with(resource_fields)
    def get(self):
        return create_post()


app = Flask(__name__)
api = Api(app)
api.add_resource(PostDetail, '/post')


if __name__ == '__main__':
    app.run(debug=True)
