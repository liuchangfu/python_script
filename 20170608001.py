#输入用户名和密码，并校验；
# 用户名输入不对时，提示用户名不存在；
# 用户名输入正确时，提示用户输入密码，并校验，如果不对，提示用户重新输入；
print('用户名输入不对时，提示用户名不存在;\n用户名输入正确时，提示用户输入密码，并校验，如果不对，提示用户重新输入；\n')
while True:
    name = input('请输入用户名:')
    if name == 'Change':
        passwd =  input('请输入密码:')
        passwd1 = '123456'
        while passwd != passwd1:
            passwd=input('密码错误，请重新输入:')
        else:
            print('登录成功!!')
            break
    else:print('用户名不存在!!')
