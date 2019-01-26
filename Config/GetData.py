#-*- coding:UTF-8 -*-
'''

'''
#__author__ = 'lixue'



import xlwt
import xlrd
import requests


#整个excel文件，转化为一个字典结构：每个key就是一个子表（Sheet）
#每个子表（Sheet），转化为一个二维数组：分别为行和列。
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

class Data(object):

    def Sheet(self,file):
        FileName = '../Data/' + file
        Excel = xlrd.open_workbook(FileName)

    def GetData(self,line,column):
        Excel = Data.Sheet()
        Sheet = Excel.sheet_by_index(0) #根据顺序获取sheet
        result = Sheet.cell(line,column).value #指定行和列获取数据
        return result


    def GetData(self,file,name,line,column):
        FileName = '../Data/' + file
        Excel = xlrd.open_workbook(FileName)
        Sheet = Excel.sheet_by_name(name)
        result = Sheet.cell(line,column).value#指定行和列，获取数据
        return result


    def ForData(self,file):
        FileName = '../Data/' + file
