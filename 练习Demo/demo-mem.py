# _*_ coding:utf-8 _*_
import memcache
mc = memcache.Client(['192.168.1.113:11211'],debug=True)
# 插入
mc.set("name","python")
# 读取
ret = mc.get("name")
print(ret)
# 增加
ret1 = mc.add('name1','python')
print(ret1)
# 增加，如果已经存在的key，重复执行add操作会出现异常
ret2 = mc.add('name2','java')
print(ret2)