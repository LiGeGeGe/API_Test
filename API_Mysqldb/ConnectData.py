#-*- coding:UTF-8 -*-

from API_Mysqldb import Setting
import urllib3
import pymysql



connect = Setting.DATABASE
# 打开数据库连接
db  = pymysql.connect(host= connect.get("host"),
                    port=connect.get("port"),
                    user=connect.get("user"),
                    password=connect.get("password"),
                    db=connect.get("db"),
                    charset=connect.get("charset")
                    )




# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
sql = "SELECT %s FROM  user  WHERE user_id =  000fox" % "user_id"
cursor.execute(sql)# 使用 execute() 方法执行SQL查询
#使用fetchone()方法获取表单数据
data = cursor.fetchone()
data1 = str(data)
print(data1)
print(type(data1))
# 关闭数据库连接
db.close()