
def add(x,y):
    return x+y

def test_add():
    assert add(1,0) == 1
    assert add(1,1) == 2
    assert add(1,99) == 100

def func():
    return 3

def test_func():
    assert func() == 4