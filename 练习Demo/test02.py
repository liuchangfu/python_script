import json

data ={
	'no':1,
	'name':'Runoob',
	'rul':'http://www.ruboob.com'
}

json_str = json.dumps(data)
print('Python原始数据:',repr(data))
print('JSON对象:',json_str)

