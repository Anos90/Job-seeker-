import pymysql as sql
import methods

# print(methods.search("Pune","4-5","Public","Software Product"))
sql = sql.connect(user="root",password="",host = "localhost",port = 3306)
print(sql)