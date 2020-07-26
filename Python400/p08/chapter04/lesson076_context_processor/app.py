#!/usr/bin/env python
# -*-coding:utf-8-*-
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.context_processor
def pass_args():
    return {
        'username': 'kana',
        'age': 18
    }

if __name__ == '__main__':
    app.run(debug=True)