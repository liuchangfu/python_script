import pytest

def um(a,b):
    return a*b

class TestUm():
    def setup(self):
        print("setup----->")

    def teardown(self):
        print("teardown-->")

    def setup_class(cls):
        print("\n")
        print("setup_class=========>")

    def teardown_class(cls):
        print("teardown_class=========>")

    def setup_method(self, method):
        print("setup_method----->>")

    def teardown_method(self, method):
        print("teardown_method-->>")

    def test_numbers_5_6(self):
        print ('test_numbers_5_6')
        assert um(5, 6) == 40

    def test_strings_b_2(self):
        print ('test_strings_b_2')
        assert um('b', 2) == 'bb'

if __name__ == '__main__':
    # 生成resultlog文件
    pytest.main(["-s","test_demo7.py","--resultlog=./log.txt"])
    # 生成JunitXML文件
    pytest.main(["-s", "test_demo7.py", "--junitxml=./log.xml"])
    # 创建测试用例的URL
    pytest.main(["-s", "test_demo7.py", "--pastebin=all"])
    # 生成html测试报告
    pytest.main(["-s","test_demo7.py","--html=./report1.html"])
    pytest.main(["-s","-v","test_demo7.py", "--html=./report2.html"])
