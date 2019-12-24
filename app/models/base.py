""" 
@Time    : 2019/12/16 下午1:26
@Author  : songszw 
@Email   : songszw315@live.com 
"""
from contextlib import contextmanager
from datetime import datetime

from flask import flash
from flask_sqlalchemy import SQLAlchemy as _SQLAlchemy
from sqlalchemy import SmallInteger, Column, Integer, String


class SQLAlchemy(_SQLAlchemy):
    @contextmanager
    def auto_commit(self):
        try:
            yield
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise e


db = SQLAlchemy()


class Base(db.Model):
    __abstract__ = True
    status = Column(SmallInteger, default=1)
    create_time = Column('create_time', Integer)

    def __init__(self):
        self.create_time = int(datetime.now().timestamp())

    def set_attrs(self, attrs_dict):
        for key, value in attrs_dict.items():
            if hasattr(self, key) and key != 'id':
                setattr(self, key, value)
