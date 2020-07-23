#!/usr/bin/env python
# -*-coding:utf-8-*-
from flask import Flask, render_template, make_response, request


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/set_cookie')
def set_cookie():
    response = make_response('Pass username to cookie.')
    response.set_cookie('username', 'kana')
    return response


@app.route('/get_cookie')
def get_cookie():
    cookie = request.cookies
    username = cookie.get('username')
    return f'The username is {username}'


if __name__ == '__main__':
    app.run(debug=True)