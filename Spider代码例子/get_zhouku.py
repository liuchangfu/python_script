# _*_ coding:utf-8 _*_
import requests
from bs4 import BeautifulSoup

url = 'http://www.zhuoku.com/'
response = requests.get(url)
response.encoding = 'gb2312'

soup = BeautifulSoup(response.text, 'lxml')

for li in soup.find_all('#zuixin>ul>li'):
    print(li)
