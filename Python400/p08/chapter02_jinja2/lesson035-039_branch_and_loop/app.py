#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    kwargs = {
        'age': 19,
        'users': ['KANA', 'AKI', 'INORI'],
        'person': {
            'Name': 'KANA',
            'Age': 30,
            'Sex': 'Female'
        }
    }
    return render_template('index.html', **kwargs)


if __name__ == '__main__':
    app.run(debug=True)
