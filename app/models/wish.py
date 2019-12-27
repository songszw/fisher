""" 
@Time    : 2019/12/19 下午5:17
@Author  : songszw 
@Email   : songszw315@live.com 
"""
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, desc, func
from sqlalchemy.orm import relationship

from app.models.base import Base, db
from app.spider.yushu_book import YuShuBook


class Wish(Base):
    id = Column(Integer, primary_key=True)
    user = relationship('User')
    uid = Column(Integer, ForeignKey('user.id'))
    isbn = Column(String(15), nullable=False)
    launched = Column(Boolean, default=False)

    @classmethod
    def get_user_wishes(cls, uid):
        wishes_list = Wish.query.filter_by(
            launched=False, uid=uid).order_by(
            desc(Wish.create_time)).all()
        return wishes_list

    @classmethod
    def get_gifts_count(cls, isbn_list):
        from app.models.gift import Gift
        count_list = db.session.query(
            func.count(Gift.id), Gift.isbn).filter(
            Gift.isbn.in_(isbn_list),
            Gift.launched == False, Gift.status == 1).group_by(
            Gift.isbn).all()
        count_list = [{'count': w[0], 'isbn': w[1]} for w in count_list]
        return count_list

    @property
    def book(self):
        yushu_book = YuShuBook()
        yushu_book.search_by_isbn(self.isbn)

        return yushu_book.first
