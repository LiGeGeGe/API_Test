#-*- coding:UTF-8 -*-
'''

'''
#__author__ = 'lixue'



import xlwt
import xlrd
import requests
'''
book = xlrd.open_workbook('stu.xls') #打开一个excel
sheet = book.sheet_by_index(0) #根据顺序获取sheet
sheet2 = book.sheet_by_name('sheet1') #根据sheet页名字获取sheet
print(sheet.cell(0,2).value) #指定行和列获取数据
print("行数：%s"% sheet.ncols) #获取excel里面有多少列
print("列数：%s"% sheet.nrows) #获取excel里面有多少行
print(sheet.row_values(2))#取第几行的数据
print(sheet.col_values(2)) #取第几列的数据
for i in range(sheet.nrows): # 0 1 2 3 4 5
    print(sheet.row_values(i)) #取第几行的数据
'''

class RequestsMethods(object):



    def Runsqlscript(self,sqlfile):
        file = '../Data/' + sqlfile #获取sql语句
        return  file


    def Assert(self,key,text,url,data):#断言方法
        response = requests.post(url=url,data=data)
        json_response = response.json()
        assert json_response[key] == text


    def requests(self,url,data,header=None):#post与get封装
        response = None
        if header != None:
            response = requests(url=url,data=data,header=header)
            return response
        else:
            if requests == 'post':
                response = requests.post(url=url,data=data)
            else:
                response = requests.get(url=url,data=data)
            result = response.text()
            return result
    def post