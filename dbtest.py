import pymysql

conn = pymysql.connect(host= "localhost", port=3307, user="root", password="0955", db="covid", charset="utf8")

#커서 가져오기
cursor=conn.cursor()
# sql 만들기
sql="select * from login"
cursor.execute(sql)

result=cursor.fetchall()
for res in result:
    print(res)
conn.close()
