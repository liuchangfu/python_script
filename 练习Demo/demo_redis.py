# _*_ coding:utf-8 _*_
from redis import StrictRedis

redis = StrictRedis(host='localhost',port=6379,db=1,password='')

redis.set('name','Bob')
print(redis.get('name'))