# 整数的阶乘（英语：factorial）是所有小于及等于该数的正整数的积，0的阶乘为1。即：n!=1×2×3×...×n。

num = int(input('请输入一个数字:'))
f = 1

if num < 0:
    print('抱歉，负数没有阶乘')
elif num == 0:
    print('0 的阶乘为 1')
else:
    for i in range(1,num+1):
        f= f * i
    print('%d的阶乘为%d'%(num,f))
