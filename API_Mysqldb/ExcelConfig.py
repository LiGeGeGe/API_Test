# -*- coding: utf-8 -*-

'''
 创建人：test
 主题：数据库配置，读取excel表中数据
 日期：2019/01/10
'''
__author__ = 'lixue'

from API_TestBase import HttpRequest
from API_Mysqldb import GetData

host = GetData.Data()
concet ={

 #   "ENGINE": host.GetData("stu.xls","mysqldb",1,0),
    "host": host.GetData("stu.xls","mysqldb",1,1),
    "port": int(host.GetData("stu.xls","mysqldb",1,2)),
    "user": host.GetData("stu.xls","mysqldb",1,3),
    "password": host.GetData("stu.xls","mysqldb",1,4),
    "db": host.GetData("stu.xls","mysqldb",1,5),
    "charset":host.GetData("stu.xls","mysqldb",1,6)


}

