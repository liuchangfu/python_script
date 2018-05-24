# _*_ coding:utf-8 _*_
from bs4 import BeautifulSoup

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
# 实例化html
soup = BeautifulSoup(html_doc,'lxml')
# 格式化
print(soup.prettify())
# 打印title
print(soup.title)
# 打印title，并以字符串输出
print(soup.title.string)
# 打印title的父节点
print(soup.title.parent.name)
# 打印p标签
print(soup.p)
# 打印p标签中的class值
print(soup.p['class'])
# 打印a标签
print(soup.a)
# 打印所有a标签
print(soup.find_all('a'))
# 打印id="link3"的标签
print(soup.find(id="link3"))
# 从文档中找到所有<a>标签的链接
for link in soup.find_all('a'):
    print(link.get('href'))
# 从文档中获取所有文字内容:
print(soup.get_text())

# 将一段文档传入BeautifulSoup 的构造方法,就能得到一个文档的对象, 可以传入一段字符串或一个文件句柄.
soup1 = BeautifulSoup(open('demo.html'),'lxml')
print(soup1)

soup2 = BeautifulSoup('<html>data</html>','lxml')
print(soup2)

soup3 = BeautifulSoup('<b class="boldest">Extremely bold</b>','lxml')
tag = soup3.b
print(type(tag))
print(tag.name)

tag.name = "blockquote"
print(tag)

print(tag['class'])

# 一个tag可能有很多个属性
print(tag.attrs)

# tag的属性可以被添加,删除或修改
tag['class'] = 'verybold'
tag['id'] = 1
print(tag)

del tag['class']
del tag['id']
print(tag)