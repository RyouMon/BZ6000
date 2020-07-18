#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, render_template
from datetime import datetime


app = Flask(__name__)


@app.route('/')
def index():
    kwargs = {
        'ps': '',  # default filter
        'number': -1,  # abs filter
        'xml': '<script>alert("hello")</script>', # escape filter, safe filter, striptags filter
        'person': ['Kana', 'Aki', 'Inori'],  # first filter, last filter, length filter
        'words': 'Fuck you!',  # replace filter, truncate filter
        'time1': '2019-06-01 12:23:33',
        'time2': '2020-03-01 12:23:33',
        'time3': '2020-07-01 12:23:33',
        'time4': '2020-07-14 12:23:33',
        'time5': '2020-07-18 05:23:33',
        'time6': '2020-07-18 12:23:33',
        'time7': '2020-07-18 12:59:33',
    }
    return render_template('index.html', **kwargs)


@app.template_filter()
def time_format(time):
    pattern = '%Y-%m-%d %H:%M:%S'
    current_time = datetime.strptime('2020-07-18 13:00:00', pattern)
    create_time = datetime.strptime(time, pattern)
    seconds = (current_time - create_time).total_seconds()
    if seconds < 60:
        return '刚刚'
    elif 60 < seconds < 60 * 60:
        return f'{int(seconds / 60)}分钟前'
    elif 60 * 60 < seconds < 60 * 60 * 60:
        return f'{int(seconds / 60 / 60)}小时前'
    elif 60 * 60 * 60< seconds < 60 * 60 * 60 * 24:
        return f'{int(seconds / 60 / 60 / 24)}天前'
    else:
        return '很久之前'


if __name__ == '__main__':
    app.run(debug=True)
