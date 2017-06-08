# 输出指定范围内的质数

Min  = int(input('请输入区间最小值:'))

Max  = int(input('请输入区间最大值:'))

for num in range(Min,Max+1):
    if num > 1:
        for i in range(2,num):
            if (num % i ==0):
                break
        else:
            print(num)
