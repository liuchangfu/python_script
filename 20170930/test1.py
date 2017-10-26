from string import Template
num = 100
print("*"*50)
print("%d to hex is %x" % (num,num))
print("%d to hex is %X" % (num,num))
print("%d to hex is %#x" % (num,num))
print("%d to hex is %#X" % (num,num))
print("*"*50)
f = 3.1415926
print("value of is:%.4f" %f)
print("*"*50)
student=[{"name":"wilber","age":27},{"name":"Will","age":28},{"name":"June","age":27}]
print("name:%10s,age:%10d" % ((student[0]["name"]),student[0]["age"]))
print("name:%-10s,age:%-10d" % ((student[1]["name"]),student[1]["age"]))
print("name:%*s,age:%*d" % (10,student[2]["name"],10,student[2]["age"]))

for student in student:
    print("%(name)s is %(age)d years old" %student)

print("*"*50)
# 位置参数
print ("{0} is {1} years old".format("Wilber", 28))
print ("{} is {} years old".format("Wilber", 28))
print ("Hi, {0}! {0} is {1} years old".format("Wilber", 28))

# 关键字参数
print ("{name} is {age} years old".format(name = "Wilber", age = 28))

# 下标参数
li = ["Wilber", 28]
print ("{0[0]} is {0[1]} years old".format(li))

# 填充与对齐
# ^、<、>分别是居中、左对齐、右对齐，后面带宽度
# :号后面带填充的字符，只能是一个字符，不指定的话默认是用空格填充
print ('{:>8}'.format('3.14'))
print ('{:<8}'.format('3.14'))
print ('{:^8}'.format('3.14'))
print ('{:0>8}'.format('3.14'))
print ('{:a>8}'.format('3.14'))

# 浮点数精度
print ('{:.4f}'.format(3.1415926))
print ('{:0>10.4f}'.format(3.1415926))

# 进制
# b、d、o、x分别是二进制、十进制、八进制、十六进制
print ('{:b}'.format(11))
print ('{:d}'.format(11))
print ('{:o}'.format(11))
print ('{:x}'.format(11))
print ('{:#x}'.format(11))
print ('{:#X}'.format(11))

# 千位分隔符
print ('{:,}'.format(15700000000))