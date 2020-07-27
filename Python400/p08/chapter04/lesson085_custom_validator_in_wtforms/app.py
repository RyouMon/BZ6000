#!/usr/bin/env python
# -*- coding: utf-8 -*-
from random import randint
from flask import Flask, render_template, request, session
from wtforms.form import Form
from wtforms.fields import IntegerField
from wtforms.validators import ValidationError


app = Flask(__name__)
app.secret_key = b'\xc8]\xc3Z\xc5\xb7\x1f\xa7\xbaIu]\x10b\xcbl'


class CodeForm(Form):
    code = IntegerField()

    def validate_code(self, field):
        code = field.data
        if code == session['code']:
            pass
        else:
            raise ValidationError('Input the correct code please.')


@app.route('/')
def index():
    code = randint(1000, 9999)
    session['code'] = code
    return render_template('index.html', code=code)


@app.route('/validator/', methods=['POST'])
def validator():
    form = CodeForm(request.form)
    if form.validate():
        return '验证通过'
    else:
        return '验证失败：' + str(form.errors)


if __name__ == '__main__':
    app.run(debug=True)
