# _*_ coding:utf-8 _*_
from lxml import etree
# text = '''
# <div>
#     <ul>
#          <li class="item-0"><a href="link1.html">first item</a></li>
#          <li class="item-1"><a href="link2.html">second item</a></li>
#          <li class="item-inactive"><a href="link3.html">third item</a></li>
#          <li class="item-1"><a href="link4.html">fourth item</a></li>
#          <li class="item-0"><a href="link5.html">fifth item</a>
#      </ul>
#  </div>
# '''
# 运行结果中不仅补全了 li 标签，还添加了 body，html 标签。
# html = etree.HTML(text)
# res = etree.tostring(html)
# print(res)

# 利用 parse 方法来读取文件
# html = etree.parse('demo.html')
# res = etree.tostring(html,pretty_print=True)
# print(res)

html = etree.parse("demo.html")
# print(type(html))

# 获取所有的 <li> 标签
# res = html.xpath('//li')
# print(res)
# print(type(res))
# print(type(res[0]))

# 获取 <li> 标签的所有 class
res = html.xpath('//li/@class')
print(res)

# 获取 <li> 标签下 href 为 link1.html 的 <a> 标签
res = html.xpath('//li/a[@href="link1.html"]')
print(res)

# 因为 / 是用来获取子元素的，而 <span> 并不是 <li> 的子元素，所以，要用双斜杠
# 获取 <li> 标签下的所有 <span> 标签
res = html.xpath('//li//span')
print(res)

# 获取 <li> 标签下的所有 class，不包括 <li>
result = html.xpath('//li/a//@class')
print (result)

# 获取最后一个 <li> 的 <a> 的 href
result = html.xpath('//li[last()]/a/@href')
print (result)

# 获取倒数第二个元素的内容
result = html.xpath('//li[last()-1]/a')
print (result[0].text)

# 获取 class 为 bold 的标签名
result = html.xpath('//*[@class="bold"]')
print (result[0].tag)