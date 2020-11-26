import json
from flask import Flask, render_template, Response
from flask_restful import Api, Resource


class HelloWorldHtml(Resource):
    def get(self):
        return render_template('hello.html')


class HelloWorldJson(Resource):
    def get(self):
        return {'hello': 'world'}


app = Flask(__name__)
api = Api(app)


@api.representation('text/html')
def output(data, code, headers):
    if isinstance(data, str):
        return Response(data)
    else:
        return Response(json.dumps(data), mimetype='application/json')


api.add_resource(HelloWorldHtml, '/html')
api.add_resource(HelloWorldJson, '/json')


if __name__ == '__main__':
    app.run(debug=True)
