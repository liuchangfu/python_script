# _*_ coding:utf-8 _*_
import memcache
mc = memcache.Client(['192.168.1.113:11211'],debug=True)
# 插入
mc.set("name","python")
# 读取
ret = mc.get("name")
print(ret)

mc.add('k1','v1')
mc.add('k2','v2')