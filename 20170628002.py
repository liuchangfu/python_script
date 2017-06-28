def outer(func):
    # func值的是函数f1，也就是装饰器装饰的函数
    def log():
        print('out log')
        # f1函数会被当作参数来传递,这里等价于调用f1()函数
        func()
        # 返回值重新赋值给f1函数
    return log

@outer
def f1():
    print('函数f1')

f1()