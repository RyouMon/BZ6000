#!/usr/bin/env python
# -*- coding: utf-8 -*-
from random import choice
from flask import Flask, render_template
from flask.views import View


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


class ADView(object):
    ads = [
        '世界失去联想，人类将会怎样？',
        '猿辅导，全球累积用户超过四亿',
        '小天才，能拍摄的电话手表',
        '涨知识了，芝士酸奶'
    ]


class LoginView(View, ADView):
    def dispatch_request(self):
        ad = choice(self.ads)
        return render_template('login.html', ad=ad)


class SignUpView(View, ADView):
    def dispatch_request(self):
        ad = choice(self.ads)
        return render_template('signup.html', ad=ad)


app.add_url_rule('/login', view_func=LoginView.as_view('login'))
app.add_url_rule('/signup', view_func=SignUpView.as_view('sign_up'))


if __name__ == '__main__':
    app.run(debug=True)
