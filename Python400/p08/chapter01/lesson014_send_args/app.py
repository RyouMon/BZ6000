"""
传参的三种方式
"""
from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/<username>/<repo>')
def repo(username, repo):
    """
    通过地址传参
    """
    return "您通过路径传递的参数为{0}:{1}".format(username, repo)


@app.route('/search')
def search():
    """
    通过查询参数传参
    """
    key = request.args.get("kw")
    return "您搜索的关键字为{}".format(key)


@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    通过POST的FORM表单传参
    """
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        return 'Your username is {0}, password is {1}'.format(username, password)


if __name__ == '__main__':
    app.run()
