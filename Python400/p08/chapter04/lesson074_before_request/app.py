#!/usr/bin/env python
# -*-coding:utf-8-*-
from flask import Flask, g, request, url_for


app = Flask(__name__)


@app.route('/')
def index():
    return f'message: {g.msg}'


# 被注册函数没有参数传入
# 被注册函数的所有返回值会被忽略
@app.before_first_request
def received_first_request():
    print('received first request')


# 被注册函数没有参数传入
# 常用于对上下文对象进行提前处理，如在g对象中加入数据库连接
# 如果被注册函数返回了一个非None的值，该值的处理方式与视图函数一样，并且该请求不会进一步被处理
@app.before_request
def received_request():
    if str(request.url_rule) == url_for('index'):
        g.msg = 'This is a message from function received_request().'
    else:
        return 'Access http://127.0.0.1:5000 please.'


if __name__ == '__main__':
    app.run(debug=True)