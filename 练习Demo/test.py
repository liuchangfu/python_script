# def is_odd(n):
#     return n % 2 == 1
#
# L = list(filter(is_odd, range(1, 20)))
# print(L)

# n = 20
# list=[]
# L= lambda n:n%2==1
# print(list.append(L))

# import random
# num  ="13800000"
# a = str(random.randrange(0,9999))
# num = num+a
# print(num)

a = [13800000000]
b= []

for i in range(5):
    number = a[-1]
    b.append(a)
    a = b
    print("空列表：", b)
print("原始列表修改后:", a)

