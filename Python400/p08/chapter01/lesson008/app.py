from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/app/')
def my_first_app():
    return 'This is my first Flask app.'


if __name__ == '__main__':
    app.run()
