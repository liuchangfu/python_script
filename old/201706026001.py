def test1():
    print('in the test1')

def test2():
    print('in the test2')
    return 10

def test3():
    print('in the test4')
    return 0,10,['alex','name'],{'name':'alex'}

x=test1()
y=test2()
z=test3()
print(x)
print(y)
print(z)