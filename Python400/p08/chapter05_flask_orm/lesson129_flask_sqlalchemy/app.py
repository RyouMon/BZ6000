# flask_sqlalchemy 的基本使用
# 1 建立数据库连接
# 2 定义 ORM 模型
# Last update：2020/11/26

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///test.db'

db = SQLAlchemy(app)

class Student(db.Model):
    __tablename__ = 'student'
    _id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer())

    def __repr__(self):
        return '<Student {name}>'.format(name=self.name)


# 迁移数据库
# >>> from app import db
# >>> db.create_all()

# 创建对象
# >>> from app import Student
# >>> kana = Student(name="kana", age=18)
# >>> aki = Student(name="aki", age=19)

# 保存对象
# >>> db.session.add(kana)
# >>> db.session.add(aki)
# >>> db.session.commit()

# 查询对象
# >>> Student.query.all()
# [<Student kana>, <Student aki>]
# >>> Student.query.filter_by(name="kana").first()
# <Student kana>
# >>> db.session.query(Student).order_by(Student.age.desc()).all()
# [<Student aki>, <Student kana>]
# >>> db.session.query(Student).filter_by(name="aki").first()
# <Student aki>

# 销毁数据库
# >>> db.drop_all()
