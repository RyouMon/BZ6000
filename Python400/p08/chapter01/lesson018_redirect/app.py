#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, redirect, url_for


app = Flask(__name__)


@app.route('/')
def index():
    return redirect(url_for('login'))


@app.route('/login')
def login():
    return 'Login Page'


if __name__ == '__main__':
    app.run()
