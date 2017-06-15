
# 文件逐行读取
import  os
f = open('E:\\python\\ex1.txt',encoding='UTF-8')
lines = f.readlines()
for line in lines:
    print(line,end='')
f.close()