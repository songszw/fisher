"""
@Time    : 2019/12/11 上午11:29
@Author  : songszw
@Email   : songszw315@live.com
"""
from wtforms import Form, StringField, IntegerField
from wtforms.validators import Length, NumberRange, DataRequired


class SearchForm(Form):
    q = StringField(validators=[DataRequired(message='搜索关键字为必填')])
    page = IntegerField(validators=[NumberRange(min=1)], default=1)
