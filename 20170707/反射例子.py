#反射说简单点 --> 就是利用字符串的形式去对象(模块)中操作(寻找/检查/删除/设置)成员。

import commons
def run():
    #利用字符串的形式去对象(模块)中操作(寻找/检查/删除/设置)成员 反射
    imp = input('请输入一个方法:')   #比如login
    # delattr()  删除内存里面的方法
    # setattr()  #设置内存里面的方法
    if hasattr(commons,imp):  #判断有没有这个方法
       fuc = getattr(commons,imp)  #获得这个方法
       fuc()   #会调用 commons文件里面的方法
    else:
        print('404')


run()