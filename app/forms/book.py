# @Time    : 2019/12/11 上午8:52
# @Author  : songszw 
# @Email   : songszw315@live.com 
from wtforms import Form, StringField, IntegerField
from wtforms.validators import Length, NumberRange, DataRequired


class SearchForm(Form):
    q = StringField(validators=[DataRequired(message='改字段为必填字段')])
    page = IntegerField(validators=[NumberRange(min=1)], default=1)
