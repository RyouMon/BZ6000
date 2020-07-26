#!/usr/bin/env python
# -*-coding:utf-8-*-
from flask import Flask


app = Flask(__name__)


@app.errorhandler(404)
def not_found_error_handler(error):
    return '您访问的页面不存在', 404


if __name__ == '__main__':
    app.run(debug=True)