# @Time    : 2019/12/10 下午4:25
# @Author  : songszw 
# @Email   : songszw315@live.com
from flask import Blueprint

web = Blueprint('web', __name__)

from app.web import book
from app.web import user
