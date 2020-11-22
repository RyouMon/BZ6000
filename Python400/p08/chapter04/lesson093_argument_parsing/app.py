from flask import Flask
from flask_restful import Api, Resource, reqparse


app = Flask(__name__)
api = Api(app)


class RegisterView(Resource):
    def post(self):
        parser = reqparse.RequestParser()

        parser.add_argument('name', type=str, help='用户名验证失败', required=True, trim=True)

        args = parser.parse_args()
        print(args)
        return {'tips': '注册成功'}


api.add_resource(RegisterView, '/')


if __name__ == '__main__':
    app.run(debug=True)
