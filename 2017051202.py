#斐波那契数列指的是这样一个数列 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233，377，610，987，1597，2584，4181，6765，10946，17711，28657，46368........
# 这个数列从第3项开始，每一项都等于前两项之和。

def fab(n):
    a1=1
    a2=1
    a3=1
    if n  < 1:
        print('输入有误！')
        return
    while n-2 > 0:
        a3 = a1+a2
        a1 = a2
        a2 = a3
        n = n-1
    return a3

result = fab(5)
if result != -1:
    print('总共有%d对小兔子崽诞生!'% result)