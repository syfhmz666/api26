#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2024/4/18 14:23
# Author    : humengzhe
# @File     : xzs_login.py
# @Software : PyCharm
import requests
class xzs_login():
    def login(self,user,ps):
        url = "http://192.168.55.41:8000/api/user/login"
        header = {
            "Content - Type": "application / json"
        }
        data = {
            "userName": user, "password": ps, "remember": False
        }
        r = requests.post(url=url, headers=header, json=data)
        return r.text

if __name__ == '__main__':
    x = xzs_login()
    print(x.login('hmz', '123456'))