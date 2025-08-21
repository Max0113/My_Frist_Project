import pymysql

mydb =pymysql.connect(host='localhost',user='root',password='',database='test1')
curs = mydb.cursor()
curs.execute("CREATE TABLE student (name VARCHAR(255), address VARCHAR(255))")
mydb.commit
mydb.close



