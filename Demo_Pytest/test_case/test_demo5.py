import pytest

def add(x,y):
    return x+y

def test_add1():
    assert add(3, 4) == 7

def test_add2():
    assert add(5,1) != 6

def test_add3():
    assert add(5,0) >= 6

def test_add4():
    assert add(2,1) <= 4

if __name__ == '__main__':
    pytest.main(["test_demo5.py"])