print('我的python第一个游戏')
temp = input('不妨猜一下我的心中想的是那个数字：')
guess = int(temp)
if guess == 8:
    print('我草，你竟然猜中了')
    print('猜中有卵用')
else:
    print('猜错了，我的数字是8!')
print('游戏结束！')
