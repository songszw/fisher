""" 
@Time    : 2019/12/25 下午3:56
@Author  : songszw 
@Email   : songszw315@live.com 
"""


class TradeInfo:
    def __init__(self, goods):
        self.total = 0
        self.trades = []
        self.__parse(goods)

    def __parse(self, goods):
        self.total = len(goods)
        self.trades = [self.__map_to_single(good) for good in goods]

    def __map_to_single(self, single):
        if single.create_time:
            time = single.create_datetime.strftime('%Y-%m-%d')
        else:
            time = '未知'
        return dict(
            user_name=single.user.nickname,
            time=time,
            id=single.id
        )
