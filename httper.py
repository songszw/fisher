# @Time    : 2019/12/10 下午3:08
# @Author  : songszw 
# @Email   : songszw315@live.com 


import requests


class HTTP:
    @staticmethod
    def get(url, return_json=True):
        r = requests.get(url)
        if r.status_code != 200:
            return {} if return_json else ''
        return r.json() if return_json else r.text
