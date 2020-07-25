#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, current_app


app = Flask(__name__)


@app.route('/')
def index():
    # 视图函数内可以直接访问app上下文
    name = current_app.name
    return f'current app: {name}'


# 视图函数外需要手动将app上下文入栈
with app.app_context():
    name = current_app.name
    print(f'current app: {name}')


if __name__ == '__main__':
    app.run(debug=True)
