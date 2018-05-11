import unittest
import requests
import sys
sys.path.append("..")
from config import readconfigfile as con

class TestGetAwardData(unittest.TestCase):

    def setUp(self):
        self.host = con.get_url("baseurl")  # 接口地址
        self.base_url = self.host + "/ssc/GetAwardData?version=3000"  # 重庆时时彩中APP两面历史接口地址
        print(self.base_url)

    def test_status_code(self):
        """验证接口返回状态码是否是200"""
        st_code = requests.get(self.base_url).status_code
        st_json = requests.get(self.base_url).json()
        self.assertEqual(st_code, 200)
        if st_code != 200:
            print("接口状态返回错误！！")
        self.assertEqual(st_json['state'], 200)
        self.assertEqual(st_json['items']['state'], True)
        self.assertEqual(st_json['error'], None)
        print(len(st_json))
        self.assertNotEqual(len(st_json), 0)

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
