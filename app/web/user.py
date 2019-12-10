# @Time    : 2019/12/10 下午5:14
# @Author  : songszw 
# @Email   : songszw315@live.com
from . import web


@web.route('/login')
def login():
    return 'login'

