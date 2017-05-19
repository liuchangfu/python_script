# 以下实例为通过用户输入两个数字，并计算连个数字之和：

# 用户输入数字

num1 = float(input('请输入第一个数字:'))

num2 = float(input('请输入第二个数字:'))

# 求和

sum = num1 + num2

# 打印求和结果

print('数字{0}数字{1}相加的结果为:{2}'.format(num1,num2,sum))