#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2024/4/15 16:21
# Author    : humengzhe
# @File     : 4.15-带参数的get请求-tpshop.py
# @Software : PyCharm
import requests
# url = "http://192.168.55.42/Home/Goods/search.html?q=%25E6%2589%258B%25E6%259C%25BA"


url = "http://192.168.55.42/Home/Goods/search.html"

pama={
    "q":"%25E6%2589%258B%25E6%259C%25BA"
}

r = requests.get(url,params=pama)
print(r.text)