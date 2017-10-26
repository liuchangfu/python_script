import pymysql
#创建连接
conn = pymysql.connect(host='127.0.0.1',user='root',passwd='',db='test')
#创建游标
cursor = conn.cursor()
#执行SQL
cursor.execute('select * from student')
#获取第一行数据
print(cursor.fetchone())
#获取前N行数据
print(cursor.fetchmany(3))
#获取前所有数据
print(cursor.fetchall())
#提交数据
conn.commit()
#关闭游标
cursor.close()
#关闭连接
conn.close()