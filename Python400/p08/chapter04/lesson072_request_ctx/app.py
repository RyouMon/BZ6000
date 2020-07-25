#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def index():
    url = request.url
    return f'access {url}'


with app.test_request_context('http://127.0.0.1:5000/'):
    url = request.url
    print(f'access {url}')


if __name__ == '__main__':
    app.run(debug=True)
