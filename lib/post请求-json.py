#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2024/4/15 15:59
# Author    : humengzhe
# @File     : post请求-json.py
# @Software : PyCharm
import requests

url = "http://httpbin.org/post"
data = '''{
    "name":"zhangsan",
    "age":"18"
}'''
# 多行文本，字符串格式，也可以单行（注意外层又引号，为字符号）data=
'{"name":"zhangsan","age":18}'

r = requests.post(url=url,data=data)
print(r.text)