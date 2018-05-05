"""
获取多条数据，存入列表
"""
import pymysql

# 定义空列表，用来存储数据库中的数据
sql_list = []
# 定义数据库链接
db = pymysql.connect('192.168.10.16', 'root', 'etlx29_st4x6su', 'siteportal_vip')
# 定义查询语句
sql = 'select period,numbers from l_xjssc_winning_number limit 5 '
# 使用cursor()方法获取操作游标,为字典类型
cursor = db.cursor(pymysql.cursors.DictCursor)
# 执行SQL语句
count = cursor.execute(sql)
# 获取所有记录，数据类型为元组
res = cursor.fetchall()
# 把元组转换成列表
res1 = list(res)
# 循环把res1的结果追加到sql_list中
for i in res1:
    sql_list.append(i)
print(sql_list)
