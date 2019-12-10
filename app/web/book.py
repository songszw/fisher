# @Time    : 2019/12/10 下午3:54
# @Author  : songszw 
# @Email   : songszw315@live.com
from flask import jsonify, Blueprint

from helper import is_isbn_or_key
from yushu_book import YuShuBook

web = Blueprint('web', __name__)


@web.route('/book/search/<q>/<page>')
def search(q, page):
    """
    q:普通搜索  or  isbn搜索
    page
    :return:
    """
    isbn_or_key = is_isbn_or_key(q)
    if isbn_or_key == 'isbn':
        result = YuShuBook.search_by_isbn(q)
    if isbn_or_key == 'keyword':
        result = YuShuBook.search_by_keyword(q)
    return jsonify(result)

