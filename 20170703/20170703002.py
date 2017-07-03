import json
#示例表达序列化1：
d1 = {'name':'xuyuanyuan','age':18}
s1 = json.dumps(d1)
print(s1)

#示例表达序列化2：
d2 = {'name':'xuyuanyuan','age':18}
f=open(r'e:\python_txt\new1','w')
json.dump(d2,f)
f.close()

#示例表达反序列化：
f1 = open(r'e:\python_txt\new1','r')
date =f1.read()
res = json.loads(date)
print(res['name'])
print(res['age'])
