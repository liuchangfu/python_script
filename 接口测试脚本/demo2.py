import unittest
import json
import requests
import demjson
'''
安装： pip install demjson
使用：  json_obj = demjson(json_string)

demjson的介绍
快速说明： http://deron.meranda.us/python/demjson/
demjson有两个主要的方法：
encode  将Python对象编码成JSON字符串
decode  将已编码的JSON字符串解码为Python对象
'''
class JenkinsGet(unittest.TestCase):# TODO TypeError: string indices must be integers

    def setUp(self):
         self.r = requests.get('http://localhost:8080/api/json?tree=jobs[name]')

    # def test_get_all_job_names(self):
    #     result = demjson.encode(self.r.text)
    #     json_result = json.loads(result)
    #     print(json_result)
    #     self.assertEqual(json_result['jobs'][0]['name'], 'fisrt_job')
    #     self.assertEqual(json_result['jobs'][1]['name'], 'second_job')

    def test_get_all_job_names(self):
         json_result =demjson.encode(self.r)
         print(json_result)
         self.assertEqual(json_result['jobs'][0]['name'], 'fisrt_job')
         self.assertEqual(json_result['jobs'][1]['name'], 'second_job')


if __name__ == '__main__':
    unittest.main()

