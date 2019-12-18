"""
@Time    : 2019/12/10 下午3:54
@Author  : songszw
@Email   : songszw315@live.com
"""
import json

from flask import jsonify, request, render_template, flash

from app.forms.book import SearchForm
from app.view_models.book import BookViewModel, BookCollection
from . import web
from app.libs.helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook


@web.route('/book/search', methods=['GET', 'POST'])
def search():
    """
    q:普通搜索  or  isbn搜索
    page
    ?q=金庸&page=1
    :return:
    """
    form = SearchForm(request.args)
    books = BookCollection()
    if form.validate():
        q = form.q.data.strip()
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)
        yushu_book = YuShuBook()

        if isbn_or_key == 'isbn':
            yushu_book.search_by_isbn(q)
        else:
            yushu_book.search_by_keyword(q, page)

        books.fill(yushu_book, q)
    else:
        flash('搜索的关键字不符合要求，请重新输入关键字')
    return render_template('search_result.html', books=books)


@web.route('/book/<isbn>/detail')
def book_detail(isbn):
    yushu_book = YuShuBook()
    yushu_book.search_by_isbn(isbn)
    if yushu_book.first:
        book = BookViewModel(yushu_book.first)
        return render_template('book_detail.html', book=book, wishes=[], gifts=[])

    # return json.dumps(book, default=lambda o: o.__dict__)


