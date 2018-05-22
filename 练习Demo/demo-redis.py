# _*_ coding:utf-8 _*_
import redis
import time

# host是redis主机，需要redis服务端和客户端都启动 redis默认端口是6379
r = redis.Redis(host="localhost", port=6379, decode_responses=True)
# key是"name" value是"junxi" 将键值对存入redis缓存
r.set("name", "junxi")
print(r["name"])
# 取出键name对应的值
print(type(r.get("name")))
print(r.get("name"))
print(type(r.get("name")))

pool = redis.ConnectionPool(host="localhost", port=6379, decode_responses=True)
r = redis.Redis(connection_pool=pool)

r.set("gender", "male")
print(r.get("gender"))

r.set('food','muton',ex=3)
print(r.get('food'))

r.set('food', 'beef', px=3)
print(r.get('food'))

# 如果键fruit不存在，那么输出是True；如果键fruit已经存在，输出是None
print(r.set('fruit', 'watermelon', nx=True))

# 如果键fruit已经存在，那么输出是True；如果键fruit不存在，输出是None
print((r.set('fruit', 'watermelon', xx=True)))

# fruit1不存在，输出为True
print(r.setnx('fruit1', 'banana'))

r.setex("fruit2", "orange", 5)
time.sleep(5)
# 5秒后，取值就从orange变成None
print(r.get('fruit2'))

r.mget({'k1': 'v1', 'k2': 'v2'})
# 这里k1 和k2 不能带引号 一次设置对个键值对 print(r.mget("k1", "k2")) # 一次取出多个键对应的值
r.mset(k1="v1", k2="v2")
print(r.mget("k1"))

print(r.mget('k1', 'k2'))
print(r.mget(['k1', 'k2']))
# 将目前redis缓存中的键对应的值批量取出来
print(r.mget("fruit", "fruit1", "fruit2", "k1", "k2"))

# 设置的新值是barbecue,设置前的值是beef
print(r.getset("food", "barbecue"))
