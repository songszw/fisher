""" 
@Time    : 2019/12/16 下午1:26
@Author  : songszw 
@Email   : songszw315@live.com 
"""
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import SmallInteger, Column, Integer, String


db = SQLAlchemy()


class Base(db.Model):
    __abstract__ = True
    status = Column(SmallInteger, default=1)

    def set_attrs(self, attrs_dict):
        for key, value in attrs_dict.items():
            if hasattr(self, key) and key != 'id':
                setattr(self, key, value)
