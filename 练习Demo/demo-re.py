# _*_ coding:utf-8 _*_
import re

# re.match 尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()就返回none。
print(re.match("www", "www.runoob.com").span())
print(re.match("com", "www.runoob.com"))

# groups() 返回一个包含所有小组字符串的元组，从 1 到 所含的小组号。
# group(num=0)  匹配的整个表达式的字符串，group() 可以一次输入多个组号，在这种情况下它将返回一个包含那些组所对应值的元组。
line = "Cats are smarter than dogs"
matchObj = re.match(r"(.*) are (.*?) (.*)", line, re.M | re.I)
if matchObj:
    print("matchObj.group() : ", matchObj.group())
    print("matchObj.group(1) : ", matchObj.group(1))
    print("matchObj.group(2) : ", matchObj.group(2))
    print("matchObj.group(3) :", matchObj.group(3))
else:
    print("No match!!")

# re.search 扫描整个字符串并返回第一个成功的匹配。
print(re.search("www", "www.runoob.com").span())  # 在起始位置匹配
print(re.search("com", "www.runoob.com").span())  # 不在起始位置匹配

# groups() 返回一个包含所有小组字符串的元组，从 1 到 所含的小组号。
# group(num=0)  匹配的整个表达式的字符串，group() 可以一次输入多个组号，在这种情况下它将返回一个包含那些组所对应值的元组。
line = "Cats are smarter than dogs"
searchObj = re.search(r"(.*) are (.*?) .*", line, re.M | re.I)
if searchObj:
    print("searchObj.group() : ", searchObj.group())
    print("searchObj.group(1) : ", searchObj.group(1))
    print("searchObj.group(2) : ", searchObj.group(2))
else:
    print("Nothing found!!")

# re.sub用于替换字符串中的匹配项。
phone = "2004-959-559 # 这是一个国外电话号码"
# 删除字符串中的 Python注释
num = re.sub(r"#.*$", "", phone)
print("电话号码是: ", num)

# 删除非数字(-)的字符串
num = re.sub(r"\D", "", phone)
print("电话号码是 : ", num)

# compile 函数用于编译正则表达式，生成一个正则表达式（ Pattern ）对象，供 match() 和 search() 这两个函数使用。
pattern = re.compile(r'\d+')
m = pattern.match('one12twothree34four')
print(m)

# 在字符串中找到正则表达式所匹配的所有子串，并返回一个列表，如果没有找到匹配的，则返回空列表。
pattern = re.compile(r'\d+')  # 查找数字
result1 = pattern.findall('runoob 123 google 456')
result2 = pattern.findall('run88oob123google456', 0, 10)

print(result1)
print(result2)

# 在字符串中找到正则表达式所匹配的所有子串，并把它们作为一个迭代器返回。
it = re.finditer(r"\d+","12a32bc43jf3")
for match in it:
    print (match.group() )