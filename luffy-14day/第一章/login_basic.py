# 定义计数器
count = 0

# 定义初始化用户名和密码
username = "change"
password = 123456

while True:
    username = (input('请输入用户名:')).strip()
    password = input('请输入密码:')
    if username == 'change' and password == '123456':
        print('登录成功')
        break
    else:
        print('登录失败,请重新输入！！')
        count += 1

    if count == 3:
        print('登录次数，已超过三次，即将退出！！')
        break
