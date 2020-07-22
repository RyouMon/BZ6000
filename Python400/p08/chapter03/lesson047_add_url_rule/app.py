#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, url_for


app = Flask(__name__)


def index():
    url = url_for('index')
    return f'Hello World! Access URL "{url}"'


# 方法add_url_rule的工作方式与装饰器route类似
app.add_url_rule('/', 'index', index)


if __name__ == '__main__':
    app.run(debug=True)
