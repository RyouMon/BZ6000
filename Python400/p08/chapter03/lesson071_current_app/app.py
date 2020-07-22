#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, current_app, render_template


app = Flask(__name__)


@app.route('/')
def index():
    name = current_app.name
    return f'视图函数内访问应用上下文：{name}'


#
with app.app_context() as ctx:
    print(current_app.name)


if __name__ == '__main__':
    app.run(debug=True)
