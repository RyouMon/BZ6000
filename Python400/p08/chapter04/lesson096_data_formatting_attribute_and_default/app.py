from flask import Flask
from flask_restful import Api, Resource, fields, marshal_with


class User:
    def __init__(self, username, signature=None):
        self.username = username
        self.signature = signature


class UserDetail(Resource):

    resource_fields = {
        'uname': fields.String(attribute='username'),
        'signature': fields.String(default='This user is too lazy to write nothing.'),
    }

    @marshal_with(resource_fields)
    def get(self):
        return User('wen')


app = Flask(__name__)
api = Api(app)
api.add_resource(UserDetail, '/user')


if __name__ == '__main__':
    app.run(debug=True)
