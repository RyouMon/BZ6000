#!/usr/bin/env python
# -*-coding:utf-8-*-
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    kwargs = dict(
        name='HANAZAWA KANA',
        age=30,
        sex='Girl'
    )
    return render_template('index.html', **kwargs)


if __name__ == '__main__':
    app.run(debug=True)