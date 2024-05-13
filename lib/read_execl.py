#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2024/4/23 11:28
# Author    : humengzhe
# @File     : read_execl.py
# @Software : PyCharm
import xlrd
# # 打开excel文件
# wb = xlrd.open_workbook("test_user_data.xlsx")
# # 读取工作薄
# sheet1 = wb.sheet_by_name("test_user_reg")
# # 行数
# print(sheet1.nrows)
# # 列数
# print(sheet1.ncols)
# # 输出第一行第一列
# print(sheet1.cell(0,0).value)
# # 输出第一行的所有值
# # print(sheet1.row_values(0))
# # print(dict(zip(sheet1.row_values(0),sheet1.row_values(1))))
# # 通过循环 把每一行的数据当列表输出
# for i in range (sheet1.nrows):
#     print(sheet1.row_values(i))
class readexcel():

    def excel_to_list(self,data_file,sheet):
        wb = xlrd.open_workbook(data_file)
        sheet1 = wb.sheet_by_name(sheet)
        # 获取第一行的数据
        keys= sheet1.row_values(0)
        list1 =[]
        # 从第二行开始获取数据
        for i in range(1,sheet1.nrows):
            j = dict(zip(keys,sheet1.row_values(i)))
            # print(j)
            list1.append(j)
        return list1

    def get_test_data(self,data_list,case_name):
        for case_data in data_list:
            if case_name == case_data['case_name']:
                return case_data

if __name__ == '__main__':
    r = readexcel()
    l = r.excel_to_list("./test_user_data.xlsx","test_user_login")
    # print(r.get_test_data(l,'log_ok'))
    print(l)
    t=""
    print(l[0]["case_name"])
    for i in range(len(l)):
        t+=l[i]["case_name"]+","
    print(t[:-1])