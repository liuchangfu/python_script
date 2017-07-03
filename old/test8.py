print("你只有三次输入机会哦!!")
temp=input('你的数是字是多少：')
guess = int(temp)
i=1
while guess != 8 and i < 3:
    temp = input("猜错了，请重新输入吧：")
    i = i+1
    guess = int(temp)
    if guess == 8:
        print('哎呀，你竟然猜中了!!!')
        print('然而并没有什么卵用！')
    else:
        if guess > 8:
            print('大了！！！')
        else:
            print('少了！！！')
print("游戏结束，不玩了！！！")