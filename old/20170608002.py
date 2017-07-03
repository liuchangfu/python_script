num = int(input('请输入1-100的数字:'))
y = 10
for x in range(1,101):
    if x == y:
        print('找到数字:',x)
        break
    else:
        print('没有找到数字')