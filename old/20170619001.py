age = 25

guess_age= int(input('请输入年龄:'))

if guess_age == age:
    print('猜对了！！')
elif guess_age > age:
    print('猜大了！！')
else:
    print('猜小了！！')
