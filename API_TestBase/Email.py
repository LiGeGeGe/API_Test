#-*- coding:UTF-8 -*-

import unittest
import smtplib
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from API_TestBase.TestBase import  Data
send = Data()

class TEST_Case(object):
    def __init__(self):
        pass
    The_sender = '{}'.format(send.detal("stu.xls","E_email",1,1))
    '''
        发件邮箱
    '''
    Authorization = "{}".format(send.detal("stu.xls","E_email",1,2))
    '''
        邮箱授权码
    '''
    The_recipient = '{}'.format(send.detal("stu.xls","E_email",1,0))
    '''
        收件邮箱
    '''
    TEH_TEST = '{}'.format(send.detal("stu.xls","E_email",1,4))
    '''
    邮件文本
    '''
    BODY = '{}'.format(send.detal("stu.xls","E_email",1,3))
    '''
        主题
    '''

class E_emai(TEST_Case):
    def __init__(self,sender = None,subject = None,receivers = None,
                email_content = None, content_type='plain', charset='utf-8',
                filenmail = None,passwd = None):
        TEST_Case.__init__(self)

        if sender is None:
            sender = self.The_sender
        else:
            sender = sender
        if receivers is None:
            receivers = self.The_recipient
        else:
            receivers = receivers
        if passwd is None:
            passwd = self.Authorization
        else:
            passwd = passwd
        if subject is None:
            subject = self.BODY
        else:
            subject = subject
        if email_content is None:
            email_content = self.TEH_TEST
        else:
            email_content = email_content
        #创建一个带附件的实例
        global msg
        msg = MIMEMultipart()
        msg['Subject'] = subject  # 主题
        msg['From'] = sender  # 发件邮箱
        msg['To'] = receivers  # 收件邮箱
        # 创建正文，将文本文件添加到MIMEMultipart中
        content = MIMEText(email_content, content_type, charset)
        msg.attach(content)
        # 构造附件1，传送当前目录下  文件
        # now = time.strftime("%Y-%m-%d %H_%M_%S")
        filename = "../TESTreport/" + filenmail
        att1 = MIMEText(open(filename, 'rb').read(), 'base64', 'utf-8')  # rb以二进制方式读取
        # att1["Content-Type"] = 'application/octet-stream'
        # filename为附件名称，可以任意写，写什么名字，邮件中显示什么名字
        # att1["Content-Disposition"] = 'attachment; filename = %s' % filename
        att1.add_header('Content-Disposition', 'attachment; filename="%s"' % filenmail)  # 给附件添加头文件
        # 将附件添加到MIMEMultipart中
        msg.attach(att1)
        #receivers = 'hao.fengkuang@foxmail.com'  # 收件邮箱
        try:
            s = smtplib.SMTP_SSL('smtp.qq.com', 465)
            s.set_debuglevel(1)  # 输出发送邮件详细过程
            s.login(sender, passwd)
            s.sendmail(sender, receivers, msg.as_string())
            print(u"发送成功")
        except:
            print(u"发送失败")