#!/usr/bin/env python
# -*-coding:utf-8-*-
from flask import Flask, request, render_template
from wtforms.form import Form
from wtforms.fields import StringField, IntegerField
from wtforms.validators import Length, URL, Email, NumberRange, Regexp


app = Flask(__name__)


class RegisterForm(Form):
    name = StringField(validators=[Length(2,4)])
    age = IntegerField(validators=[NumberRange(0, 100)])
    phone = StringField(validators=[Regexp(r'1[358]\d{9}')])
    mail = StringField(validators=[Email()])
    personal_page = StringField(validators=[URL()])


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/register/', methods=['POST'])
def register():
    form = RegisterForm(request.form)
    if form.validate():
        return '提交成功'
    else:
        return '提交失败：' + str(form.errors)


if __name__ == '__main__':
    app.run(debug=True)