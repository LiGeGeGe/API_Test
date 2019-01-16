#-*- coding:UTF-8 -*-

from API_Mysqldb import ExcelConfig
import urllib3
import pymysql
# sql = TestBase.Data()
# sqlfile = sql.Runsqlscript("user.sql")

connect = ExcelConfig.concet
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
sql = "SELECT * FROM  user  WHERE user_id = '000fox' "
cursor.execute(sql)# 使用 execute() 方法执行SQL查询
#使用fetchone()方法获取表单数据
data = cursor.fetchone()
data1 = str(data)
print(data1)
print(type(data1))
# 关闭数据库连接
db.close()