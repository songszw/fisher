""" 
@Time    : 2019/12/27 下午3:42
@Author  : songszw 
@Email   : songszw315@live.com 
"""
from app.view_models.book import BookViewModel


class MyWishes:
    def __init__(self, wishes_of_mine, wishes_count_list):
        self.wishes = []
        self.__wishes_of_mine = wishes_of_mine
        self.__wishes_count_list = wishes_count_list
        self.wishes = self.__parse()

    def __parse(self):
        temp_wishes = []
        for wish in self.__wishes_of_mine:
            my_wish = self.__matching(wish)
            temp_wishes.append(my_wish)
        return temp_wishes

    def __matching(self, wish):
        count = 0
        for wish_count in self.__wishes_count_list:
            if wish.isbn == wish_count['isbn']:
                count = wish_count['count']
        r = {
            'wishes_count': count,
            'book': BookViewModel(wish.book),
            'id': wish.id
        }
        return r

