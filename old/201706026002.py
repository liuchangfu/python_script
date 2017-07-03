def test1(*args):
    print(args)

def test2(x,*args):
    print(x,args)

def test3(**kwargs):
    print(kwargs)


test1(1,2,3,4)

test2(1,4,4,4,4,4,4)

test3(name='alex',age=8)