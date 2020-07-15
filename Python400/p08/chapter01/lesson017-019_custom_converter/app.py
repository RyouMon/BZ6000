#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, url_for
from werkzeug.routing import BaseConverter, UnicodeConverter


class PhoneNumberConverter(BaseConverter):
    regex = r'1[2358]\d{9}'


class SplitAndConverter(UnicodeConverter):
    def to_python(self, value):
        return value.split('&')

    def to_url(self, value):
        return '&'.join(value)


app = Flask(__name__)

# 注册自定义转换器
app.url_map.converters['phone'] = PhoneNumberConverter
app.url_map.converters['split_and'] = SplitAndConverter


@app.route('/')
def index():
    return '<a href="http://127.0.0.1:5000{0}">test phone converter</a> <br>' \
           '<a href="http://127.0.0.1:5000/{1}">test to python method</a>'.format(
        url_for('matching_phone_number', number=13785629912),
        '花澤香菜&豊崎愛生&水瀬いのり',
    )


@app.route('/<phone:number>')
def matching_phone_number(number):
    return f'Your phone number is {number}.'


@app.route('/<split_and:string>')
def test_to_python_method(string):
    words = ' + '.join(string)
    url = 'http://localhost:5000' + url_for('test_to_python_method', string=['花澤香菜', '豊崎愛生', '水瀬いのり'])
    return 'You\'re accessed the url: "{0}". Words are {1}.'.format(url, words)


if __name__ == '__main__':
    app.run()
