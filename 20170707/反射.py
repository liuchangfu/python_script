class Foo(object):
    def __init__(self):
        self.name = 'abc'

    def func(self):
        return 'func'

obj = Foo()

# #检查是否含有成员
# print(hasattr(obj,'name'))
# print(hasattr(obj,'func'))
# print(hasattr(obj,'func1'))
#
# #获取成员
# print(getattr(obj,'name'))
# print(getattr(obj,'func'))

#设置成员
print(setattr(obj,'age',18))
print(setattr(obj,'show',lambda num:num+1))

# #删除成员
# print(delattr(obj,'name'))
# print(delattr(obj,'func'))
