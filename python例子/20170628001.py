def outer(func):
    def log():
        print('打印LOG!!!!!')
        func()
    return log
@outer
def f1():
    print('打印AAAA')

@outer
def f2():
    print('打印BBBB')

@outer
def f3():
    print('打印CCCC')

f1()
f2()
f3()
