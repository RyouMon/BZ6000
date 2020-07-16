#!/usr/bin/env python
# -*-coding:utf-8-*-
from flask import Flask, url_for, render_template


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/string')
def string():
    return '返回值为字符串'


@app.route('/dict')
def dictionary():
    return {"姓名": "KANA", "年龄": 18}


@app.route('/tuple')
def tuple():
    return "KANA", 200


if __name__ == '__main__':
    app.run(debug=True)
