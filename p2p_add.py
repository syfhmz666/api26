#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2024/4/22 17:13
# Author    : humengzhe
# @File     : p2p_add.py
# @Software : PyCharm
import requests
class p2p_add():
    def add(self,key,key1,key2,key3):
        url = "http://192.168.55.41:8081/p2p_management/addProduct"
        header = {
            "Content-Type: application/json"
        }
        data = {
            "proNum":key,"proName":key1,"proLimit":key2,"annualized":key3
        }
        r = requests.post(url=url, headers=header, json=data)
        return r.text

if __name__ == '__main__':
    a = p2p_add()
    a.add()