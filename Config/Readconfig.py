# -*- coding:utf-8 -*-

'''
如果ini文件里面写的是数字，读出来默认是字符串
'''
__author__ = 'test'


import  os #配置文件路径得模块
import configparser#读取ini文件得模块
class Read_config():

    def __int__(self,config_ini,section,key):
        #创建管理对象
        config = configparser.ConfigParser()
        #获取文件路径
        filepath = os.path.dirname(os.path.realpath(__file__))

        try:
            cfpath = os.path.join(filepath,config_ini)  #配置文件
            config.read(cfpath)
            t = config.items(section) #获取制定节点得键值对
            # section = config.sections()
            # print(section) #获取节点名称
            if t != []:

                self.value = config.get(section,key) #获取指定节点value值
                return self.value
                #print(self.value)
                # options = config.options(section[0])
                # print(options[0:3]) #获取0到3得key值

            else:
                print(section + "为空")

        except Exception as e:
            print(e)





    def R_config(self):
        return self.value

    #     print(cfpath)
    #     #读取配置文件
    #     config.read(cfpath)
    #     # #config.read('../Config' + file,encoding="utf-8")
    #     t = config.items(section)
    #     print(t)
    #     items = config.options(key)
    #     print(items)

if __name__ == '__main__':
    a = Read_config()

    # a.__int__()
    a.get_GetBookListByCreateTime()
    # Readconig().R_config("db_config.ini","DATABASE","host")


