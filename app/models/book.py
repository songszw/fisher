""" 
@Time    : 2019/12/11 上午11:29
@Author  : songszw 
@Email   : songszw315@live.com 
"""
from sqlalchemy import Column, Integer, String

from app.models.base import db


class Book(db.Model):
    """
    id
    title:书名
    author:作者
    binding:装订版本（精装/平装）
    publisher:出版社
    price:价格
    pages:页数
    pubdate:出版年月
    isbn:isbn编号
    summary:简介
    image:封面图
    """
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    author = Column(String(30))
    binding = Column(String(20))
    publisher = Column(String(50))
    price = Column(String(20))
    pages = Column(Integer)
    pubdate = Column(String(20))
    isbn = Column(String(15), nullable=False, unique=True)
    summary = Column(String(1000))
    image = Column(String(50))





