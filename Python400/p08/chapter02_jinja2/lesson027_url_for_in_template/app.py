#!/usr/bin/env python
# -*-coding:utf-8-*-
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    kwargs = dict(
        host='127.0.0.1',
        port='5000',
        page='login'
    )
    return render_template('index.html', **kwargs)


@app.route('/login')
def login():
    return "Login Page."


if __name__ == '__main__':
    app.run(debug=True)