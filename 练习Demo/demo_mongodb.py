from pymongo import MongoClient

# 连接数据库，地址，端口
client = MongoClient('localhost',27017)

# 指定数据库
db = client.pythondb

# 指定集合,类似于关系型数据库中的表
my_set = db.students

# 插入单条数据
student = {
    'id': '20170101',
    'name': 'Jordan',
    'age': 20,
    'gender': 'male'
}
print(my_set.insert(student))

# 插入多条数据
student1 = {
    'id': '20170101',
    'name': 'Jordan',
    'age': 20,
    'gender': 'male'
}
student2 = {
    'id': '20170202',
    'name': 'Mike',
    'age': 21,
    'gender': 'male'
}
print(my_set.insert([student1,student2]))

# 插入单条数据
student = {
    'id': '20170101',
    'name': 'Jordan',
    'age': 20,
    'gender': 'male'
}

result = my_set.insert_one(student)
print(result)
print(result.inserted_id)

# # 插入多条数据
student1 = {
    'id': '20170101',
    'name': 'Jordan',
    'age': 20,
    'gender': 'male'
}
student2 = {
    'id': '20170202',
    'name': 'Mike',
    'age': 21,
    'gender': 'male'
}
result = my_set.insert_many([student1, student2])
print(result)
print(result.inserted_ids)
# 查询
result = my_set.find_one({'name':'Mike'})
print(type(result),result)

# 根据ObjectId来查询
from bson.objectid import ObjectId
result = my_set.find_one({'_id': ObjectId('5b17ac771a9cb73eb846fcae')})
print(result)

# 单条数据的查询
results = my_set.find({'age': 20})
print(results)
for result in results:
    print(result)

# 多条数据的查询
results = my_set.find({'age': {'$gt': 20}})
print(results)
for result in results:
    print(result)

results = my_set.find({'name': {'$regex': '^M.*'}})
print(results)

# 计数
print('计数：',my_set.find().count())

# 升序排序
import pymongo
results = my_set.find().sort('name',pymongo.ASCENDING)
print([result['name'] for result in results])
# 降序排序
results = my_set.find().sort('name',pymongo.DESCENDING)
print([result['name'] for result in results])

# 偏移,偏移2，就忽略前两个元素，得到第三个及以后的元素
results = my_set.find().sort('name', pymongo.ASCENDING).skip(2)
print([result['name'] for result in results])

# 指定要取的结果个数
results = my_set.find().sort('name', pymongo.ASCENDING).skip(2).limit(2)
print([result['name'] for result in results])

#  单条更新
condition = {'name': 'Jordan'}
student = my_set.find_one(condition)
student['age'] = 26
result = my_set.update_one(condition, {'$set': student})
print(result)
print(result.matched_count, result.modified_count)

#  多条更新
condition = {'age': {'$gt': 20}}
result = my_set.update_many(condition, {'$inc': {'age': 1}})
print(result)
print(result.matched_count, result.modified_count)

# 删除单条数据
result = my_set.delete_one({'name': 'Kevin'})
print(result)
print(result.deleted_count)
# 删除多条数据
result = my_set.delete_many({'age': {'$lt': 25}})
print(result.deleted_count)