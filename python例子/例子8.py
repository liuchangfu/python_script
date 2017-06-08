# 以下实例通过使用 if...elif...else 语句判断数字是正数、负数或零：

num =  float(input('请输入一个数字:'))

if num >= 0:
    print('您输入的是一个正数。')
elif num == 0:
    print('您输入是零!!')
else:
    print('您输入是一个负数。')