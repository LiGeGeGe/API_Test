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
#字典，只不过是字典里面嵌套着字典、列表，列表里面有嵌套着字典
#pkey需要开发设置时效

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
        print("Success:" + str(json_response["Success"]))
        succes = json_response["Success"]
        print("Message:" + str(json_response["Message"]))
        print("PageCount:" + str(json_response["PageCount"]))
        print("PageNumber:" + str(json_response["PageNumber"]))
        print("PageSize:" + str(json_response["PageSize"])) #获取json中某个值，获取检索结果数

        assert json_response["Success"] == True #断言方法
        assert json_response["Message"] == "已完成"
        assert json_response["Message"] == "已完成"

    def test_GetBookListByCreateTime_MissingValueStarTime(self):#缺少开始时间
        requests_host = Apitest().requests()
        data = {'endTime':'1506787200','PageNumber':'','PageSize':'','pkey':'ODgsMTMwLDEzNiwxNDAsMTcxLDEzMCwxNzIsMTQxLDEwOCwxMzQ=','organid':'e'}
        response = requests.post(url=requests_host,data=data)
        json_response = response.json()
        '''
        打印值
        '''
        print("Success:" + str(json_response["Success"]))
        print("Message:" + str(json_response["Message"]))
        print("PageCount:" + str(json_response["PageCount"]))
        print("PageNumber:" + str(json_response["PageNumber"]))
        print("PageSize:" + str(json_response["PageSize"])) #获取json中某个值，获取检索结果数
        '''
        断言返回信息得key得value
        '''
        assert json_response["Success"] == False
        assert json_response["Message"] == "开始时间为空或超出有效Unix时间戳范围，请求无效！"

    def test_GetBookListByCreateTime_MissingValueEndTime(self):#缺少结束时间
        requests_host = Apitest().requests()
        data = {'StartTime':'946656000','PageNumber':'','PageSize':'','pkey':'ODgsMTMwLDEzNiwxNDAsMTcxLDEzMCwxNzIsMTQxLDEwOCwxMzQ=','organid':'e'}
        response = requests.post(url=requests_host,data=data)
        json_response = response.json()
        '''
        打印值
        '''
        print("Success:" + str(json_response["Success"]))
        print("Message:" + str(json_response["Message"]))
        print("PageCount:" + str(json_response["PageCount"]))
        print("PageNumber:" + str(json_response["PageNumber"]))
        print("PageSize:" + str(json_response["PageSize"])) #获取json中某个值，获取检索结果数
        '''
        断言返回信息得key得value
        '''
        assert json_response["Success"] == False
        assert json_response["Message"] == "结束时间为空或超出有效Unix时间戳范围，请求无效！"

    def test_GetBookListByCreateTime_StarTimeLessThanEndTime(self):#开始时间大于结束时间
        requests_host = Apitest().requests()
        data = {'StartTime':'1506787200','endTime':'946656000','PageNumber':'','PageSize':'','pkey':'ODgsMTMwLDEzNiwxNDAsMTcxLDEzMCwxNzIsMTQxLDEwOCwxMzQ=','organid':'e'}
        response = requests.post(url=requests_host,data=data)
        json_response = response.json()
        '''
        打印值
        '''
        print("Success:" + str(json_response["Success"]))
        print("Message:" + str(json_response["Message"]))
        print("PageCount:" + str(json_response["PageCount"]))
        print("PageNumber:" + str(json_response["PageNumber"]))
        print("PageSize:" + str(json_response["PageSize"])) #获取json中某个值，获取检索结果数
        '''
        断言返回信息得key得value
        '''
        assert json_response["Message"] == "开始时间超出结束时间，请求无效！"
        assert json_response["Success"] == False





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
    p.test_GetBookListByCreateTime_MissingValueStarTime()
    p.test_GetBookListByCreateTime_MissingValueEndTime()
    p.test_GetBookListByCreateTime_StarTimeLessThanEndTime()
    # p.est_AetBookListByCreateTime_Pkayfailure()


    # test = unittest.TestSuite()#
    # test.addTest(Apitest("test_GetBookListByCreateTime_Pkay"))

    # test_suite = unittest.defaultTestLoader.discover('../API_Case/',pattern='ApiTest*.py')#discover方法找到path目录下所有测试用例组装到测试套件
    # result = BeautifulReport(test_suite)
    # result.report(filename='测试报告', description='GetBookListByCreateTime接口报告', log_path='../API_TestReport/')
