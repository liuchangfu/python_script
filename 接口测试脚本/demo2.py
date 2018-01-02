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
encode  编码，将对象转换为json
decode   解码，将json转化为对象
'''
class JenkinsGet(unittest.TestCase):# TODO json解析会报错,google一直没有找到解决办法，先挂起！！！
    def setUp(self):
        self.r = requests.get('http://localhost:8080/api/json?tree=jobs[name]')

    def test_get_all_job_names(self):
        result = self.r.text
        json_result = json.loads(result)
        print(json_result)
        self.assertEqual(json_result['jobs'][0]['name'], 'fisrt_job')
        self.assertEqual(json_result['jobs'][0]['name'], 'second_job')

    # def test_get_all_job_names(self):
    #     json_result = self.r.json()
    #     print(json_result)
    #     self.assertEqual(json_result['jobs'][0]['name'], 'fisrt_job')
    #     self.assertEqual(json_result['jobs'][0]['name'], 'second_job')



if __name__ == '__main__':
    unittest.main()