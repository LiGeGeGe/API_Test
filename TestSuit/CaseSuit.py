#-*- coding:UTF-8 -*-
import unittest
import sys
import time
import  os

from TestReport.HtmlReport import BeautifulReport
Test_Case = "../TestCase"

file =  unittest.defaultTestLoader.discover(Test_Case,pattern='test*.py',top_level_dir=None)
Begin_Time = time.strftime("%Y-%m-%d %H_%M_%S")




if __name__ == '__main__':
    suit = unittest.TestSuite()
    suit.addTest(file)
    rets = BeautifulReport(suit)
    rets.report(filename="{}.html".format(Begin_Time))
    #发送邮件
    E_emai(filenmail="{}.html".format(Begin_Time))

