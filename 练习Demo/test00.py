import  unittest

class TestSetup(unittest.TestCase):
    def setUp(self):
        print("测试开始前，我运行了！")

    def test01(self):
        self.assertEqual(-1,-1,"不相等")

    def test02(self):
        self.assertEqual(2, 2, "不相等")

    def tearDown(self):
        print("测试开始后，我运行了！")

if __name__ == '__main__':
    unittest.main()
