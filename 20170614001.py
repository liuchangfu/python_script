#输入用户名和密码，验证用户名和密码，验证成功后，打印欢迎信息，如密码输错3次，锁定用户！！！！
import os,sys
name = 'Change'
password = '123456'
times = 3
count = 0
#验证用户名
while True:
    input_name =input('请输入用户名:')
    if len(input_name) == 0:
        print('用户名不能输入为空!!!')
    elif input_name != name:
        print('用户不存在,请重新输入用户名!!')
    elif input_name == name:
        break
#验证密码，输错3次锁定用户
while True:
        input_passwd=input('请输入密码:')
        if len(input_passwd) == 0:
            print('密码不能为空!!!')
            continue
        elif input_passwd == password:
            print('%s,登录成功！！'% input_name)
            break
        elif count < 2:
            count = count + 1
            print('密码输入错误,请重新输入,您还有%d次输入机会!!' % (times-count))
        elif count == 2:
            print('密码输错三次，%s用户已锁定!!!!' % name)
            f=open('E:\\python\\lock_user.txt','w')
            f.write(name+'\n')
            f.close()
            break








