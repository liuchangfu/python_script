import random
ser = random.randint(1,10)
temp=input('你的数是字是多少：')
guess = int(temp)
while guess != ser:
    temp = input("猜错了，请重新输入吧：")
    guess = int(temp)
    if guess == ser:
        print('哎呀，你竟然猜中了!!!')
        print('然而并没有什么卵用！')
    else:
         if guess > ser:
             print('大了！！！')
         else:
            print('少了！！！')
print("游戏结束，不玩了！！！")