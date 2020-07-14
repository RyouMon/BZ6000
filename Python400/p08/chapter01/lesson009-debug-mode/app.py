"""
使用DEBUG模式开启FLASK
"""
from flask import Flask

app = Flask(__name__)


@app.route('/')
def bug():
    """
    制造一个错误
    """
    return 1/0


if __name__ == '__main__':
    app.run()

    # 终端执行命令：
    # $ export FLASK_ENV=development
    # $ flask run
    # (Windows下使用set来代替export)
