# -*- coding:utf-8 -*-
'''

'''
from Config import Readconfig
class Url():
    def __int__(self):
        get = Readconfig.Read_config()
        self.url = get.__int__()

    def get_GetBookListByCreateTime(self):
        host = self.get("http_config.ini","HTTP","host")
        path = get.__int__("http_config.ini","HTTP","path")
        url = host + path
        return url #返回url
