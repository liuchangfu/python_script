#创建类
class Foo(object):
    #创建类中的函数
    def Bar(self):
        print('Bar')

    def hello(self,name):
        print('I am %s' %name )

#根据类Foo创建对象b1
b1=Foo()
b1.Bar() # 执行Bar
b1.hello('Change') #执行hello方法

#第一步：将内容封装到某处

#创建类
class Foo1(object):
    def __init__(self,name,age): #构造函数，根椐类对象创建对象时自动执行
        self.name =  name
        self.age = age

#根据类Foo1创建对象
#自动执行Foo1类的__init__方法
obj1=Foo1('Change',18) #将change和18分别封装到obj1/self的name和age属性
#根据类Foo1创建对象
#自动执行Foo1类的__init__方法
obj2=Foo1('Alex',18) #将alex和18分别封装到obj1/self的name和age属性


#第二步：从某处调用被封装的内容

# 通过对象直接调用被封装的内容

class Foo2(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

obj3 = Foo2('wupeiqi', 18)
print (obj3.name)  # 直接调用obj1对象的name属性
print (obj3.age)  # 直接调用obj1对象的age属性

obj4 = Foo2('alex',73)
print (obj4.name) # 直接调用obj2对象的name属性
print (obj4.age) # 直接调用obj2对象的age属性

# 通过self间接调用被封装的内容
class Foo3(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def detail(self):
        print(self.name)
        print(self.age)


obj5 = Foo3('wupeiqi', 18)
obj5.detail()  # Python默认会将obj5传给self参数，即：obj5.detail(obj1)，所以，此时方法内部的 self ＝ obj5，即：self.name 是 wupeiqi ；self.age 是 18

obj6 = Foo3('alex', 73)
obj6.detail()  # Python默认会将obj6传给self参数，即：obj6.detail(obj2)，所以，此时方法内部的 self ＝ obj2，即：self.name 是 alex ； self.age 是 78

