# from __future__ import division
#
# def methic(x,y,oper):
#     result = {
#         '+':x+y,
#         '-':x-y,
#         '*':x*y,
#         '/':x/y
#     }
#     return result.get(oper)
# print(methic(1,2,'+'))

# str1 = 'Hello world'
# print(str1[0:3])
# print(str1[::2])

# spam  = 10
# if spam == 10:
#     print('eggs')
#     if spam > 5:
#         print('bacon')
#     else:
#         print('ham')
#     print('spam')
# print('spam')

import pymysql

conn = pymysql.connect(host='127.0.0.1',user='root',passwd='',db='test')

cur = conn.cursor()

recount = cur.execute('select * FROM student')

nret = cur.fetchall()

#conn.commit()
cur.close()
conn.close()

print(recount)
print(nret)

for i in nret:
    print(i[0],i[1],i[2],i[3])