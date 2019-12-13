"""
@Time    : 2019/12/11 上午11:29
@Author  : songszw
@Email   : songszw315@live.com
"""
from app import create_app

app = create_app()


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=app.config['DEBUG'])
