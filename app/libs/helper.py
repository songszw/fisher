"""
@Time    : 2019/12/11 上午11:29
@Author  : songszw
@Email   : songszw315@live.com
"""


def is_isbn_or_key(word):
    """
    判断查询字段为isbn还是关键字
    :param word:
    :return:
    """
    isbn_or_key = 'keyword'
    if len(word) == 13 and word.isdigit():
        isbn_or_key = 'isbn'
    short_word = word.replace('-', '')
    if '-' in word and len(short_word) == 10 and short_word.isdigit():
        isbn_or_key = 'isbn'
    return isbn_or_key
