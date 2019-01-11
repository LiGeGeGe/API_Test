#-*- coding:utf-8 -*-
'''
    主题：创建第一个case，用例框架unittest
    日期：2109/1/11
    创建人：test
'''

__author__ = 'lixue'
import unittest
import requests
from BeautifulReport import BeautifulReport



class Apitest(unittest.TestCase):


    def test_GetBookListByCreateTime_Pkay(self):
        response = requests.post("http://api.test.edu.wanfangdata.com.cn/api/Huitu/GetBookListByCreateTime")
        status_code = response.status_code
        print(status_code)
        if status_code == 500:
            print(u"测试通过,直接访问URL不加参数状态码为500")
        else:
             print(u"测试失败")
    def test_etBookListByCreateTime_Pkayfailure(self):

        response = requests.post("http://api.test.edu.wanfangdata.com.cn/api/Huitu/GetBookListByCreateTime",)




if __name__ == '__main__':
    p=Apitest()
    p.test_GetBookListByCreateTime_Pkay()
    test = unittest.TestSuite()#
    test.addTest(Apitest("test_GetBookListByCreateTime_Pkay"))
    test_suite = unittest.defaultTestLoader.discover('../API_Case/',pattern='ApiTest*.py')#discover方法找到path目录下所有测试用例组装到测试套件
    result = BeautifulReport(test_suite)
    result.report(filename='测试报告', description='测试deafult报告', log_path='../API_TestReport/')
