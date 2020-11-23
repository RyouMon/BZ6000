from flask import Flask
from flask_restful import Api, Resource, fields, marshal_with


app = Flask(__name__)
api = Api(app)


class TodoDao:
    def __init__(self, todo_id, task):
        self.todo_id = todo_id
        self.task = task
        # This field will not be sent in the response
        self.status = 'active'


class Todo(Resource):

    resource_fields = {
        'todo_id': fields.String,
        'task': fields.String,
    }

    @marshal_with(resource_fields)
    def get(self):
        return TodoDao(todo_id='my_todo', task='Remember the milk')


api.add_resource(Todo, '/')


if __name__ == '__main__':
    app.run(debug=True)
