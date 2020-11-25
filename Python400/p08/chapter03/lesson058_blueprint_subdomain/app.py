#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask
from blueprints import user


app = Flask(__name__)
app.register_blueprint(user.user_bp)
app.config['SERVER_NAME'] = 'wen.com:5000'


if __name__ == '__main__':
    app.run(debug=True)
