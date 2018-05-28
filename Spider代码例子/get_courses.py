# _*_ coding:utf-8 _*_
import requests
from bs4 import BeautifulSoup
"""
抓取重定向科技目前开设的所有测试课程
"""
# 定义被抓取页面的url
url= "http://www.itest.info/courses"
# 获取被抓取页面的html代码，并使用html.parser来实例化BeautifulSoup，属于固定套路
soup = BeautifulSoup(requests.get(url).text,'html.parser')
# 遍历页面上所有的h4
for coures in soup.find_all('h4'):
    # 打印出h4的text属性
    print(coures.text)
