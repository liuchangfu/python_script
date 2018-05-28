# _*_ coding:utf-8 _*_
"""
获取知乎每日及每月最热问题的功能。
"""
import requests
from bs4 import BeautifulSoup


def get_zhihu():
    url = 'https://www.zhihu.com/explore'
    print(url)
    headers = {
        'user-agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36"}
    soup = BeautifulSoup(requests.get(url, headers=headers).text, 'html.parser')
    for link in soup.find_all('a', class_='question_link'):
        print(link.text)


get_zhihu()
