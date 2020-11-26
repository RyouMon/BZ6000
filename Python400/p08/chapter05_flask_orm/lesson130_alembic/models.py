from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine('sqlite:///test.db')
Base = declarative_base(engine)


class Student(Base):
    __tablename__ = 'student'
    _id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
