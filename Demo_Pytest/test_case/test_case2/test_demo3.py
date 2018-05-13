import pytest

def func(x):
    return  x+1

def test_func1():
    assert func(3) == 4

def test_func2():
    assert func(3) == 3

def test_func3():
    assert func(3) != 2

if __name__ == '__main__':
    pytest.main()