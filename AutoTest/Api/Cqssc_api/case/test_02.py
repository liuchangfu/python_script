import unittest
import requests

class TestTwoFaceDayStat(unittest.TestCase):

    def setUp(self):
        self.base_url = "https://mo.1394x.com/ssc/NumberStat?version=3000" #重庆时时彩中APP号码统计接口地址

    def test_status_code(self):
        """验证接口返回状态码是否是200"""
        st_code =  requests.get(self.base_url).status_code
        self.assertEqual(st_code,200)
        if st_code != 200:
            print("接口状态返回错误！！")

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()