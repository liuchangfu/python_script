# 求输入的数的阶乘
def rec1(n):
     result = n
     for i in range(1,n):
         result = i * n
     return result

number = int(input('请输入一个整数：'))
result = rec1(number)
print("%d的阶乘是：%d" % (number,result))


