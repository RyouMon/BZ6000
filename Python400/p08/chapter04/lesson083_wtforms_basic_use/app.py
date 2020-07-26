#!/usr/bin/env python
# -*-coding:utf-8-*-
from flask import Flask, render_template, request
from wtforms.form import Form
from wtforms.fields import StringField
from wtforms.validators import Length, EqualTo


app = Flask(__name__)


# 1 定义一个Form的子类
class RegisterFrom(Form):
    # 2 定义字段名、字段类型及验证器
    uname = StringField(validators=[Length(2, 5)])
    pwd = StringField(validators=[Length(6, 12)])
    pwd2 = StringField(validators=[EqualTo('pwd')])


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/register/', methods=['POST'])
def register():
    # 3 使用request.form实例化自定义类RegisterFrom
    form = RegisterFrom(request.form)
    # 4 使用validate()方法验证表单是否通过
    if form.validate():
        return '注册成功'
    else:
        # 5 使用errors属性返回验证不通过的原因
        return '注册失败：' + str(form.errors)


if __name__ == '__main__':
    app.run(debug=True)