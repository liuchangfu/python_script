import redis

r = redis.Redis(host='192.168.57.129',port=6379)

r.set('foo','bar')
print(r.get('foo'))