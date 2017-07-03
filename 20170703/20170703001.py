'''
多个实参，放到一个元组里面,以*开头，可以传多个参数；**是形参中按照关键字传值把多余的传值以字典的方式呈现
*args：（表示的就是将实参中按照位置传值，多出来的值都给args，且以元祖的方式呈现）
'''
#*args：（表示的就是将实参中按照位置传值，多出来的值都给args，且以元祖的方式呈现）
#示例1
def foo(x,*args):
    print(x)
    print(args)

foo(1,2,3,4,5)
print ('------------------我是分隔符-----------------')
#示例2  三者顺序是:位置参数、默认参数、*args
def foo1(x,y=1,*args):
    print(x)
    print(y)
    print(args)

foo1(1,2,3,4,5)
print ('------------------我是分隔符-----------------')
#示例3 三者顺序是:位置参数、*args、默认参数
def foo2 (x,*args,y=1):
    print(x)
    print(args)
    print(y)

foo2(1,2,3,4,5)
print ('------------------我是分隔符-----------------')

#**kwargs：（表示的就是形参中按照关键字传值把多余的传值以字典的方式呈现）

def foo3(x,**kwargs):
    print(x)
    print(kwargs)

foo3(1,y=1,a=2,b=3,c=4)
print ('------------------我是分隔符-----------------')

# 位置参数、*args、**kwargs三者的顺序必须是位置参数、*args、**kwargs
def foo4(x,*args,**kwargs):
    print(x)
    print(args)
    print(kwargs)

foo4(1,2,3,4,y=1,a=2,b=3,c=4)

print ('------------------我是分隔符-----------------')
# 位置参数、默认参数、**kwargs三者的顺序必须是位置参数、默认参数、**kwargs
def foo5(x,y=1,**kwargs):
    print(x)
    print(y)
    print(kwargs)

foo5(1,a=2,b=3,c=4)
