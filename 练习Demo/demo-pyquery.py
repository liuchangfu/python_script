# _*_ coding:utf-8 _*_
from pyquery import PyQuery as pq

doc = pq('html')
# doc= py('http://www.qq.com')
# print(doc)

# 基本CSS选择器
from pyquery import PyQuery as pq
html = '''
    <div id="wrap">
        <ul class="s_from">
            asdasd
            <link href="http://asda.com">asdadasdad12312</link>
            <link href="http://asda1.com">asdadasdad12312</link>
            <link href="http://asda2.com">asdadasdad12312</link>
        </ul>
    </div>
'''
print("基本CSS选择器")
doc = pq(html)
print (doc("#wrap .s_from link"))

# 查找子元素
html = '''
    <div id="wrap">
        <ul class="s_from">
            asdasd
            <link href="http://asda.com">asdadasdad12312</link>
            <link href="http://asda1.com">asdadasdad12312</link>
            <link href="http://asda2.com">asdadasdad12312</link>
        </ul>
    </div>
'''
# 查找子元素
print("查找子元素")
doc = pq(html)
items=doc("#wrap")
print(items)
print("类型为:%s"%type(items))
link = items.find('.s_from')
print(link)
link = items.children()
print(link)

# 查找父元素
html = '''
    <div href="wrap">
        hello nihao
        <ul class="s_from">
            asdasd
            <link href="http://asda.com">asdadasdad12312</link>
            <link href="http://asda1.com">asdadasdad12312</link>
            <link href="http://asda2.com">asdadasdad12312</link>
        </ul>
    </div>
'''
print("查找父元素")
doc = pq(html)
items=doc(".s_from")
print(items)
# 查找父元素
parent_href=items.parent()
print(parent_href)

# 查找兄弟元素
html = '''
    <div href="wrap">
        hello nihao
        <ul class="s_from">
            asdasd
            <link class='active1 a123' href="http://asda.com">asdadasdad12312</link>
            <link class='active2' href="http://asda1.com">asdadasdad12312</link>
            <link class='movie1' href="http://asda2.com">asdadasdad12312</link>
        </ul>
    </div>
'''
print("查找兄弟元素")
doc = pq(html)
items=doc("link.active1.a123")
print(items)
#查找兄弟元素
siblings_href=items.siblings()
print(siblings_href)

# 遍历查找结果
html = '''
    <div href="wrap">
        hello nihao
        <ul class="s_from">
            asdasd
            <link class='active1 a123' href="http://asda.com">asdadasdad12312</link>
            <link class='active2' href="http://asda1.com">asdadasdad12312</link>
            <link class='movie1' href="http://asda2.com">asdadasdad12312</link>
        </ul>
    </div>
'''
print("遍历查找结果")
doc = pq(html)
its=doc("link").items()
for it in its:
    print(it)

# 获取属性信息
html = '''
    <div href="wrap">
        hello nihao
        <ul class="s_from">
            asdasd
            <link class='active1 a123' href="http://asda.com">asdadasdad12312</link>
            <link class='active2' href="http://asda1.com">asdadasdad12312</link>
            <link class='movie1' href="http://asda2.com">asdadasdad12312</link>
        </ul>
    </div>
'''
print("获取属性信息")
doc = pq(html)
its=doc("link").items()
for it in its:
    print(it.attr('href'))
    print(it.attr.href)

# 获取文本
html = '''
    <div href="wrap">
        hello nihao
        <ul class="s_from">
            asdasd
            <link class='active1 a123' href="http://asda.com">asdadasdad12312</link>
            <link class='active2' href="http://asda1.com">asdadasdad12312</link>
            <link class='movie1' href="http://asda2.com">asdadasdad12312</link>
        </ul>
    </div>
'''
print("获取文本")
doc = pq(html)
its=doc("link").items()
for it in its:
    print(it.text())

# 获取 HTML信息
html = '''
    <div href="wrap">
        hello nihao
        <ul class="s_from">
            asdasd
            <link class='active1 a123' href="http://asda.com"><a>asdadasdad12312</a></link>
            <link class='active2' href="http://asda1.com">asdadasdad12312</link>
            <link class='movie1' href="http://asda2.com">asdadasdad12312</link>
        </ul>
    </div>
'''
print("获取 HTML信息")
doc = pq(html)
its=doc("link").items()
for it in its:
    print(it.html())

# 添加，移除class标签
html = '''
    <div href="wrap">
        hello nihao
        <ul class="s_from">
            asdasd
            <link class='active1 a123' href="http://asda.com"><a>asdadasdad12312</a></link>
            <link class='active2' href="http://asda1.com">asdadasdad12312</link>
            <link class='movie1' href="http://asda2.com">asdadasdad12312</link>
        </ul>
    </div>
'''
print('添加，移除class标签')
doc = pq(html)
its=doc("link").items()
for it in its:
    print("添加:%s"%it.addClass('active1'))
    print("移除:%s"%it.removeClass('active1'))

# attr 为获取/修改属性 css 添加style属性

html = '''
    <div href="wrap">
        hello nihao
        <ul class="s_from">
            asdasd
            <link class='active1 a123' href="http://asda.com"><a>asdadasdad12312</a></link>
            <link class='active2' href="http://asda1.com">asdadasdad12312</link>
            <link class='movie1' href="http://asda2.com">asdadasdad12312</link>
        </ul>
    </div>
'''
print(" attr 为获取/修改属性 css 添加style属性")
doc = pq(html)
its=doc("link").items()
for it in its:
    print("修改:%s"%it.attr('class','active'))
    print("添加:%s"%it.css('font-size','14px'))


# 移除标签
html = '''
    <div href="wrap">
        hello nihao
        <ul class="s_from">
            asdasd
            <link class='active1 a123' href="http://asda.com"><a>asdadasdad12312</a></link>
            <link class='active2' href="http://asda1.com">asdadasdad12312</link>
            <link class='movie1' href="http://asda2.com">asdadasdad12312</link>
        </ul>
    </div>
'''
print('移除标签')
doc = pq(html)
its=doc("div")
print('移除前获取文本结果:\n%s'%its.text())
it=its.remove('ul')
print('移除后获取文本结果:\n%s'%it.text())

# 伪类选择器
html = '''
    <div href="wrap">
        hello nihao
        <ul class="s_from">
            asdasd
            <link class='active1 a123' href="http://asda.com"><a>helloasdadasdad12312</a></link>
            <link class='active2' href="http://asda1.com">asdadasdad12312</link>
            <link class='active3' href="http://asda2.com">asdadasdad12312</link>
        </ul>
    </div>
'''
print('伪类选择器')
doc = pq(html)
its=doc("link:first-child")
print('第一个标签:%s'%its)
its=doc("link:last-child")
print('最后一个标签:%s'%its)
its=doc("link:nth-child(2)")
print('第二个标签:%s'%its)
its=doc("link:gt(0)") #从零开始
print("获取0以后的标签:%s"%its)
its=doc("link:nth-child(2n-1)")
print("获取奇数标签:%s"%its)
its=doc("link:contains('hello')")
print("获取文本包含hello的标签:%s"%its)