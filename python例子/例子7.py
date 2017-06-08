# 以下实例通过用户输入两个变量，并相互交换：

a = input('请输入a的值：')

b =  input('请输入b的值：')

temp = a

a = b

b = temp

print('交换后a的值为:{}'.format(a))

print('交换后b的值为:{}'.format(b))

