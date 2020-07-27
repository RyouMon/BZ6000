#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, request, render_template
from flask.views import MethodView


app = Flask(__name__)


class UserAPI(MethodView):
    def get(self):
        return render_template('index.html')

    def post(self):
        name = request.form.get('username')
        return f'Already loggin, username: {name}'


app.add_url_rule('/', view_func=UserAPI.as_view('index'))
app.add_url_rule('/login', view_func=UserAPI.as_view('login'), methods=['POST', ])


if __name__ == '__main__':
    app.run(debug=True)

