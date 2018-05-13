import pytest

def mul(a,b):
    return a*b

def setup_module(module):
    print ("\n")
    print ("setup_module================>")

def teardown_module(module):
    print ("teardown_module=============>")

def setup_function(function):
    print ("setup_function------>")

def teardown_function(function):
    print ("teardown_function--->")


def test_numbers_3_4():
    print ('test_numbers_3_4')
    assert mul(3,4) == 12


def test_strings_a_3():
    print ('test_strings_a_3')
    assert mul('a',3) == 'aaa'

if __name__ == '__main__':
    pytest.main (["-s", "test_demo6.py"])


