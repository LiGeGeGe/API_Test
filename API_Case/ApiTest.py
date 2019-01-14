#-*- coding:utf-8 -*-
'''
    主题：创建第一个case，用例框架unittest
    日期：2109/1/11
    创建人：test
    改进：后期需要加一个循环判断返回的数据是json还是list列表
'''

__author__ = 'lixue'
import unittest
import requests
import json
from BeautifulReport import BeautifulReport
#json就是一个字典，只不过是字典里面嵌套着字典、列表，列表里面有嵌套着字典


class Apitest(unittest.TestCase):

    def  requests(self):
        host = "http://api.test.edu.wanfangdata.com.cn/api/" # host指固定的host地址或者ip+端口
        requests = "Huitu/GetBookListByCreateTime" #接口名称
        requests_host = host + requests # 请求URL
        return requests_host #返回参数

    def test_GetBookListByCreateTime_Pkay(self):
        requests_host = Apitest().requests()
        data = {'StartTime':'946656000','endTime':'1506787200','PageNumber':'','PageSize':'','pkey':'ODgsMTMwLDEzNiwxNDAsMTcxLDEzMCwxNzIsMTQxLDEwOCwxMzQ=','organid':'e'}
        response = requests.post(url=requests_host,data=data)
        json_response = response.json()

        print(json_response["TotalCount"]) #获取json中某个值















    def test_AetBookListByCreateTime_Ckayfailure(self):
        response = requests.post("http://api.test.edu.wanfangdata.com.cn/api/Huitu/GetBookListByCreateTime")
        print (response)
        str_response = response.content
        print(str_response)
        status_code = response.status_code
        print(status_code)

        if status_code == 400:
            print(u"测试失败")



    # def test_etBookListByCreateTime_Pkayfailure(self):
    #
    #     response = requests.post("http://api.test.edu.wanfangdata.com.cn/api/Huitu/GetBookListByCreateTime",)
    #     dic_response = response.json()
    #     errcode = dic_response["code"]
    #     print("errpr_code=="+str(errcode))


if __name__ == '__main__':
    p=Apitest()
    p.test_GetBookListByCreateTime_Pkay()
    # p.est_AetBookListByCreateTime_Pkayfailure()


    # test = unittest.TestSuite()#
    # test.addTest(Apitest("test_GetBookListByCreateTime_Pkay"))

    # test_suite = unittest.defaultTestLoader.discover('../API_Case/',pattern='ApiTest*.py')#discover方法找到path目录下所有测试用例组装到测试套件
    # result = BeautifulReport(test_suite)
    # result.report(filename='测试报告', description='GetBookListByCreateTime接口报告', log_path='../API_TestReport/')
