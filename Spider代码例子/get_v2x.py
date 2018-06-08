# _*_ coding:utf-8 _*_
import requests
from bs4 import BeautifulSoup
"""
在v2ex主页的右侧一般有个最热主题区域，里面列出了当日的热门讨论话题。这一节里我们就尝试使用爬虫技术获取这些热门主题文本和链接。
"""
url = 'https://www.v2ex.com/'
soup = BeautifulSoup(requests.get(url).text, 'html.parser')
# 遍历所有的class=item_hot_topic_title的span
for span in soup.find_all('span', class_='item_hot_topic_title'):
    # 打印a标签中的文本，打印a标签中的链接地址
    print(span.find('a').text, span.find('a')['href'])