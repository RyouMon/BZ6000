#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, g, request, url_for, render_template

app = Flask(__name__)


# g的生命周期与current_app相同
# 可以在任意位置进行访问
@app.route('/')
def index():
    name = request.args.get('name')
    if name:
        g.name = name
        return render_template('index.html', **set_name())
    return 'access http://127.0.0.1:5000/?name=liang wen'


def set_name():
    name = g.get('name')
    family_name = lambda x: x.split(' ')[0]
    given_name = lambda x: x.split(' ')[1]
    return {
        'fullname': name,
        'family_name': family_name(name),
        'given_name': given_name(name)
    }


if __name__ == '__main__':
    app.run(debug=True)
