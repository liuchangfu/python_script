# 文件逐行读取
import  os
f = open('E:\\python\\ex1.txt')
lines = f.readlines()
for line in lines:
    print(line)
f.close()
