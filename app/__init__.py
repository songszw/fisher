# @Time    : 2019/12/10 下午4:24
# @Author  : songszw 
# @Email   : songszw315@live.com
from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config.from_object('config')
    register_blueprint(app)
    return app


def register_blueprint(app):
    from app.web.book import web
    app.register_blueprint(web)
