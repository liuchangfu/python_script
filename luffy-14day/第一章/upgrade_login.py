# 定义用户输入次数计数器
count = 0

# 嵌套列表存储用户名和密码
usr_list = [['user1', '1234'], ['user2', '12345'], ['user3', '123456']]

while True:
    username = (input('请输入用户名:')).strip()
    if len(username) == 0:
        print('对不起，您没有输入用户名，请重新输入！！')
        continue
    # 检查加锁用户名是否在user_lock.txt中
    f = open('user_lock.txt', 'r+',encoding='utf-8')
    f_lock = f.read()
    f.close()
    if username in f_lock:
        print('用户名已锁定,请更换其它用户名！！')
        continue

    while True:
        password = input('请输入密码:')
        if [username, password] in usr_list:
            print('登录成功！！')
            exit()
        else:
            print('密码错误，请重新输入密码！！')
            count = count + 1
        # 用户密码超过3次，把用户写入user_lock.txt文件
        if count == 3:
            user_lock = open('user_lock.txt', 'a+',encoding='utf-8')
            user_lock.write(username + "\n")
            user_lock.close()
            print("%s用户输入密码已超过3次，将被锁定！！" % username)
            exit()
